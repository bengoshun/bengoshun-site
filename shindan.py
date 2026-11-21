# -*- coding: utf-8 -*-
"""診断ツール（日本語ページ専用）のデータ。build.py が from shindan import ... で読む。

ソースは単体HTML（~/Downloads/*.html）で、/tmp/gen_shindan.py が変換して生成する。
css はページの <head> に、body・js はそのまま <main> 内に出力される。
クラス名・CSS変数はサイト側 style.css と衝突しないよう接頭辞を付けてある。"""

SHINDAN = [
    dict(
        slug="""harassment""",
        pfx="""hsd""",
        title="""職場のハラスメント対策 総合診断""",
        desc="""セクハラ・妊娠出産等・育児介護・パワハラに加え、2026年10月1日から義務化されたカスタマーハラスメントと就職活動中の学生等へのセクハラまで。厚生労働省の6つの指針に共通する措置の枠組みで、自社の対策を16問でセルフチェックできます。入力内容は送信されません。""",
        summary="""6つのハラスメント指針に共通する措置の枠組みで、方針の明確化・相談体制・発生後の対応・プライバシー保護・類型別の措置を16問でチェックします。""",
        tag="""16問 ／ 5分""",
        css="""  .hsd{
    --hsd-main:#1f5f5a; --hsd-main2:#2c7a73; --hsd-bg:#f4f8f7; --hsd-card:#ffffff;
    --hsd-ok:#2e7d52; --hsd-mid:#b07820; --hsd-ng:#b03a3a; --hsd-line:#dbe5e3;
  }
  .hsd *{box-sizing:border-box; margin:0; padding:0;}
  .hsd{font-family:"Hiragino Kaku Gothic ProN","Hiragino Sans","Yu Gothic","Meiryo",sans-serif;
       background:var(--hsd-bg); color:#2a2f36; line-height:1.75; padding:24px 12px; border-radius:8px;}
  .hsd .wrap{max-width:760px; margin:0 auto;}
  .hsd .head{background:var(--hsd-main); color:#fff; border-radius:10px 10px 0 0; padding:26px 24px;}
  .hsd .head h1{font-size:1.35rem; line-height:1.5;}
  .hsd .head p{font-size:.86rem; margin-top:10px; opacity:.92;}
  .hsd .hsdlead{background:var(--hsd-card); border:1px solid var(--hsd-line); border-top:none; padding:20px 24px; font-size:.92rem;}
  .hsd .hsdlead strong{color:var(--hsd-main);}
  .hsd .hsdcat{background:var(--hsd-card); border:1px solid var(--hsd-line); border-radius:8px; margin-top:18px; overflow:hidden;}
  .hsd .hsdcat h2{background:var(--hsd-main2); color:#fff; font-size:1rem; padding:10px 18px;}
  .hsd .hsdcat h2 small{font-weight:normal; font-size:.78rem; opacity:.9; margin-left:8px;}
  .hsd .q{padding:16px 18px; border-top:1px solid var(--hsd-line);}
  .hsd .q:first-of-type{border-top:none;}
  .hsd .q .qt{font-size:.95rem; font-weight:600; margin-bottom:10px;}
  .hsd .q .qt .num{display:inline-block; background:var(--hsd-main); color:#fff; border-radius:4px;
       font-size:.78rem; padding:1px 8px; margin-right:8px; vertical-align:2px;}
  .hsd .opts{display:flex; gap:8px; flex-wrap:wrap;}
  .hsd .opts label{flex:1 1 30%; min-width:110px; text-align:center; border:1.5px solid var(--hsd-line);
       border-radius:6px; padding:8px 6px; font-size:.88rem; cursor:pointer; background:#fafbfd; user-select:none;}
  .hsd .opts input{display:none;}
  .hsd .opts input:checked + span{display:block; margin:-8px -6px; padding:8px 6px; border-radius:4.5px;
       background:var(--hsd-main); color:#fff; font-weight:600;}
  .hsd .btnrow{text-align:center; margin:26px 0 8px;}
  .hsd button.go{background:var(--hsd-main); color:#fff; border:none; border-radius:8px;
       font-size:1.05rem; font-weight:700; padding:14px 52px; cursor:pointer;}
  .hsd button.go:hover{background:var(--hsd-main2);}
  .hsd .warn{display:none; text-align:center; color:var(--hsd-ng); font-size:.88rem; margin-top:8px;}
  .hsd #hsdResult{display:none; margin-top:24px;}
  .hsd .score{background:var(--hsd-card); border:2px solid var(--hsd-main); border-radius:10px; padding:22px 24px; text-align:center;}
  .hsd .score .pct{font-size:2.6rem; font-weight:800; color:var(--hsd-main);}
  .hsd .score .lvl{font-size:1.1rem; font-weight:700; margin-top:4px;}
  .hsd .score .lvl.ok{color:var(--hsd-ok);} .hsd .score .lvl.mid{color:var(--hsd-mid);} .hsd .score .lvl.ng{color:var(--hsd-ng);}
  .hsd .score .msg{font-size:.9rem; margin-top:10px; text-align:left;}
  .hsd .catres{background:var(--hsd-card); border:1px solid var(--hsd-line); border-radius:8px; margin-top:14px; padding:16px 18px;}
  .hsd .catres h3{font-size:.95rem; color:var(--hsd-main);}
  .hsd .bar{background:#e6eeec; border-radius:5px; height:12px; margin:8px 0;}
  .hsd .bar i{display:block; height:12px; border-radius:5px; background:var(--hsd-main2);}
  .hsd .catres p{font-size:.88rem;}
  .hsd .catres .flag{font-weight:700;}
  .hsd .flag.ok{color:var(--hsd-ok);} .hsd .flag.mid{color:var(--hsd-mid);} .hsd .flag.ng{color:var(--hsd-ng);}
  .hsd .hsdnote{background:#ecf2f1; border-radius:8px; padding:16px 18px; font-size:.8rem; margin-top:20px; color:#4a515a;}
  .hsd .hsdcta{background:var(--hsd-card); border:1px solid var(--hsd-line); border-radius:8px; padding:18px; font-size:.9rem; margin-top:14px; text-align:center;}
  @media(max-width:480px){ .hsd .opts label{flex:1 1 100%;} }""",
        body="""<div class="hsd">
<div class="wrap">

  <div class="head">
    <h1>職場のハラスメント対策 総合診断</h1>
    <p>職場のハラスメント対策は、法律上の義務です。セクハラ（男女雇用機会均等法11条）、妊娠・出産・育児休業等に関するハラスメント（同法15条・育児介護休業法25条）、パワハラ（労働施策総合推進法31条）に加え、2026年（令和8年）10月1日からは、カスタマーハラスメント（同法33条）と、就職活動中の学生等に対するセクハラ（均等法13条）についても、雇用管理上の措置が全ての事業主に義務付けられています。<br>
    厚生労働省の6つの指針に共通する措置の枠組みをもとに、貴社のハラスメント対策の全体像を16問でセルフチェックできます。</p>
  </div>

  <div class="hsdlead">
    <strong>使い方</strong>：各設問について、現在の自社の状況に最も近いものを選んでください。所要時間は3〜4分程度です。<br>
    特に断りのない設問は、パワハラ・セクハラ・マタハラ等の各ハラスメントに共通して義務とされている措置です。「一部のハラスメントについてはできているが、他はできていない」という場合は「一部できている」を選んでください。<br><br>
    <strong>「一部できている」とは</strong>：取組はあるものの不十分な状態を指します。例えば、
    実際の運用はあるが文書・ルールになっていない／ルールはあるが従業員に周知されていない／
    一部のハラスメント類型・部署・従業員にとどまっている、といった場合です。
  </div>

  <form id="hsdForm">

  <div class="hsdcat">
    <h2>１　会社の方針の明確化と周知・啓発</h2>
    <div class="q"><div class="qt"><span class="num">Q1</span>パワハラ・セクハラ・妊娠出産・育児介護等に関するハラスメントを行ってはならないという会社の方針と、各ハラスメントの内容を、文書（就業規則・社内報・イントラネット等）で明確にし、管理職を含む従業員に周知している。</div>
      <div class="opts" data-q="1"></div></div>
    <div class="q"><div class="qt"><span class="num">Q2</span>ハラスメントの行為者には厳正に対処する旨の方針と対処の内容を、就業規則等の服務規律・懲戒規定に定め、従業員に周知している。</div>
      <div class="opts" data-q="2"></div></div>
    <div class="q"><div class="qt"><span class="num">Q3</span>妊娠・出産や、育児休業・介護休業等の制度を利用することについて、否定的な言動（「休まれると迷惑」など）をしないよう、方針の周知・啓発を行っている。</div>
      <div class="opts" data-q="3"></div></div>
    <div class="q"><div class="qt"><span class="num">Q4</span>ハラスメント防止に関する研修・講習等を実施している（管理職向けを含む）。</div>
      <div class="opts" data-q="4"></div></div>
  </div>

  <div class="hsdcat">
    <h2>２　相談に対応する体制の整備</h2>
    <div class="q"><div class="qt"><span class="num">Q5</span>ハラスメントの相談窓口（担当者を決める・相談制度を設ける・外部委託のいずれでも可）をあらかじめ定め、従業員に周知している。</div>
      <div class="opts" data-q="5"></div></div>
    <div class="q"><div class="qt"><span class="num">Q6</span>窓口の担当者が適切に対応できる仕組みがある（対応の留意点をまとめたマニュアル、担当者向け研修、人事部門等と連携する仕組みなど）。</div>
      <div class="opts" data-q="6"></div></div>
    <div class="q"><div class="qt"><span class="num">Q7</span>ハラスメントに当たるかどうか微妙なケースや、発生の「おそれ」の段階でも幅広く相談を受け付け、パワハラ・セクハラ等の複数の類型にまたがる相談にも一元的に対応できる体制にしている。</div>
      <div class="opts" data-q="7"></div></div>
  </div>

  <div class="hsdcat">
    <h2>３　発生後の迅速・適切な対応</h2>
    <div class="q"><div class="qt"><span class="num">Q8</span>相談があった場合に、事実関係を迅速かつ正確に確認する手順がある（相談者・行為者とされる者の双方や第三者からの聴取など）。</div>
      <div class="opts" data-q="8"></div></div>
    <div class="q"><div class="qt"><span class="num">Q9</span>ハラスメントの事実が確認できた場合に、被害を受けた従業員への配慮の措置（配置転換などの引き離し、労働条件上の不利益の回復、メンタルヘルス不調への相談対応など）を速やかに行うことにしている。</div>
      <div class="opts" data-q="9"></div></div>
    <div class="q"><div class="qt"><span class="num">Q10</span>ハラスメントの事実が確認できた場合に、就業規則等に基づき、行為者に対する措置（懲戒、配置転換、注意・指導など）を適正に行うことにしている。</div>
      <div class="opts" data-q="10"></div></div>
    <div class="q"><div class="qt"><span class="num">Q11</span>事実が確認できた場合も確認できなかった場合も、方針の再周知や研修など、再発防止に向けた措置をとることにしている。</div>
      <div class="opts" data-q="11"></div></div>
  </div>

  <div class="hsdcat">
    <h2>４　あわせて必要な措置</h2>
    <div class="q"><div class="qt"><span class="num">Q12</span>相談者・行為者等のプライバシーを保護するための措置（マニュアルへの明記、担当者研修など）を講じ、保護されることを従業員に周知している。</div>
      <div class="opts" data-q="12"></div></div>
    <div class="q"><div class="qt"><span class="num">Q13</span>ハラスメントの相談をしたことや、事実確認に協力したこと等を理由に、解雇その他の不利益な取扱いをしない旨を文書で定め、従業員に周知している。</div>
      <div class="opts" data-q="13"></div></div>
  </div>

  <div class="hsdcat">
    <h2>５　類型ごとに特に求められる措置<small>2026年10月施行の新しい義務を含む</small></h2>
    <div class="q"><div class="qt"><span class="num">Q14</span>妊娠・出産・育児・介護に関するハラスメントの原因や背景を解消するため、業務体制の整備（妊娠した従業員や制度利用者の業務の分担見直し・代替要員の確保など）の措置をとっている。</div>
      <div class="opts" data-q="14"></div></div>
    <div class="q"><div class="qt"><span class="num">Q15</span>就職活動中の学生やインターンシップ参加者等に対するセクハラの防止についても、方針の明確化や相談対応の体制をとっている（2026年10月1日から義務化）。</div>
      <div class="opts" data-q="15"></div></div>
    <div class="q"><div class="qt"><span class="num">Q16</span>顧客や取引先からの著しい迷惑行為（カスタマーハラスメント）から従業員を守るための措置（方針の明確化、相談体制、発生時の対応手順など）をとっている（2026年10月1日から義務化）。</div>
      <div class="opts" data-q="16"></div></div>
  </div>

  <div class="btnrow">
    <button type="button" class="go" onclick="hsdScore()">診断結果を見る</button>
    <p class="warn" id="hsdWarn">未回答の設問があります。すべての設問にお答えください。</p>
  </div>
  </form>

  <div id="hsdResult">
    <div class="score">
      <div style="font-size:.9rem;">ハラスメント対策（措置義務）の充足度</div>
      <div class="pct" id="hsdPct"></div>
      <div class="lvl" id="hsdLvl"></div>
      <div class="msg" id="hsdMsg"></div>
    </div>
    <div id="hsdCats"></div>

    <!-- ▼お問い合わせ導線（設置時にリンク先・文言を編集してください）▼ -->
    <div class="hsdcta">
      ハラスメント防止体制の整備（防止規程・就業規則の整備、相談窓口の設計、研修、発生時の調査対応等）に関するご相談は、<a href="#contact" style="color:var(--hsd-main); font-weight:700;">下のお問い合わせ欄</a>のメールアドレスまでご連絡ください。
    </div>
    <!-- ▲お問い合わせ導線▲ -->
  </div>

  <div class="hsdnote">
    <strong>ご利用上の注意</strong><br>
    ・本診断は、労働施策総合推進法31条・33条、男女雇用機会均等法11条・13条・15条、育児介護休業法25条と、これらに基づく厚生労働省の各指針（パワハラ指針＝令和2年厚生労働省告示第5号、カスハラ指針＝令和8年厚生労働省告示第51号、セクハラ指針＝平成18年厚生労働省告示第615号、求職者等セクハラ指針＝令和8年厚生労働省告示第52号、マタハラ指針＝平成28年厚生労働省告示第312号、育児介護ハラスメント関係＝平成21年厚生労働省告示第509号）の内容をもとにした、一般的な情報提供です。個別の事案に関する法的助言ではありません。<br>
    ・診断結果はあくまで目安であり、実際に措置義務を満たしているかどうかは、個別の状況に応じて判断されます。<br>
    ・派遣労働者については、派遣元・派遣先の双方が措置義務を負います。<br>
    ・入力内容がサーバーに送信されることはありません（お使いのブラウザ内でのみ処理されます）。
  </div>

</div>
</div>
<a class="back" href="../shindan.html">← 診断ツール一覧に戻る</a>""",
        js="""(function(){
  var opts=[["できている",2],["一部できている",1],["できていない",0]];
  document.querySelectorAll('.hsd .opts').forEach(function(box){
    var q=box.getAttribute('data-q');
    opts.forEach(function(o){
      var l=document.createElement('label');
      l.innerHTML='<input type="radio" name="hq'+q+'" value="'+o[1]+'"><span>'+o[0]+'</span>';
      box.appendChild(l);
    });
  });
})();

var hsdCatDef=[
  {name:"１ 方針の明確化と周知・啓発", qs:[1,2,3,4],
   advice:"ハラスメントを行ってはならない旨の方針と行為者への厳正対処方針（懲戒規定）の明文化・周知は、全てのハラスメント類型に共通する措置義務の出発点です。就業規則・防止規程の整備と、管理職を含む研修から着手することが考えられます。妊娠・出産や育児介護の制度利用への否定的な言動を防ぐ周知・啓発も義務の内容に含まれます。"},
  {name:"２ 相談体制の整備", qs:[5,6,7],
   advice:"相談窓口の設置と周知は措置義務の中核です。窓口は各ハラスメント共通で一元的に対応できる体制が望ましいとされています。担当者向けのマニュアル・研修、該当するか微妙な段階でも広く受け付ける運用の整備が求められます。"},
  {name:"３ 発生後の迅速・適切な対応", qs:[8,9,10,11],
   advice:"事実確認の手順、被害を受けた従業員への配慮措置、行為者への措置、再発防止措置をあらかじめ決めておくことが求められます。発生時に場当たりで対応する状態は、措置義務の観点からも、安全配慮義務や懲戒処分の有効性の観点からもリスクがあります。"},
  {name:"４ プライバシー保護・不利益取扱いの禁止", qs:[12,13],
   advice:"相談者・行為者等のプライバシー保護の措置と、相談等を理由とする不利益取扱いをしない旨の規定・周知が義務とされています。就業規則やハラスメント防止規程の見直しが必要になる部分です。"},
  {name:"５ 類型ごとに特に求められる措置", qs:[14,15,16],
   advice:"妊娠・出産・育児・介護に関するハラスメントでは、原因・背景を解消するための業務体制の整備が義務とされています。また、2026年10月1日からは、就職活動中の学生等へのセクハラ防止と、カスタマーハラスメントへの対応も措置義務の対象です。従来のハラスメント規程のままでは、この2つの新しい義務をカバーできていないことが多いため、規程・体制の見直しをおすすめします。"}
];

function hsdScore(){
  var warn=document.getElementById('hsdWarn');
  var vals={};
  for(var i=1;i<=16;i++){
    var el=document.querySelector('.hsd input[name="hq'+i+'"]:checked');
    if(!el){warn.style.display='block'; return;}
    vals[i]=parseInt(el.value,10);
  }
  warn.style.display='none';

  var got=0, max=0;
  for(var i=1;i<=16;i++){got+=vals[i]; max+=2;}
  var pct=Math.round(got/max*100);

  var lvlEl=document.getElementById('hsdLvl'), msgEl=document.getElementById('hsdMsg');
  document.getElementById('hsdPct').textContent=pct+'%';
  if(pct>=90){
    lvlEl.textContent='おおむね整備されています'; lvlEl.className='lvl ok';
    msgEl.textContent='義務とされている措置はおおむね整備されている状態です。運用が形骸化していないか（窓口の周知度、研修の実施状況、規程と実際の対応の一致など）の定期的な点検と、下記で「一部」にとどまった項目の底上げを検討するとよいでしょう。';
  }else if(pct>=60){
    lvlEl.textContent='一部に不足があります'; lvlEl.className='lvl mid';
    msgEl.textContent='基本的な取組はあるものの、措置義務の観点からは不足している項目があります。特に、2026年10月から義務化されたカスタマーハラスメント対応と就職活動中の学生等へのセクハラ防止は、従来の規程ではカバーされていないことが多い部分です。下記の項目別の結果を参考に、不足部分の整備を進めることをおすすめします。';
  }else{
    lvlEl.textContent='体制の整備が必要な状態です'; lvlEl.className='lvl ng';
    msgEl.textContent='義務とされている措置の多くが未整備の状態です。これらの措置義務に対応していない場合、行政による助言・指導・勧告の対象となり得るほか、勧告に従わない場合には企業名が公表されることがあります（労働施策総合推進法42条、男女雇用機会均等法35条・36条、育児介護休業法56条・56条の2）。また、ハラスメントが実際に発生した場合には、会社が損害賠償責任を問われるおそれもあります。方針の明文化と相談窓口の設置から、早めに整備に着手することをおすすめします。';
  }

  var html='';
  hsdCatDef.forEach(function(c){
    var g=0, m=c.qs.length*2;
    c.qs.forEach(function(q){g+=vals[q];});
    var p=Math.round(g/m*100);
    var flag, cls;
    if(p>=90){flag='○ 整備されています'; cls='ok';}
    else if(p>=50){flag='△ 一部に不足があります'; cls='mid';}
    else {flag='× 整備が必要です'; cls='ng';}
    html+='<div class="catres"><h3>'+c.name+'</h3>'
        +'<div class="bar"><i style="width:'+p+'%"></i></div>'
        +'<p><span class="flag '+cls+'">'+flag+'</span></p>'
        +(p<90?'<p>'+c.advice+'</p>':'')
        +'</div>';
  });
  document.getElementById('hsdCats').innerHTML=html;
  var r=document.getElementById('hsdResult');
  r.style.display='block';
  r.scrollIntoView({behavior:'smooth'});
}""",
    ),
    dict(
        slug="""koueki""",
        pfx="""ktd""",
        title="""公益通報対応体制 簡易診断""",
        desc="""2026年12月1日施行の改正公益通報者保護法に対応。従事者の指定、内部規程、通報を理由とする不利益取扱いの禁止、通報妨害の禁止などを13問でセルフチェックできます。入力内容は送信されません。""",
        summary="""従事者の指定、受付・調査・是正の体制、通報者の保護、改正法（2026年12月1日施行）で新設された通報妨害の禁止までを13問でチェックします。""",
        tag="""13問 ／ 5分""",
        css="""  .ktd{
    --ktd-navy:#274a2e; --ktd-navy2:#38653f; --ktd-bg:#f5f8f5; --ktd-card:#ffffff;
    --ktd-ok:#2e7d52; --ktd-mid:#b07820; --ktd-ng:#b03a3a; --ktd-line:#dce6dc;
  }
  .ktd *{box-sizing:border-box; margin:0; padding:0;}
  .ktd{font-family:"Hiragino Kaku Gothic ProN","Hiragino Sans","Yu Gothic","Meiryo",sans-serif;
       background:var(--ktd-bg); color:#2a2f36; line-height:1.75; padding:24px 12px; border-radius:8px;}
  .ktd .wrap{max-width:760px; margin:0 auto;}
  .ktd .head{background:var(--ktd-navy); color:#fff; border-radius:10px 10px 0 0; padding:26px 24px;}
  .ktd .head h1{font-size:1.35rem; line-height:1.5;}
  .ktd .head p{font-size:.86rem; margin-top:10px; opacity:.92;}
  .ktd .ktdlead{background:var(--ktd-card); border:1px solid var(--ktd-line); border-top:none; padding:20px 24px; font-size:.92rem;}
  .ktd .ktdlead strong{color:var(--ktd-navy);}
  .ktd .ktdcat{background:var(--ktd-card); border:1px solid var(--ktd-line); border-radius:8px; margin-top:18px; overflow:hidden;}
  .ktd .ktdcat h2{background:var(--ktd-navy2); color:#fff; font-size:1rem; padding:10px 18px;}
  .ktd .ktdcat h2 small{font-weight:normal; font-size:.78rem; opacity:.9; margin-left:8px;}
  .ktd .q{padding:16px 18px; border-top:1px solid var(--ktd-line);}
  .ktd .q:first-of-type{border-top:none;}
  .ktd .q .qt{font-size:.95rem; font-weight:600; margin-bottom:10px;}
  .ktd .q .qt .num{display:inline-block; background:var(--ktd-navy); color:#fff; border-radius:4px;
       font-size:.78rem; padding:1px 8px; margin-right:8px; vertical-align:2px;}
  .ktd .opts{display:flex; gap:8px; flex-wrap:wrap;}
  .ktd .opts label{flex:1 1 30%; min-width:110px; text-align:center; border:1.5px solid var(--ktd-line);
       border-radius:6px; padding:8px 6px; font-size:.88rem; cursor:pointer; background:#fafdfa; user-select:none;}
  .ktd .opts input{display:none;}
  .ktd .opts input:checked + span{display:block; margin:-8px -6px; padding:8px 6px; border-radius:4.5px;
       background:var(--ktd-navy); color:#fff; font-weight:600;}
  .ktd .btnrow{text-align:center; margin:26px 0 8px;}
  .ktd button.go{background:var(--ktd-navy); color:#fff; border:none; border-radius:8px;
       font-size:1.05rem; font-weight:700; padding:14px 52px; cursor:pointer;}
  .ktd button.go:hover{background:var(--ktd-navy2);}
  .ktd .warn{display:none; text-align:center; color:var(--ktd-ng); font-size:.88rem; margin-top:8px;}
  .ktd #ktdResult{display:none; margin-top:24px;}
  .ktd .score{background:var(--ktd-card); border:2px solid var(--ktd-navy); border-radius:10px; padding:22px 24px; text-align:center;}
  .ktd .score .pct{font-size:2.6rem; font-weight:800; color:var(--ktd-navy);}
  .ktd .score .lvl{font-size:1.1rem; font-weight:700; margin-top:4px;}
  .ktd .score .lvl.ok{color:var(--ktd-ok);} .ktd .score .lvl.mid{color:var(--ktd-mid);} .ktd .score .lvl.ng{color:var(--ktd-ng);}
  .ktd .score .msg{font-size:.9rem; margin-top:10px; text-align:left;}
  .ktd .catres{background:var(--ktd-card); border:1px solid var(--ktd-line); border-radius:8px; margin-top:14px; padding:16px 18px;}
  .ktd .catres h3{font-size:.95rem; color:var(--ktd-navy);}
  .ktd .bar{background:#e8f0e8; border-radius:5px; height:12px; margin:8px 0;}
  .ktd .bar i{display:block; height:12px; border-radius:5px; background:var(--ktd-navy2);}
  .ktd .catres p{font-size:.88rem;}
  .ktd .catres .flag{font-weight:700;}
  .ktd .flag.ok{color:var(--ktd-ok);} .ktd .flag.mid{color:var(--ktd-mid);} .ktd .flag.ng{color:var(--ktd-ng);}
  .ktd .ktdnote{background:#edf3ed; border-radius:8px; padding:16px 18px; font-size:.8rem; margin-top:20px; color:#4a514a;}
  .ktd .ktdcta{background:var(--ktd-card); border:1px solid var(--ktd-line); border-radius:8px; padding:18px; font-size:.9rem; margin-top:14px; text-align:center;}
  .ktd .sizebox{background:var(--ktd-card); border:1px solid var(--ktd-line); border-radius:8px; margin-top:18px; padding:16px 18px;}
  .ktd .sizebox .qt{font-size:.95rem; font-weight:600; margin-bottom:10px;}
  @media(max-width:480px){ .ktd .opts label{flex:1 1 100%;} }""",
        body="""<div class="ktd">
<div class="wrap">

  <div class="head">
    <h1>公益通報対応体制 簡易診断</h1>
    <p>改正公益通報者保護法（令和7年法律第62号）が<strong>2026年（令和8年）12月1日に施行</strong>されます。<br>
    通報を理由とする解雇・懲戒には担当者個人への刑事罰が新設され、退職合意書の「通報しない」条項は無効になるなど、全ての企業に影響する改正です。<br>
    改正法と、法律に基づいて内閣総理大臣が定める指針（法定指針）の内容をもとに、貴社の対応状況を13問でセルフチェックできます。</p>
  </div>

  <div class="ktdlead">
    <strong>使い方</strong>：各設問について、現在の自社の状況に最も近いものを選んでください。所要時間は3分程度です。<br><br>
    <strong>「一部できている」とは</strong>：取組はあるものの不十分な状態を指します。例えば、
    実際の運用はあるが文書・ルールになっていない／規程はあるが周知されていない／
    一部の対象者・部署にとどまっている、といった場合です。
  </div>

  <form id="ktdForm">

  <div class="sizebox">
    <div class="qt">まず、貴社の常時使用する労働者数を選んでください。</div>
    <div class="opts" id="ktdSize">
      <label><input type="radio" name="qsize" value="big"><span>301人以上</span></label>
      <label><input type="radio" name="qsize" value="small"><span>300人以下</span></label>
    </div>
    <p style="font-size:.8rem; margin-top:8px; color:#4a514a;">※内部通報体制の整備は、301人以上の企業では法律上の義務、300人以下の企業では努力義務です。ただし、通報者への不利益取扱いの禁止・通報妨害の禁止などは企業規模を問わず適用されます。</p>
  </div>

  <div class="ktdcat">
    <h2>１　通報窓口・従事者・周知<small>法11条1項・2項</small></h2>
    <div class="q"><div class="qt"><span class="num">Q1</span>内部通報の受付窓口を設け、受付・調査・是正までの対応体制を定めている。</div>
      <div class="opts" data-q="1"></div></div>
    <div class="q"><div class="qt"><span class="num">Q2</span>通報対応業務に従事する担当者（従事者）を書面で指定し、指定された本人にもその旨を伝えている。</div>
      <div class="opts" data-q="2"></div></div>
    <div class="q"><div class="qt"><span class="num">Q3</span>窓口の連絡先や通報者が保護される仕組みを、従業員だけでなく、退職者（退職後1年以内）や業務委託先のフリーランスにも分かる形で周知している。</div>
      <div class="opts" data-q="3"></div></div>
  </div>

  <div class="ktdcat">
    <h2>２　独立性・利益相反の排除<small>法定指針</small></h2>
    <div class="q"><div class="qt"><span class="num">Q4</span>経営幹部が関与する事案でも機能するよう、経営幹部から独立した通報ルート（社外窓口・監査役等への通報経路など）を確保している。</div>
      <div class="opts" data-q="4"></div></div>
    <div class="q"><div class="qt"><span class="num">Q5</span>通報事案の関係者（通報で名指しされた人やその部下など）を、その事案の通報対応業務から外す仕組みがある。</div>
      <div class="opts" data-q="5"></div></div>
  </div>

  <div class="ktdcat">
    <h2>３　通報者の保護<small>法3条・11条の2・11条の3</small></h2>
    <div class="q"><div class="qt"><span class="num">Q6</span>通報者が誰かという情報を必要最小限の範囲でしか共有しないルールがあり、通報者が誰かを探す行為（通報者の探索）を防ぐ措置をとっている。</div>
      <div class="opts" data-q="6"></div></div>
    <div class="q"><div class="qt"><span class="num">Q7</span>通報したことを理由とする解雇・懲戒・配転・嫌がらせ等の不利益な取扱いを禁止するルールを定め、通報後の通報者の状況をフォローする運用がある。</div>
      <div class="opts" data-q="7"></div></div>
    <div class="q"><div class="qt"><span class="num">Q8</span>退職合意書・誓約書などの社内ひな形に「通報・申告をしない」といった条項が入っていないかを点検した（改正法では、正当な理由なく公益通報を妨げる行為は禁止され、これに違反してされた合意は無効とされます）。</div>
      <div class="opts" data-q="8"></div></div>
  </div>

  <div class="ktdcat">
    <h2>４　改正対応と日常の運用<small>改正法・法定指針</small></h2>
    <div class="q"><div class="qt"><span class="num">Q9</span>業務委託先のフリーランス（業務委託の終了後1年以内の人を含む）からの通報も受け付ける運用に見直した。</div>
      <div class="opts" data-q="9"></div></div>
    <div class="q"><div class="qt"><span class="num">Q10</span>解雇や懲戒を行う前に、対象者による通報の有無や、処分の決定者がそれを知っていたかを確認し、記録を残すプロセスがある（通報から1年以内の解雇・懲戒は、通報を理由とするものと推定されます）。</div>
      <div class="opts" data-q="10"></div></div>
    <div class="q"><div class="qt"><span class="num">Q11</span>内部通報に関する社内規程を、法定指針の内容（従事者の定め、独立性の確保、範囲外共有の防止、不利益取扱いの防止など）に沿って整備している。</div>
      <div class="opts" data-q="11"></div></div>
    <div class="q"><div class="qt"><span class="num">Q12</span>通報対応の記録を適切に保管し、従業員への教育・研修や、運用実績の概要の開示を行っている。</div>
      <div class="opts" data-q="12"></div></div>
    <div class="q"><div class="qt"><span class="num">Q13</span>通報者に対して、調査結果や是正の結果を適切に通知する運用がある。</div>
      <div class="opts" data-q="13"></div></div>
  </div>

  <div class="btnrow">
    <button type="button" class="go" onclick="ktdScore()">診断結果を見る</button>
    <p class="warn" id="ktdWarn">未回答の設問があります。従業員数とすべての設問にお答えください。</p>
  </div>
  </form>

  <div id="ktdResult">
    <div class="score">
      <div style="font-size:.9rem;">公益通報対応体制（Q1〜Q13）の充足度</div>
      <div class="pct" id="ktdPct"></div>
      <div class="lvl" id="ktdLvl"></div>
      <div class="msg" id="ktdMsg"></div>
    </div>
    <div id="ktdCats"></div>

    <!-- ▼お問い合わせ導線（設置時にリンク先・文言を編集してください）▼ -->
    <div class="ktdcta">
      内部通報体制の整備（社内規程・退職合意書ひな形の見直し、従事者指定、研修等）に関するご相談は、<a href="#contact" style="color:var(--ktd-navy); font-weight:700;">下のお問い合わせ欄</a>のメールアドレスまでご連絡ください。
    </div>
    <!-- ▲お問い合わせ導線▲ -->
  </div>

  <div class="ktdnote">
    <strong>ご利用上の注意</strong><br>
    ・本診断は、公益通報者保護法（令和7年法律第62号による改正後のもの）および同法11条4項に基づき内閣総理大臣が定める指針（法定指針）の内容をもとにした、一般的な情報提供です。個別の事案に関する法的助言ではありません。<br>
    ・診断結果はあくまで目安であり、実際に法律上の義務を満たしているかどうかは、個別の状況に応じて判断されます。<br>
    ・入力内容がサーバーに送信されることはありません（お使いのブラウザ内でのみ処理されます）。
  </div>

</div>
</div>
<a class="back" href="../shindan.html">← 診断ツール一覧に戻る</a>""",
        js="""(function(){
  var opts=[["できている",2],["一部できている",1],["できていない",0]];
  document.querySelectorAll('.ktd .opts[data-q]').forEach(function(box){
    var q=box.getAttribute('data-q');
    opts.forEach(function(o){
      var l=document.createElement('label');
      l.innerHTML='<input type="radio" name="q'+q+'" value="'+o[1]+'"><span>'+o[0]+'</span>';
      box.appendChild(l);
    });
  });
})();

var ktdCatDef=[
  {name:"１ 通報窓口・従事者・周知", qs:[1,2,3],
   advice:"窓口の設置と従事者の書面による指定、対象者への周知が体制整備の出発点です。改正法では、体制を労働者等に周知することが条文上も明確にされました。窓口を置いただけで周知が不十分な状態では足りないとされています。"},
  {name:"２ 独立性・利益相反の排除", qs:[4,5],
   advice:"経営幹部が関わる事案で通報がにぎりつぶされない仕組み（社外窓口や監査役等への経路）と、事案関係者を対応から外すルールは、法定指針が求める体制の中核です。"},
  {name:"３ 通報者の保護", qs:[6,7,8],
   advice:"改正法では、通報者を特定しようとする行為（通報者の探索）や通報の妨害が明文で禁止され、「通報しない」旨の合意は無効とされました。退職合意書・誓約書のひな形の点検は、施行までに必ず行っておきたい項目です。"},
  {name:"４ 改正対応と日常の運用", qs:[9,10,11,12,13],
   advice:"フリーランスへの対象拡大、通報から1年以内の解雇・懲戒を通報理由と推定する規定など、改正への対応は日常の人事プロセスの見直しが必要です。特に、解雇・懲戒の前に通報の有無を確認して記録する運用は、推定規定への備えとして重要です。"}
];

function ktdScore(){
  var warn=document.getElementById('ktdWarn');
  var size=document.querySelector('.ktd input[name="qsize"]:checked');
  var vals={};
  var ok=true;
  if(!size) ok=false;
  for(var i=1;i<=13;i++){
    var el=document.querySelector('.ktd input[name="q'+i+'"]:checked');
    if(!el){ok=false; break;}
    vals[i]=parseInt(el.value,10);
  }
  if(!ok){warn.style.display='block'; return;}
  warn.style.display='none';

  var got=0, max=26;
  for(var i=1;i<=13;i++){got+=vals[i];}
  var pct=Math.round(got/max*100);
  var big = size.value==='big';

  var lvlEl=document.getElementById('ktdLvl'), msgEl=document.getElementById('ktdMsg');
  document.getElementById('ktdPct').textContent=pct+'%';

  var sizeNote = big
    ? '貴社の規模（301人以上）では、内部通報体制の整備と従事者の指定は法律上の義務であり、改正法では、違反に対する行政措置（助言・指導、勧告、従事者を指定する義務については勧告に従わない場合の命令と、命令をした場合の公表）や、報告徴収・立入検査の権限、罰則が強化されています。'
    : '貴社の規模（300人以下）では体制整備は努力義務ですが、通報者への不利益取扱いの禁止、通報妨害の禁止と「通報しない」合意の無効、通報者探索の禁止、担当者個人への刑事罰は、企業規模を問わず適用されます。';

  if(pct>=90){
    lvlEl.textContent='おおむね整備されています'; lvlEl.className='lvl ok';
    msgEl.textContent='改正法が求める水準をおおむね満たしている状態です。'+sizeNote+'「一部」にとどまった項目の底上げと、施行後の運用状況の点検を続けるとよいでしょう。';
  }else if(pct>=60){
    lvlEl.textContent='一部に不足があります'; lvlEl.className='lvl mid';
    msgEl.textContent='基本的な体制はあるものの、改正法への対応として不足している項目があります。'+sizeNote+'施行は2026年12月1日です。下記の項目別の結果を参考に、不足部分の整備を進めることをおすすめします。';
  }else{
    lvlEl.textContent='体制の整備が必要な状態です'; lvlEl.className='lvl ng';
    msgEl.textContent='改正法が求める体制の多くが未整備の状態です。'+sizeNote+'特に、通報を理由とする解雇・懲戒には、処分を決めた個人に6月以下の拘禁刑または30万円以下の罰金、法人に3000万円以下の罰金（両罰規定）が新設されており、通報から1年以内の解雇・懲戒は通報を理由とするものと推定されます。施行（2026年12月1日）に向けて、早急な整備をおすすめします。';
  }

  var html='';
  ktdCatDef.forEach(function(c){
    var cgot=0, cmax=c.qs.length*2;
    c.qs.forEach(function(q){cgot+=vals[q];});
    var p=Math.round(cgot/cmax*100);
    var flag, cls;
    if(p>=90){flag='○ 整備されています'; cls='ok';}
    else if(p>=50){flag='△ 一部に不足があります'; cls='mid';}
    else {flag='× 整備が必要です'; cls='ng';}
    html+='<div class="catres"><h3>'+c.name+'</h3>'
        +'<div class="bar"><i style="width:'+p+'%"></i></div>'
        +'<p><span class="flag '+cls+'">'+flag+'</span></p>'
        +(p<90?'<p>'+c.advice+'</p>':'')
        +'</div>';
  });
  document.getElementById('ktdCats').innerHTML=html;
  var r=document.getElementById('ktdResult');
  r.style.display='block';
  r.scrollIntoView({behavior:'smooth'});
}""",
    ),
    dict(
        slug="""kasuhara""",
        pfx="""ksd""",
        title="""カスタマーハラスメント対応体制 簡易診断""",
        desc="""2026年10月1日施行の改正労働施策総合推進法33条で、カスタマーハラスメントへの雇用管理上の措置が全ての事業主に義務付けられました。方針の明確化、相談対応体制、現場対応の手順などを15問でセルフチェックできます。入力内容は送信されません。""",
        summary="""方針の明確化と周知、相談対応体制、現場で対応する従業員への支援、記録と再発防止までを15問でチェックします。取引の相手方（企業間取引）からの言動も対象です。""",
        tag="""15問 ／ 5分""",
        css="""  .ksd{
    --ksd-navy:#1f3a5f; --ksd-navy2:#2d5280; --ksd-bg:#f5f7fa; --ksd-card:#ffffff;
    --ksd-ok:#2e7d52; --ksd-mid:#b07820; --ksd-ng:#b03a3a; --ksd-line:#dde4ec;
  }
  .ksd *{box-sizing:border-box; margin:0; padding:0;}
  .ksd{font-family:"Hiragino Kaku Gothic ProN","Hiragino Sans","Yu Gothic","Meiryo",sans-serif;
       background:var(--ksd-bg); color:#2a2f36; line-height:1.75; padding:24px 12px; border-radius:8px;}
  .ksd .wrap{max-width:760px; margin:0 auto;}
  .ksd .head{background:var(--ksd-navy); color:#fff; border-radius:10px 10px 0 0; padding:26px 24px;}
  .ksd .head h1{font-size:1.35rem; line-height:1.5;}
  .ksd .head p{font-size:.86rem; margin-top:10px; opacity:.92;}
  .ksd .ksdlead{background:var(--ksd-card); border:1px solid var(--ksd-line); border-top:none; padding:20px 24px; font-size:.92rem;}
  .ksd .ksdlead strong{color:var(--ksd-navy);}
  .ksd .ksdcat{background:var(--ksd-card); border:1px solid var(--ksd-line); border-radius:8px; margin-top:18px; overflow:hidden;}
  .ksd .ksdcat h2{background:var(--ksd-navy2); color:#fff; font-size:1rem; padding:10px 18px;}
  .ksd .ksdcat h2 small{font-weight:normal; font-size:.78rem; opacity:.9; margin-left:8px;}
  .ksd .q{padding:16px 18px; border-top:1px solid var(--ksd-line);}
  .ksd .q:first-of-type{border-top:none;}
  .ksd .q .qt{font-size:.95rem; font-weight:600; margin-bottom:10px;}
  .ksd .q .qt .num{display:inline-block; background:var(--ksd-navy); color:#fff; border-radius:4px;
       font-size:.78rem; padding:1px 8px; margin-right:8px; vertical-align:2px;}
  .ksd .opts{display:flex; gap:8px; flex-wrap:wrap;}
  .ksd .opts label{flex:1 1 30%; min-width:110px; text-align:center; border:1.5px solid var(--ksd-line);
       border-radius:6px; padding:8px 6px; font-size:.88rem; cursor:pointer; background:#fafbfd; user-select:none;}
  .ksd .opts input{display:none;}
  .ksd .opts input:checked + span{display:block; margin:-8px -6px; padding:8px 6px; border-radius:4.5px;
       background:var(--ksd-navy); color:#fff; font-weight:600;}
  .ksd .btnrow{text-align:center; margin:26px 0 8px;}
  .ksd button.go{background:var(--ksd-navy); color:#fff; border:none; border-radius:8px;
       font-size:1.05rem; font-weight:700; padding:14px 52px; cursor:pointer;}
  .ksd button.go:hover{background:var(--ksd-navy2);}
  .ksd .warn{display:none; text-align:center; color:var(--ksd-ng); font-size:.88rem; margin-top:8px;}
  .ksd #ksdResult{display:none; margin-top:24px;}
  .ksd .score{background:var(--ksd-card); border:2px solid var(--ksd-navy); border-radius:10px; padding:22px 24px; text-align:center;}
  .ksd .score .pct{font-size:2.6rem; font-weight:800; color:var(--ksd-navy);}
  .ksd .score .lvl{font-size:1.1rem; font-weight:700; margin-top:4px;}
  .ksd .score .lvl.ok{color:var(--ksd-ok);} .ksd .score .lvl.mid{color:var(--ksd-mid);} .ksd .score .lvl.ng{color:var(--ksd-ng);}
  .ksd .score .msg{font-size:.9rem; margin-top:10px; text-align:left;}
  .ksd .catres{background:var(--ksd-card); border:1px solid var(--ksd-line); border-radius:8px; margin-top:14px; padding:16px 18px;}
  .ksd .catres h3{font-size:.95rem; color:var(--ksd-navy);}
  .ksd .bar{background:#e8edf3; border-radius:5px; height:12px; margin:8px 0;}
  .ksd .bar i{display:block; height:12px; border-radius:5px; background:var(--ksd-navy2);}
  .ksd .catres p{font-size:.88rem;}
  .ksd .catres .flag{font-weight:700;}
  .ksd .flag.ok{color:var(--ksd-ok);} .ksd .flag.mid{color:var(--ksd-mid);} .ksd .flag.ng{color:var(--ksd-ng);}
  .ksd .ksdnote{background:#eef2f7; border-radius:8px; padding:16px 18px; font-size:.8rem; margin-top:20px; color:#4a515a;}
  .ksd .ksdcta{background:var(--ksd-card); border:1px solid var(--ksd-line); border-radius:8px; padding:18px; font-size:.9rem; margin-top:14px; text-align:center;}
  @media(max-width:480px){ .ksd .opts label{flex:1 1 100%;} }""",
        body="""<div class="ksd">
<div class="wrap">

  <div class="head">
    <h1>カスハラ対応体制 簡易診断</h1>
    <p>2026年（令和8年）10月1日から、企業の規模を問わず、カスタマーハラスメント防止のための雇用管理上の措置が全ての事業主に義務付けられています（労働施策総合推進法33条）。<br>
    厚生労働省の指針（令和8年厚生労働省告示第51号）の内容をもとに、貴社の対応体制を15問でセルフチェックできます。</p>
  </div>

  <div class="ksdlead">
    <strong>使い方</strong>：各設問について、現在の自社の状況に最も近いものを選んでください。所要時間は3分程度です。<br>
    Q1〜Q13は指針で<strong>義務</strong>とされている措置、Q14・Q15は指針で望ましいとされている取組等です。<br><br>
    <strong>「一部できている」とは</strong>：取組はあるものの不十分な状態を指します。例えば、
    実際の運用はあるが文書・ルールになっていない／ルールはあるが従業員に周知されていない／
    一部の部署・店舗・従業員にとどまっている、といった場合です。
  </div>

  <form id="ksdForm">

  <div class="ksdcat">
    <h2>１　会社の方針の明確化と周知・啓発<small>指針4⑴</small></h2>
    <div class="q"><div class="qt"><span class="num">Q1</span>カスハラには毅然と対応し、従業員を保護するという会社の方針を文書（社内報・イントラネット・マニュアル等）で明確にし、管理職を含む従業員に周知している。</div>
      <div class="opts" data-q="1"></div></div>
    <div class="q"><div class="qt"><span class="num">Q2</span>カスハラが起きたときの対応手順（上司への報告、従業員を一人で対応させない、やり取りの録音・録画、警察への通報基準、本社・本部への情報共有など）をあらかじめ定め、従業員に周知している。</div>
      <div class="opts" data-q="2"></div></div>
    <div class="q"><div class="qt"><span class="num">Q3</span>会社の方針や対応手順について、研修・講習等を実施している。</div>
      <div class="opts" data-q="3"></div></div>
  </div>

  <div class="ksdcat">
    <h2>２　相談に対応する体制の整備<small>指針4⑵</small></h2>
    <div class="q"><div class="qt"><span class="num">Q4</span>カスハラの相談窓口（担当者を決める・相談制度を設ける・外部委託のいずれでも可）を定め、従業員に周知している。</div>
      <div class="opts" data-q="4"></div></div>
    <div class="q"><div class="qt"><span class="num">Q5</span>窓口の担当者が適切に対応できる仕組みがある（対応の留意点をまとめたマニュアル、担当者向け研修、関係部門と連携する仕組みなど）。</div>
      <div class="opts" data-q="5"></div></div>
    <div class="q"><div class="qt"><span class="num">Q6</span>カスハラに当たるかどうか微妙なケースや、発生の「おそれ」の段階でも、幅広く相談を受け付ける運用にしている。</div>
      <div class="opts" data-q="6"></div></div>
  </div>

  <div class="ksdcat">
    <h2>３　発生後の迅速・適切な対応<small>指針4⑶</small></h2>
    <div class="q"><div class="qt"><span class="num">Q7</span>相談があった場合に、事実関係を迅速かつ正確に確認する手順がある（本人や周囲の従業員からの聴取、録音・録画等の客観的な証拠の確認など）。</div>
      <div class="opts" data-q="7"></div></div>
    <div class="q"><div class="qt"><span class="num">Q8</span>被害を受けた従業員への配慮の措置を用意している（担当の交代や複数名での対応、行為者との引き離し、メンタルヘルス不調への相談対応など）。</div>
      <div class="opts" data-q="8"></div></div>
    <div class="q"><div class="qt"><span class="num">Q9</span>発生後には、方針の再周知や、原因・背景（商品・サービス・接客側の問題を含む）の分析と改善など、再発防止の措置をとることにしている。</div>
      <div class="opts" data-q="9"></div></div>
  </div>

  <div class="ksdcat">
    <h2>４　特に悪質なケースを抑止する措置<small>指針4⑷</small></h2>
    <div class="q"><div class="qt"><span class="num">Q10</span>過度な要求を繰り返すなど特に悪質なケースへの対処方針（警察への通報、警告文の発出、サービス提供の停止、店舗・施設への出入禁止、仮処分命令の申立てなど）をあらかじめ定め、従業員に周知している。</div>
      <div class="opts" data-q="10"></div></div>
    <div class="q"><div class="qt"><span class="num">Q11</span>その対処を実際に行える体制がある（関係部門間の連携、本社・法務部門・外部の専門家への相談ルートなど）。</div>
      <div class="opts" data-q="11"></div></div>
  </div>

  <div class="ksdcat">
    <h2>５　あわせて必要な措置<small>指針4⑸</small></h2>
    <div class="q"><div class="qt"><span class="num">Q12</span>相談者等のプライバシーを保護するための措置（マニュアルへの明記、担当者研修など）を講じ、保護されることを従業員に周知している。</div>
      <div class="opts" data-q="12"></div></div>
    <div class="q"><div class="qt"><span class="num">Q13</span>カスハラの相談をしたこと等を理由に解雇その他の不利益な取扱いをしない旨を、就業規則等の文書で定め、従業員に周知している。</div>
      <div class="opts" data-q="13"></div></div>
  </div>

  <div class="ksdcat">
    <h2>６　さらに望ましい取組<small>指針5・6・7</small></h2>
    <div class="q"><div class="qt"><span class="num">Q14</span>従業員の顧客対応力の向上（接客・苦情対応の研修等）や、顧客等への理解（消費者心理・障害特性等）を深めるための取組を行っている。</div>
      <div class="opts" data-q="14"></div></div>
    <div class="q"><div class="qt"><span class="num">Q15</span>自社の従業員が取引先の従業員に対して行う言動にも注意を払うよう周知し、取引先から事実確認等の協力を求められた場合に応じる体制を考えている。</div>
      <div class="opts" data-q="15"></div></div>
  </div>

  <div class="btnrow">
    <button type="button" class="go" onclick="ksdScore()">診断結果を見る</button>
    <p class="warn" id="ksdWarn">未回答の設問があります。すべての設問にお答えください。</p>
  </div>
  </form>

  <div id="ksdResult">
    <div class="score">
      <div style="font-size:.9rem;">義務とされている措置（Q1〜Q13）の充足度</div>
      <div class="pct" id="ksdPct"></div>
      <div class="lvl" id="ksdLvl"></div>
      <div class="msg" id="ksdMsg"></div>
    </div>
    <div id="ksdCats"></div>

    <!-- ▼お問い合わせ導線（設置時にリンク先・文言を編集してください）▼ -->
    <div class="ksdcta">
      カスタマーハラスメント対応体制の整備（基本方針・対応マニュアル・就業規則の整備、研修等）に関するご相談は、<a href="#contact" style="color:var(--ksd-navy); font-weight:700;">下のお問い合わせ欄</a>のメールアドレスまでご連絡ください。
    </div>
    <!-- ▲お問い合わせ導線▲ -->
  </div>

  <div class="ksdnote">
    <strong>ご利用上の注意</strong><br>
    ・本診断は、労働施策総合推進法33条および厚生労働省「事業主が職場における顧客等の言動に起因する問題に関して雇用管理上講ずべき措置等についての指針」（令和8年厚生労働省告示第51号）の内容をもとにした、一般的な情報提供です。個別の事案に関する法的助言ではありません。<br>
    ・診断結果はあくまで目安であり、実際に措置義務を満たしているかどうかは、個別の状況に応じて判断されます。<br>
    ・入力内容がサーバーに送信されることはありません（お使いのブラウザ内でのみ処理されます）。
  </div>

</div>
</div>
<a class="back" href="../shindan.html">← 診断ツール一覧に戻る</a>""",
        js="""(function(){
  var opts=[["できている",2],["一部できている",1],["できていない",0]];
  document.querySelectorAll('.ksd .opts').forEach(function(box){
    var q=box.getAttribute('data-q');
    opts.forEach(function(o){
      var l=document.createElement('label');
      l.innerHTML='<input type="radio" name="q'+q+'" value="'+o[1]+'"><span>'+o[0]+'</span>';
      box.appendChild(l);
    });
  });
})();

var ksdCatDef=[
  {name:"１ 方針の明確化と周知・啓発", qs:[1,2,3], duty:true,
   advice:"カスハラに毅然と対応し従業員を保護する方針の明文化と周知は、措置義務の出発点です。トップメッセージや社内マニュアルへの明記、対応手順（報告ルート・一人で対応させない・録音録画・警察への通報基準等）の整備から着手することが考えられます。"},
  {name:"２ 相談体制の整備", qs:[4,5,6], duty:true,
   advice:"相談窓口の設置・周知は義務の中核です。他のハラスメント窓口との一体運用や外部委託も認められています。窓口担当者向けのマニュアル・研修、該当するか微妙な段階でも広く受け付ける運用の整備が求められます。"},
  {name:"３ 発生後の迅速・適切な対応", qs:[7,8,9], duty:true,
   advice:"事実確認の手順（客観証拠の確認を含む）、被害を受けた従業員への配慮措置、再発防止措置をあらかじめ決めておくことが求められます。発生時に場当たりで対応する状態は、措置義務の観点からも従業員保護の観点からもリスクがあります。"},
  {name:"４ 悪質なケースの抑止措置", qs:[10,11], duty:true,
   advice:"特に悪質なケースへの対処方針（警察への通報・警告文・サービス提供の停止・出入禁止・仮処分等）の事前の明確化と、実行できる体制の整備が義務とされています。現場任せにせず、会社としての判断基準とエスカレーションルートを決めておくことが重要です。"},
  {name:"５ プライバシー保護・不利益取扱いの禁止", qs:[12,13], duty:true,
   advice:"相談者のプライバシー保護の措置と、相談等を理由とする不利益取扱いをしない旨の規定・周知が義務とされています。就業規則や関連規程の見直しが必要になる部分です。"},
  {name:"６ さらに望ましい取組", qs:[14,15], duty:false,
   advice:"顧客対応力向上の研修や、取引先との関係での対応（自社従業員への注意喚起・他社からの協力要請への対応）は、指針上は努力義務・望ましい取組ですが、実効性を高めるうえで有用です。"}
];

function ksdScore(){
  var warn=document.getElementById('ksdWarn');
  var vals={};
  for(var i=1;i<=15;i++){
    var el=document.querySelector('.ksd input[name="q'+i+'"]:checked');
    if(!el){warn.style.display='block'; return;}
    vals[i]=parseInt(el.value,10);
  }
  warn.style.display='none';

  var dutyGot=0, dutyMax=0;
  for(var i=1;i<=13;i++){dutyGot+=vals[i]; dutyMax+=2;}
  var pct=Math.round(dutyGot/dutyMax*100);

  var lvlEl=document.getElementById('ksdLvl'), msgEl=document.getElementById('ksdMsg');
  document.getElementById('ksdPct').textContent=pct+'%';
  if(pct>=90){
    lvlEl.textContent='おおむね整備されています'; lvlEl.className='lvl ok';
    msgEl.textContent='義務とされている措置はおおむね整備されている状態です。運用が形骸化していないか（窓口の周知度、研修の実施状況など）の定期的な点検と、下記で「一部」にとどまった項目の底上げを検討するとよいでしょう。';
  }else if(pct>=60){
    lvlEl.textContent='一部に不足があります'; lvlEl.className='lvl mid';
    msgEl.textContent='基本的な取組はあるものの、措置義務の観点からは不足している項目があります。措置義務はすでに施行されています。下記の項目別の結果を参考に、不足部分の整備を進めることをおすすめします。';
  }else{
    lvlEl.textContent='体制の整備が必要な状態です'; lvlEl.className='lvl ng';
    msgEl.textContent='義務とされている措置の多くが未整備の状態です。措置義務は2026年10月1日からすでに施行されており、行政（厚生労働大臣。権限の一部は都道府県労働局長に委任されています）による助言・指導・勧告の対象となり得るほか、勧告に従わない場合には企業名が公表されることがあります（労働施策総合推進法42条）。方針の明文化と相談窓口の設置から、早めに整備に着手することをおすすめします。';
  }

  var html='';
  ksdCatDef.forEach(function(c){
    var got=0, max=c.qs.length*2;
    c.qs.forEach(function(q){got+=vals[q];});
    var p=Math.round(got/max*100);
    var flag, cls;
    if(p>=90){flag='○ 整備されています'; cls='ok';}
    else if(p>=50){flag='△ 一部に不足があります'; cls='mid';}
    else {flag='× 整備が必要です'; cls='ng';}
    html+='<div class="catres"><h3>'+c.name+(c.duty?'':'（努力義務・望ましい取組）')+'</h3>'
        +'<div class="bar"><i style="width:'+p+'%"></i></div>'
        +'<p><span class="flag '+cls+'">'+flag+'</span></p>'
        +(p<90?'<p>'+c.advice+'</p>':'')
        +'</div>';
  });
  document.getElementById('ksdCats').innerHTML=html;
  var r=document.getElementById('ksdResult');
  r.style.display='block';
  r.scrollIntoView({behavior:'smooth'});
}""",
    ),
    dict(
        slug="""romu-navi""",
        pfx="""lnv""",
        title="""労務トラブル初動ナビ""",
        desc="""解雇・雇止め、残業代請求、団体交渉、労働審判、労働基準監督署の調査、ハラスメントの申告、問題社員、休職・復職の8類型から選ぶと、一般的な手続の流れと初動対応のポイントがわかります。""",
        summary="""よくある労務トラブル8類型から選ぶと、一般的な手続の流れと、初動でやるべきこと・避けたいことがわかります。見通しの予測はしません。""",
        tag="""8類型から選ぶ""",
        css="""  .lnv{
    --lnv-main:#39456b; --lnv-main2:#4c5a8a; --lnv-bg:#f5f6fa; --lnv-card:#ffffff;
    --lnv-accent:#b07820; --lnv-line:#dcdfe9; --lnv-ng:#b03a3a;
  }
  .lnv *{box-sizing:border-box; margin:0; padding:0;}
  .lnv{font-family:"Hiragino Kaku Gothic ProN","Hiragino Sans","Yu Gothic","Meiryo",sans-serif;
       background:var(--lnv-bg); color:#2a2f36; line-height:1.75; padding:24px 12px; border-radius:8px;}
  .lnv .wrap{max-width:760px; margin:0 auto;}
  .lnv .head{background:var(--lnv-main); color:#fff; border-radius:10px 10px 0 0; padding:26px 24px;}
  .lnv .head h1{font-size:1.35rem; line-height:1.5;}
  .lnv .head p{font-size:.86rem; margin-top:10px; opacity:.92;}
  .lnv .lnvlead{background:var(--lnv-card); border:1px solid var(--lnv-line); border-top:none; padding:18px 24px; font-size:.92rem;}
  .lnv .grid{display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:18px;}
  .lnv .grid button{border:1.5px solid var(--lnv-line); background:var(--lnv-card); border-radius:8px;
       padding:14px 12px; font-size:.92rem; font-weight:600; cursor:pointer; text-align:left; line-height:1.5; color:#2a2f36;}
  .lnv .grid button:hover{border-color:var(--lnv-main2);}
  .lnv .grid button.on{background:var(--lnv-main); color:#fff; border-color:var(--lnv-main);}
  .lnv .panel{display:none; background:var(--lnv-card); border:1px solid var(--lnv-line); border-radius:8px; margin-top:18px; overflow:hidden;}
  .lnv .panel h2{background:var(--lnv-main2); color:#fff; font-size:1.02rem; padding:12px 18px;}
  .lnv .sec{padding:14px 18px; border-top:1px solid var(--lnv-line);}
  .lnv .sec:first-of-type{border-top:none;}
  .lnv .sec h3{font-size:.92rem; color:var(--lnv-main); margin-bottom:6px;}
  .lnv .sec p, .lnv .sec li{font-size:.9rem;}
  .lnv .sec ul, .lnv .sec ol{padding-left:1.4em;}
  .lnv .flow{display:flex; flex-wrap:wrap; gap:6px; align-items:center;}
  .lnv .flow span{background:#eef0f7; border:1px solid var(--lnv-line); border-radius:6px; padding:4px 10px; font-size:.84rem;}
  .lnv .flow i{font-style:normal; color:var(--lnv-main2); font-weight:700;}
  .lnv .caution{color:var(--lnv-ng); font-weight:600;}
  .lnv .law{background:#eef0f7; border-radius:6px; padding:10px 14px; font-size:.82rem; color:#4a515a; margin-top:4px;}
  .lnv .lnvnote{background:#eceef4; border-radius:8px; padding:16px 18px; font-size:.8rem; margin-top:20px; color:#4a515a;}
  .lnv .lnvcta{background:var(--lnv-card); border:1px solid var(--lnv-line); border-radius:8px; padding:18px; font-size:.9rem; margin-top:14px; text-align:center;}
  @media(max-width:480px){ .lnv .grid{grid-template-columns:1fr;} }""",
        body="""<div class="lnv">
<div class="wrap">

  <div class="head">
    <h1>労務トラブル初動ナビ</h1>
    <p>「従業員側から書面が届いた」「社内でトラブルが起きた」——。経営者・人事担当者の方向けに、よくある労務トラブルの類型ごとの<strong>一般的な手続の流れと初動対応のポイント</strong>をまとめました。該当する状況を選んでください。</p>
  </div>

  <div class="lnvlead">
    ※本ナビは一般的な情報提供です。実際の対応は事案ごとの事情によって大きく異なりますので、個別の見通しや方針は、資料をもとにした弁護士への相談でご確認ください。
  </div>

  <div class="grid" id="lnvGrid">
    <button data-p="lnvP1">解雇・雇止めを争う通知が届いた</button>
    <button data-p="lnvP2">残業代（未払賃金）の請求が届いた</button>
    <button data-p="lnvP3">労働組合（ユニオン）から団体交渉の申入れが届いた</button>
    <button data-p="lnvP4">労働審判を申し立てられた</button>
    <button data-p="lnvP5">労働基準監督署の調査・是正勧告を受けた</button>
    <button data-p="lnvP6">社内でハラスメントの申告があった</button>
    <button data-p="lnvP7">問題行動のある従業員への対応を検討している</button>
    <button data-p="lnvP8">メンタル不調の従業員への対応（休職・復職）</button>
  </div>

  <!-- 1 解雇・雇止め -->
  <div class="panel" id="lnvP1">
    <h2>解雇・雇止めを争う通知が届いた場合</h2>
    <div class="sec"><h3>一般的な経過</h3>
      <div class="flow"><span>本人・代理人からの通知書</span><i>→</i><span>交渉</span><i>→</i><span>あっせん・労働審判・訴訟</span><i>→</i><span>和解または判決等</span></div>
      <p style="margin-top:8px;">交渉段階で解決する事案も、労働審判・訴訟に進む事案もあります。</p></div>
    <div class="sec"><h3>初動のポイント</h3><ul>
      <li>解雇に至る経緯の資料（指導記録、注意書、議事録、就業規則、解雇通知書・理由書）を時系列で整理する。</li>
      <li>解雇理由を後から付け足すことには制約が生じ得るため、理由の整理は慎重に行う。</li>
      <li>回答期限がある場合も、焦って不用意な回答をしない。回答内容は後の手続で証拠になり得る。</li>
      <li class="caution">本人や代理人に対する感情的な反応・SNS等での言及は避ける。</li></ul></div>
    <div class="sec"><h3>知っておきたい法律の枠組み</h3>
      <p>解雇は、客観的に合理的な理由を欠き、社会通念上相当と認められない場合には、権利濫用として無効とされます（労働契約法16条）。解雇が無効と判断されると、復職に加えて解雇期間中の賃金の支払（バックペイ）が問題になるため、争いが長引くほど金銭的な負担が大きくなり得ます。</p></div>
  </div>

  <!-- 2 残業代 -->
  <div class="panel" id="lnvP2">
    <h2>残業代（未払賃金）の請求が届いた場合</h2>
    <div class="sec"><h3>一般的な経過</h3>
      <div class="flow"><span>請求書面（内容証明等）</span><i>→</i><span>資料開示の要求（タイムカード等）</span><i>→</i><span>交渉</span><i>→</i><span>労働審判・訴訟</span></div></div>
    <div class="sec"><h3>初動のポイント</h3><ul>
      <li>労働時間の記録（タイムカード、勤怠システム、PCログ、日報等）と賃金規程・雇用契約書を確保する。</li>
      <li>自社の残業代の計算方法（固定残業代、管理監督者、変形労働時間制、歩合給等）に弱点がないかを早期に点検する。制度の要件を満たしていないと、想定より大きな金額になることがある。</li>
      <li>同種の働き方の従業員が他にもいる場合、他の従業員への波及も視野に入れて方針を決める。</li>
      <li class="caution">記録の破棄・改変は絶対に行わない。</li></ul></div>
    <div class="sec"><h3>知っておきたい法律の枠組み</h3>
      <p>賃金請求権の消滅時効は5年ですが、当分の間は3年とされています（退職手当は5年。労働基準法115条・143条）。また、訴訟では未払額と同額までの付加金の支払を命じられることがあります（同法114条）。時間の経過とともに対象期間が動くため、時効管理も踏まえた対応が必要です。</p></div>
  </div>

  <!-- 3 団体交渉 -->
  <div class="panel" id="lnvP3">
    <h2>労働組合（ユニオン）から団体交渉の申入れが届いた場合</h2>
    <div class="sec"><h3>一般的な経過</h3>
      <div class="flow"><span>団体交渉申入書</span><i>→</i><span>日時・場所等の調整</span><i>→</i><span>団体交渉（複数回のことも）</span><i>→</i><span>合意または労働委員会の手続等</span></div></div>
    <div class="sec"><h3>初動のポイント</h3><ul>
      <li>申入書記載の要求事項・回答期限を確認し、期限までに「応じる姿勢」を示す連絡を行う（条件面の調整はそのうえで可能）。</li>
      <li>交渉の日時・場所・出席者・時間は、会社側からも対案を出して調整できる。社外の会議室等を利用する例も多い。</li>
      <li>要求事項に関する事実関係と資料を整理し、出席者の役割分担を決めてから臨む。</li>
      <li class="caution">組合加入を理由とする不利益な取扱いや、組合からの脱退勧奨は行わない。</li></ul></div>
    <div class="sec"><h3>知っておきたい法律の枠組み</h3>
      <p>正当な理由なく団体交渉を拒むことは不当労働行為に当たります（労働組合法7条2号）。団体交渉には誠実に応じる義務がありますが、要求をそのまま受け入れる義務まではありません。説明と協議を尽くすプロセスが重要です。</p></div>
  </div>

  <!-- 4 労働審判 -->
  <div class="panel" id="lnvP4">
    <h2>労働審判を申し立てられた場合</h2>
    <div class="sec"><h3>一般的な経過</h3>
      <div class="flow"><span>申立書の送達</span><i>→</i><span>答弁書の提出</span><i>→</i><span>第1回期日</span><i>→</i><span>調停成立または労働審判</span><i>→</i><span>（異議があれば）訴訟へ移行</span></div></div>
    <div class="sec"><h3>初動のポイント</h3><ul>
      <li class="caution">答弁書の提出期限までの準備期間が短いため、申立書が届いたらすぐに動き出す。</li>
      <li>労働審判は第1回期日で心証が大きく形成されるといわれており、答弁書の段階で主張と証拠を出し切る準備が必要。</li>
      <li>期日には事情を直接説明できる担当者（当時の上司等）の出席を検討する。</li>
      <li>解決金による調停も有力な選択肢になるため、許容できる解決水準を早期に社内で検討しておく。</li></ul></div>
    <div class="sec"><h3>知っておきたい法律の枠組み</h3>
      <p>労働審判手続は、特別の事情がある場合を除き、3回以内の期日で審理を終結しなければならないとされています（労働審判法15条2項）。短期間に集中して審理される分、初動の準備がそのまま結果に影響しやすい手続です。</p></div>
  </div>

  <!-- 5 労基署 -->
  <div class="panel" id="lnvP5">
    <h2>労働基準監督署の調査・是正勧告を受けた場合</h2>
    <div class="sec"><h3>一般的な経過</h3>
      <div class="flow"><span>調査通知・臨検</span><i>→</i><span>資料提出・聴取</span><i>→</i><span>是正勧告書・指導票の交付</span><i>→</i><span>是正報告書の提出</span></div></div>
    <div class="sec"><h3>初動のポイント</h3><ul>
      <li>求められた資料（労働条件通知書、賃金台帳、出勤簿、36協定等）を整理し、誠実に対応する。</li>
      <li>是正勧告書に記載された違反事項と報告期限を確認し、実態を踏まえた是正計画を立てる。</li>
      <li>未払賃金の遡及支払が指摘された場合は、対象者の範囲・期間の整理が重要になる。</li>
      <li class="caution">虚偽の報告や資料の改変は、それ自体が重大な問題になるので絶対に行わない。</li></ul></div>
    <div class="sec"><h3>知っておきたい法律の枠組み</h3>
      <p>是正勧告自体は行政指導ですが、放置したり虚偽の対応をしたりすると、送検などより重い対応につながるおそれがあります。指摘の根本原因（労働時間管理や賃金制度の問題）まで遡って是正することが、再発防止の観点から重要です。</p></div>
  </div>

  <!-- 6 ハラスメント申告 -->
  <div class="panel" id="lnvP6">
    <h2>社内でハラスメントの申告があった場合</h2>
    <div class="sec"><h3>一般的な経過</h3>
      <div class="flow"><span>相談・申告</span><i>→</i><span>事実関係の調査（双方・第三者の聴取）</span><i>→</i><span>認定・判断</span><i>→</i><span>被害者への配慮措置・行為者への措置</span><i>→</i><span>再発防止策</span></div></div>
    <div class="sec"><h3>初動のポイント</h3><ul>
      <li>相談者の意向を確認しつつ、迅速に事実確認に着手する（相談者・行為者とされる者の双方、必要に応じて第三者から聴取）。</li>
      <li>聴取記録を残し、客観的な資料（メール、チャット、録音等）と突き合わせて判断する。</li>
      <li>調査中の接触やプライバシーに配慮する（安易に「様子を見る」で済ませない）。</li>
      <li class="caution">相談したことを理由とする不利益な取扱いは法律上禁止されている。</li>
      <li>懲戒処分を行う場合は、就業規則上の根拠と手続、処分の重さの相当性を慎重に検討する（労働契約法15条）。</li></ul></div>
    <div class="sec"><h3>知っておきたい法律の枠組み</h3>
      <p>パワハラ・セクハラ・妊娠出産・育児介護等に関するハラスメントについては、相談体制の整備や事後の迅速・適切な対応などの措置が事業主に義務付けられています。対応を誤ると、行為者の問題にとどまらず、会社自身の責任（損害賠償等）を問われるおそれがあります。</p></div>
  </div>

  <!-- 7 問題社員 -->
  <div class="panel" id="lnvP7">
    <h2>問題行動のある従業員への対応を検討している場合</h2>
    <div class="sec"><h3>一般的な経過</h3>
      <div class="flow"><span>注意・指導（記録化）</span><i>→</i><span>書面での指導・改善機会の付与</span><i>→</i><span>配置転換・懲戒処分等の検討</span><i>→</i><span>退職勧奨・解雇は最終手段</span></div></div>
    <div class="sec"><h3>初動のポイント</h3><ul>
      <li>問題行動を「いつ・どこで・何があったか」のレベルで具体的に記録する（抽象的な「勤務態度不良」では足りない）。</li>
      <li>注意・指導は口頭だけでなく書面やメールで行い、改善の機会を与えたことを残す。</li>
      <li>段階を踏まない、いきなりの解雇は無効と判断されるリスクが高い。</li>
      <li class="caution">退職に追い込むことを目的とした仕事外し・過度な叱責は、それ自体がハラスメントや違法行為と評価されるおそれがある。</li></ul></div>
    <div class="sec"><h3>知っておきたい法律の枠組み</h3>
      <p>懲戒処分も解雇も、客観的に合理的な理由と社会通念上の相当性がなければ権利濫用として無効とされます（労働契約法15条・16条）。有効性は「問題行動の内容・程度」と「会社が踏んだプロセス」の両面で判断されるため、日々の記録と段階的な対応が結論を左右します。</p></div>
  </div>

  <!-- 8 休職・復職 -->
  <div class="panel" id="lnvP8">
    <h2>メンタル不調の従業員への対応（休職・復職）の場合</h2>
    <div class="sec"><h3>一般的な経過</h3>
      <div class="flow"><span>不調の把握・受診勧奨</span><i>→</i><span>休職発令</span><i>→</i><span>療養・経過確認</span><i>→</i><span>復職可否の判断（主治医・産業医）</span><i>→</i><span>復職支援または休職期間満了の対応</span></div></div>
    <div class="sec"><h3>初動のポイント</h3><ul>
      <li>就業規則の休職制度（休職期間、復職の要件、期間満了時の取扱い）を確認する。規定が曖昧なまま運用すると後で紛争になりやすい。</li>
      <li>休職発令時に、休職期間・復職の手続・期間満了時の取扱いを本人に書面で説明しておく。</li>
      <li>復職可否は主治医の診断書だけで決めず、産業医の意見や業務の実態も踏まえて判断する。主治医と会社の判断が食い違う場面は紛争になりやすい。</li>
      <li class="caution">不調の従業員への対応を現場任せにしない（上司の不用意な言動が二次的な紛争を生みやすい）。</li></ul></div>
    <div class="sec"><h3>知っておきたい法律の枠組み</h3>
      <p>会社は、従業員がその生命・身体等の安全を確保しつつ労働できるよう必要な配慮をするものとされています（労働契約法5条）。メンタル不調への対応は、休職・復職の手続面だけでなく、この安全配慮の観点からの検討も必要になる領域です。</p></div>
  </div>

  <!-- ▼お問い合わせ導線（設置時にリンク先・文言を編集してください）▼ -->
  <div class="lnvcta" id="lnvCta" style="display:none;">
    個別の事案の見通しや対応方針は、資料を拝見したうえでの検討が必要です。労務トラブルへの対応に関するご相談は、<a href="#contact" style="color:var(--lnv-main); font-weight:700;">下のお問い合わせ欄</a>のメールアドレスまでご連絡ください。
  </div>
  <!-- ▲お問い合わせ導線▲ -->

  <div class="lnvnote">
    <strong>ご利用上の注意</strong><br>
    ・本ナビは一般的な情報提供であり、個別の事案に関する法的助言ではありません。記載した流れ・ポイントが当てはまらない事案も多くあります。<br>
    ・紛争の結果を予測・保証するものではありません。個別の見通しは、具体的な資料・事実関係をもとにした検討が必要です。<br>
    ・選択内容がサーバーに送信されることはありません（お使いのブラウザ内でのみ処理されます）。
  </div>

</div>
</div>
<a class="back" href="../shindan.html">← 診断ツール一覧に戻る</a>""",
        js="""(function(){
  var grid=document.getElementById('lnvGrid');
  grid.addEventListener('click', function(e){
    var btn=e.target.closest('button'); if(!btn) return;
    grid.querySelectorAll('button').forEach(function(b){b.classList.remove('on');});
    btn.classList.add('on');
    document.querySelectorAll('.lnv .panel').forEach(function(p){p.style.display='none';});
    var p=document.getElementById(btn.getAttribute('data-p'));
    p.style.display='block';
    document.getElementById('lnvCta').style.display='block';
    p.scrollIntoView({behavior:'smooth'});
  });
})();""",
    ),
]

# 記事ページに診断ツールへの導線を入れる対応表（記事slug → 診断slug）
SHINDAN_FOR = {
    "harassment-madoguchi": "harassment",
    "harassment-chosa": "harassment",
    "harassment-kenshu-gimu": "harassment",
    "pawahara-6ruikei": "harassment",
    "pawahara-taio-5steps": "harassment",
    "pawahara-kokuseki": "harassment",
    "gyaku-pawahara": "harassment",
    "shido-pawahara-kyokai": "harassment",
    "sekuhara-sekinin": "harassment",
    "sekuhara-shobun-ryotei": "harassment",
    "shukatsu-sekuhara-gimuka": "harassment",
    "matahara": "harassment",
    "kasuhara-taisaku-gimuka": "kasuhara",
    "kasuhara-genba-taio": "kasuhara",
    "kasuhara-kyaku-torihiki-kyohi": "kasuhara",
    "kasuhara-sodan-madoguchi-taisei": "kasuhara",
    "kasuhara-sns-kuchikomi": "kasuhara",
    "kasuhara-shazai-nensho": "kasuhara",
    "kasuhara-rosai-nintei": "kasuhara",
    "kasuhara-jisha-jugyoin-kagai": "kasuhara",
    "koueki-tsuho-kaisei-shiko": "koueki",
    "naibu-tsuho": "koueki",
    "rodo-shinpan": "romu-navi",
    "rokisho-chosa": "romu-navi",
    "kaiko-mae-checklist": "romu-navi",
}
