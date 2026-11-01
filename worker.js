export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    // 旧URL（*.workers.dev）と www 付きは bengoshun.com へ301転送し、評価の分散を防ぐ
    if (url.hostname.endsWith(".workers.dev") || url.hostname === "www.bengoshun.com") {
      url.hostname = "bengoshun.com";
      return Response.redirect(url.toString(), 301);
    }
    // .html 付きURLは拡張子なしの正規URLへ301転送する
    // （Cloudflare Assets の既定は307＝一時転送のため、Googleが .html 版を索引に残して評価が分散する）
    if (url.pathname.endsWith(".html")) {
      url.pathname = url.pathname.endsWith("/index.html")
        ? url.pathname.slice(0, -"index.html".length)
        : url.pathname.slice(0, -".html".length);
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
