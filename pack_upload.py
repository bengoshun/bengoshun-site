# -*- coding: utf-8 -*-
"""GitHubアップロード用に、前回から変更・追加されたファイルを100個単位の
バッチフォルダにまとめるスクリプト。

使い方:
  python3 pack_upload.py          # 前回パック以降に変更されたファイルだけをまとめる
  python3 pack_upload.py --all    # 全ファイルをまとめ直す（初回アップロードやアップロード失敗時）

出力:
  upload/batch_01/, upload/batch_02/, ... （各フォルダ最大100ファイル・元のフォルダ構造を保持）

GitHubでのアップロード手順:
  1. GitHubのリポジトリページで「Add file → Upload files」を開く
  2. Finderで upload/batch_01 を開き、中身を全選択（Cmd+A）してドラッグ&ドロップ
     ※ batch_01フォルダ自体ではなく「中身」をドラッグすること（フォルダ構造が保たれます）
  3. Commit changes を押す
  4. batch_02 以降も同様に繰り返す
"""
import hashlib
import json
import os
import shutil
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE, "upload")
MANIFEST = os.path.join(BASE, ".upload_manifest.json")
BATCH_SIZE = 100
EXCLUDE_DIRS = {".git", "upload", "__pycache__", "node_modules"}
EXCLUDE_FILES = {".upload_manifest.json", ".DS_Store", "pack_upload.py"}


def file_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def collect_files():
    files = {}
    for root, dirs, names in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for name in names:
            if name in EXCLUDE_FILES:
                continue
            full = os.path.join(root, name)
            rel = os.path.relpath(full, BASE)
            files[rel] = file_hash(full)
    return files


def main():
    repack_all = "--all" in sys.argv

    current = collect_files()
    previous = {}
    if os.path.exists(MANIFEST) and not repack_all:
        with open(MANIFEST) as f:
            previous = json.load(f)

    changed = sorted(rel for rel, h in current.items() if previous.get(rel) != h)
    deleted = sorted(rel for rel in previous if rel not in current)

    if not changed and not deleted:
        print("変更されたファイルはありません。")
        return

    # 出力先を作り直す
    if os.path.exists(UPLOAD_DIR):
        shutil.rmtree(UPLOAD_DIR)
    os.makedirs(UPLOAD_DIR)

    batches = [changed[i:i + BATCH_SIZE] for i in range(0, len(changed), BATCH_SIZE)]
    for n, batch in enumerate(batches, 1):
        batch_dir = os.path.join(UPLOAD_DIR, f"batch_{n:02d}")
        for rel in batch:
            dst = os.path.join(batch_dir, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(os.path.join(BASE, rel), dst)
        print(f"batch_{n:02d}: {len(batch)}ファイル")

    # マニフェスト更新
    with open(MANIFEST, "w") as f:
        json.dump(current, f, ensure_ascii=False, indent=0)

    print(f"\n合計 {len(changed)}ファイル → {len(batches)}バッチを upload/ に作成しました。")
    print("各 batch_XX フォルダの「中身」をGitHubの Upload files 画面に")
    print("ドラッグ&ドロップしてください（1バッチ＝1コミット）。")
    if deleted:
        print("\n【注意】前回から削除されたファイルがあります。GitHub上で手動削除してください:")
        for rel in deleted:
            print("  -", rel)
    print("\n※アップロードに失敗した場合は `python3 pack_upload.py --all` で全ファイルをまとめ直せます。")


if __name__ == "__main__":
    main()
