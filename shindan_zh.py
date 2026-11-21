# -*- coding: utf-8 -*-
"""診断ツールの繁体字版（簡体字版は build.py の to_cn で自動変換）。

CSS は shindan.py の SHINDAN と共用するため、body の class 名・要素の id・
JS の関数名は日本語版と完全に一致させている（変更すると表示が崩れる）。
"""

SHINDAN_ZH = {}

# ===== 1 職場騷擾防治 綜合診斷 =====
SHINDAN_ZH["harassment"] = dict(
    title="職場騷擾防治 綜合診斷",
    tag="16題 ／ 5分鐘",
    summary="依據6份騷擾防治指針共通的措施架構，用16題檢視方針的明確化、諮詢制度、事後處理、隱私保護，以及各類型特別要求的措施。",
    desc="性騷擾、懷孕生產、育嬰照護、職場霸凌，再加上2026年10月1日起成為法定義務的顧客騷擾與對求職學生的性騷擾。依照厚生勞動省6份指針共通的措施架構，用16題檢視貴公司的防治制度。輸入內容不會被傳送。",
    body="""<div class="hsd">
<div class="wrap">

  <div class="head">
    <h1>職場騷擾防治 綜合診斷</h1>
    <p>在日本，職場騷擾的防治是法律上的義務。除了性騷擾（男女僱用機會均等法11條）、與懷孕、生產、育嬰留職停薪等相關的騷擾（同法15條、育兒照護休業法25條）、職場霸凌（勞動施策綜合推進法31條）之外，自2026年（令和8年）10月1日起，顧客騷擾（同法33條）與對求職中的學生等所為的性騷擾（均等法13條），也成為所有僱主在僱用管理上必須採取措施的事項。<br>
    本診斷依照厚生勞動省6份指針共通的措施架構，讓您用16題檢視貴公司騷擾防治制度的整體狀況。</p>
  </div>

  <div class="hsdlead">
    <strong>使用方式</strong>：請就每一題，選擇最接近貴公司現狀的選項。所需時間約3到4分鐘。<br>
    未特別註明的題目，是各類型騷擾共通被要求的措施。若屬於「某一類型騷擾已做到，其他類型尚未做到」的情形，請選「部分做到」。<br><br>
    <strong>所謂「部分做到」</strong>：指雖然有所作為但仍不充分的狀態。例如：實際上有在運作但沒有形成文件或規則／有規則但沒有讓員工知悉／只及於部分騷擾類型、部分部門或部分員工等情形。
  </div>

  <form id="hsdForm">

  <div class="hsdcat">
    <h2>一　公司方針的明確化與周知、宣導</h2>
    <div class="q"><div class="qt"><span class="num">Q1</span>已用文件（工作規則、公司內部刊物、內部網站等）明確表示不得為職場霸凌、性騷擾、與懷孕生產及育兒照護相關的騷擾等行為的公司方針，以及各類型騷擾的內容，並讓包含管理職在內的員工知悉。</div>
      <div class="opts" data-q="1"></div></div>
    <div class="q"><div class="qt"><span class="num">Q2</span>已在工作規則等的服務紀律、懲戒規定中，訂明對騷擾行為人將嚴正處理的方針及處理內容，並讓員工知悉。</div>
      <div class="opts" data-q="2"></div></div>
    <div class="q"><div class="qt"><span class="num">Q3</span>已就懷孕、生產，以及利用育嬰留職停薪、照護留職停薪等制度一事，進行方針的周知與宣導，避免出現否定性的言行（例如「請假會造成大家的麻煩」等）。</div>
      <div class="opts" data-q="3"></div></div>
    <div class="q"><div class="qt"><span class="num">Q4</span>已實施騷擾防治的研修、講習等（包含針對管理職者）。</div>
      <div class="opts" data-q="4"></div></div>
  </div>

  <div class="hsdcat">
    <h2>二　諮詢對應制度的建立</h2>
    <div class="q"><div class="qt"><span class="num">Q5</span>已事先設置騷擾的諮詢窗口（指定負責人、設置諮詢制度、委外處理，任一方式均可），並讓員工知悉。</div>
      <div class="opts" data-q="5"></div></div>
    <div class="q"><div class="qt"><span class="num">Q6</span>有讓窗口負責人能妥適處理的機制（彙整處理要點的手冊、針對負責人的研修、與人事部門等連繫合作的機制等）。</div>
      <div class="opts" data-q="6"></div></div>
    <div class="q"><div class="qt"><span class="num">Q7</span>對於是否構成騷擾尚屬微妙的案例，或仍處於「有發生之虞」的階段，也廣泛受理諮詢；並且對橫跨職場霸凌、性騷擾等多種類型的諮詢，能以單一窗口統一處理。</div>
      <div class="opts" data-q="7"></div></div>
  </div>

  <div class="hsdcat">
    <h2>三　發生後的迅速、妥適處理</h2>
    <div class="q"><div class="qt"><span class="num">Q8</span>有在接到諮詢後迅速且正確確認事實關係的程序（例如向諮詢者與被指為行為人的一方雙方、以及第三人進行訪談等）。</div>
      <div class="opts" data-q="8"></div></div>
    <div class="q"><div class="qt"><span class="num">Q9</span>在確認騷擾事實後，會迅速採取對受害員工的照護措施（調職等隔離措施、回復勞動條件上的不利益、對心理健康不佳者的諮詢對應等）。</div>
      <div class="opts" data-q="9"></div></div>
    <div class="q"><div class="qt"><span class="num">Q10</span>在確認騷擾事實後，會依工作規則等對行為人採取適當的措施（懲戒、調職、告誡指導等）。</div>
      <div class="opts" data-q="10"></div></div>
    <div class="q"><div class="qt"><span class="num">Q11</span>無論事實是否獲得確認，都會採取防止再發生的措施（重新周知方針、辦理研修等）。</div>
      <div class="opts" data-q="11"></div></div>
  </div>

  <div class="hsdcat">
    <h2>四　同時必須採取的措施</h2>
    <div class="q"><div class="qt"><span class="num">Q12</span>已採取保護諮詢者、行為人等隱私的措施（在手冊中明文規定、對負責人辦理研修等），並讓員工知悉其隱私會受到保護。</div>
      <div class="opts" data-q="12"></div></div>
    <div class="q"><div class="qt"><span class="num">Q13</span>已以文件訂明不會因為員工提出騷擾諮詢、或配合事實調查等原因，而為解僱或其他不利處遇，並讓員工知悉。</div>
      <div class="opts" data-q="13"></div></div>
  </div>

  <div class="hsdcat">
    <h2>五　各類型特別要求的措施<small>包含2026年10月施行的新義務</small></h2>
    <div class="q"><div class="qt"><span class="num">Q14</span>為消除與懷孕、生產、育兒、照護相關騷擾的原因及背景，已採取整備業務體制的措施（重新分配懷孕員工或制度利用者的工作、確保替代人力等）。</div>
      <div class="opts" data-q="14"></div></div>
    <div class="q"><div class="qt"><span class="num">Q15</span>對於防止向求職中的學生、實習生等所為的性騷擾，也已採取方針明確化及諮詢對應的制度（自2026年10月1日起成為法定義務）。</div>
      <div class="opts" data-q="15"></div></div>
    <div class="q"><div class="qt"><span class="num">Q16</span>已採取措施保護員工免於顧客或交易對象顯著的騷擾行為（顧客騷擾），包括方針的明確化、諮詢制度、發生時的處理程序等（自2026年10月1日起成為法定義務）。</div>
      <div class="opts" data-q="16"></div></div>
  </div>

  <div class="btnrow">
    <button type="button" class="go" onclick="hsdScore()">查看診斷結果</button>
    <p class="warn" id="hsdWarn">有尚未回答的題目。請回答所有題目。</p>
  </div>
  </form>

  <div id="hsdResult">
    <div class="score">
      <div style="font-size:.9rem;">騷擾防治（法定措施義務）的達成度</div>
      <div class="pct" id="hsdPct"></div>
      <div class="lvl" id="hsdLvl"></div>
      <div class="msg" id="hsdMsg"></div>
    </div>
    <div id="hsdCats"></div>

    <div class="hsdcta">
      關於騷擾防治制度的建立（防治規程與工作規則的整備、諮詢窗口的設計、研修、發生時的調查對應等），歡迎以中文或日文，寄到<a href="#contact" style="color:var(--hsd-main); font-weight:700;">下方諮詢欄</a>的電子郵件地址聯繫。
    </div>
  </div>

  <div class="hsdnote">
    <strong>使用上的注意</strong><br>
    ・本診斷是依據勞動施策綜合推進法31條、33條，男女僱用機會均等法11條、13條、15條，育兒照護休業法25條，以及依這些規定訂定的厚生勞動省各指針（職場霸凌指針＝令和2年厚生勞動省告示第5號、顧客騷擾指針＝令和8年厚生勞動省告示第51號、性騷擾指針＝平成18年厚生勞動省告示第615號、求職者等性騷擾指針＝令和8年厚生勞動省告示第52號、懷孕生產騷擾指針＝平成28年厚生勞動省告示第312號、育兒照護騷擾相關＝平成21年厚生勞動省告示第509號）的內容所製作的一般性資訊提供，並非針對個別案件的法律意見。<br>
    ・診斷結果僅供參考。實際是否已滿足法定的措施義務，須依個別情況判斷。<br>
    ・就派遣員工而言，派遣公司與要派公司雙方都負有措施義務。<br>
    ・輸入的內容不會被傳送到伺服器（僅在您的瀏覽器內處理）。
  </div>

</div>
</div>
<a class="back" href="../shindan.html">← 回到診斷工具一覽</a>""",
    js="""(function(){
  var opts=[["已做到",2],["部分做到",1],["尚未做到",0]];
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
  {name:"一 方針的明確化與周知、宣導", qs:[1,2,3,4],
   advice:"以文字明訂並讓員工知悉「不得為騷擾行為」的方針，以及對行為人嚴正處理的方針（懲戒規定），是所有類型騷擾共通的措施義務的起點。可以先從整備工作規則、防治規程，以及辦理含管理職在內的研修著手。此外，為避免出現對懷孕、生產或利用育兒照護制度的否定性言行而進行的周知與宣導，也屬於義務的內容。"},
  {name:"二 諮詢制度的建立", qs:[5,6,7],
   advice:"設置諮詢窗口並讓員工知悉，是措施義務的核心。指針認為，窗口以能統一處理各類型騷擾為宜。並且要求整備給窗口負責人的手冊與研修，以及在是否構成騷擾尚屬微妙的階段也廣泛受理的運作方式。"},
  {name:"三 發生後的迅速、妥適處理", qs:[8,9,10,11],
   advice:"事先決定事實確認的程序、對受害員工的照護措施、對行為人的措施，以及防止再發生的措施，是法律所要求的。若停留在事情發生才臨時應變的狀態，不只在措施義務上有風險，在安全照護義務與懲戒處分是否有效的層面上也有風險。"},
  {name:"四 隱私保護與禁止不利處遇", qs:[12,13],
   advice:"保護諮詢者、行為人等隱私的措施，以及訂明並周知不因提出諮詢等原因而為不利處遇，都屬於法定義務。這部分往往需要一併檢討修改工作規則或騷擾防治規程。"},
  {name:"五 各類型特別要求的措施", qs:[14,15,16],
   advice:"關於與懷孕、生產、育兒、照護相關的騷擾，為消除其原因與背景而整備業務體制屬於法定義務。此外，自2026年10月1日起，防止對求職中的學生等所為的性騷擾，以及顧客騷擾的對應，也納入措施義務的範圍。沿用舊有的騷擾防治規程，往往無法涵蓋這兩項新義務，建議一併檢討修改規程與制度。"}
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
    lvlEl.textContent='大致已建立'; lvlEl.className='lvl ok';
    msgEl.textContent='法律所要求的措施大致上都已具備。建議定期檢視運作是否流於形式（員工對窗口的認知程度、研修的實施狀況、規程與實際處理是否一致等），並就下列僅達「部分」的項目加以補強。';
  }else if(pct>=60){
    lvlEl.textContent='部分項目不足'; lvlEl.className='lvl mid';
    msgEl.textContent='基本的措施已有，但從措施義務的角度仍有不足的項目。尤其自2026年10月起成為法定義務的顧客騷擾對應，以及對求職中學生等的性騷擾防治，往往是舊有規程未能涵蓋的部分。建議參考下列各項結果，逐步補足不足之處。';
  }else{
    lvlEl.textContent='需要建立制度'; lvlEl.className='lvl ng';
    msgEl.textContent='法律所要求的措施多數尚未建立。未因應這些措施義務時，可能成為行政機關建議、指導、勸告的對象；若不遵從勸告，還可能被公布企業名稱（勞動施策綜合推進法42條，男女僱用機會均等法35條、36條，育兒照護休業法56條、56條之2）。此外，一旦實際發生騷擾，公司本身也可能被追究損害賠償責任。建議先從方針的明文化與設置諮詢窗口著手，盡早開始整備。';
  }

  var html='';
  hsdCatDef.forEach(function(c){
    var g=0, m=c.qs.length*2;
    c.qs.forEach(function(q){g+=vals[q];});
    var p=Math.round(g/m*100);
    var flag, cls;
    if(p>=90){flag='○ 已建立'; cls='ok';}
    else if(p>=50){flag='△ 部分不足'; cls='mid';}
    else {flag='× 需要建立'; cls='ng';}
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
)

# ===== 2 公益通報（內部檢舉）對應制度 簡易診斷 =====
SHINDAN_ZH["koueki"] = dict(
    title="公益通報對應制度 簡易診斷",
    tag="13題 ／ 5分鐘",
    summary="2026年12月1日施行的修正公益通報者保護法，用13題檢視檢舉窗口、獨立性、檢舉人保護與修法對應的狀況。",
    desc="修正公益通報者保護法（令和7年法律第62號）將於2026年12月1日施行。以修正後的法律與法定指針的內容為基礎，用13題檢視貴公司內部檢舉制度的對應狀況。輸入內容不會被傳送。",
    body="""<div class="ktd">
<div class="wrap">

  <div class="head">
    <h1>公益通報對應制度 簡易診斷</h1>
    <p>日本的修正公益通報者保護法（令和7年法律第62號）將於<strong>2026年（令和8年）12月1日施行</strong>。<br>
    以檢舉為理由的解僱、懲戒，新增了對承辦個人的刑事罰；離職協議書中「不得檢舉」的條款也將變成無效。這是影響所有企業的修法。<br>
    本診斷以修正後的法律，以及依法由內閣總理大臣訂定的指針（法定指針）的內容為基礎，讓您用13題檢視貴公司的對應狀況。</p>
  </div>

  <div class="ktdlead">
    <strong>使用方式</strong>：請就每一題，選擇最接近貴公司現狀的選項。所需時間約3分鐘。<br><br>
    <strong>所謂「部分做到」</strong>：指雖然有所作為但仍不充分的狀態。例如：實際上有在運作但沒有形成文件或規則／有規程但沒有讓員工知悉／只及於部分對象或部分部門等情形。
  </div>

  <form id="ktdForm">

  <div class="sizebox">
    <div class="qt">首先，請選擇貴公司經常僱用的員工人數。</div>
    <div class="opts" id="ktdSize">
      <label><input type="radio" name="qsize" value="big"><span>301人以上</span></label>
      <label><input type="radio" name="qsize" value="small"><span>300人以下</span></label>
    </div>
    <p style="font-size:.8rem; margin-top:8px; color:#4a514a;">※建立內部檢舉制度，在301人以上的企業是法律上的義務，在300人以下的企業是努力義務。但禁止對檢舉人為不利處遇、禁止妨礙檢舉等規定，不論企業規模一律適用。</p>
  </div>

  <div class="ktdcat">
    <h2>一　檢舉窗口、從事者、周知<small>法11條1項、2項</small></h2>
    <div class="q"><div class="qt"><span class="num">Q1</span>已設置內部檢舉的受理窗口，並訂有從受理、調查到改正的對應制度。</div>
      <div class="opts" data-q="1"></div></div>
    <div class="q"><div class="qt"><span class="num">Q2</span>已以書面指定從事檢舉對應業務的承辦人（從事者），並且也已告知被指定的本人。</div>
      <div class="opts" data-q="2"></div></div>
    <div class="q"><div class="qt"><span class="num">Q3</span>已將窗口的聯絡方式與檢舉人受到保護的機制，不只讓在職員工，也讓離職者（離職後1年內）與業務委託的自由工作者能以可理解的方式知悉。</div>
      <div class="opts" data-q="3"></div></div>
  </div>

  <div class="ktdcat">
    <h2>二　獨立性與排除利益衝突<small>法定指針</small></h2>
    <div class="q"><div class="qt"><span class="num">Q4</span>為使涉及經營高層的案件也能運作，已確保獨立於經營高層的檢舉途徑（外部窗口、向監察人等檢舉的管道等）。</div>
      <div class="opts" data-q="4"></div></div>
    <div class="q"><div class="qt"><span class="num">Q5</span>有機制將該案件的關係人（被檢舉指名的人或其下屬等）排除於該案件的檢舉對應業務之外。</div>
      <div class="opts" data-q="5"></div></div>
  </div>

  <div class="ktdcat">
    <h2>三　檢舉人的保護<small>法3條、11條之2、11條之3</small></h2>
    <div class="q"><div class="qt"><span class="num">Q6</span>有規則限制「檢舉人是誰」的資訊只在必要最小限度的範圍內共享，並已採取措施防止追查檢舉人身分的行為（檢舉人探索）。</div>
      <div class="opts" data-q="6"></div></div>
    <div class="q"><div class="qt"><span class="num">Q7</span>已訂有規則禁止以檢舉為理由的解僱、懲戒、調職、刁難等不利處遇，並有在檢舉後持續關注檢舉人狀況的運作方式。</div>
      <div class="opts" data-q="7"></div></div>
    <div class="q"><div class="qt"><span class="num">Q8</span>已檢查離職協議書、承諾書等公司內部的範本中，是否放入了「不進行檢舉、申告」之類的條款（修正後的法律禁止無正當理由妨礙公益通報的行為，違反此規定所成立的協議無效）。</div>
      <div class="opts" data-q="8"></div></div>
  </div>

  <div class="ktdcat">
    <h2>四　修法對應與日常運作<small>修正後的法律、法定指針</small></h2>
    <div class="q"><div class="qt"><span class="num">Q9</span>已修改運作方式，使業務委託的自由工作者（包含業務委託結束後1年內的人）所為的檢舉也在受理範圍內。</div>
      <div class="opts" data-q="9"></div></div>
    <div class="q"><div class="qt"><span class="num">Q10</span>在進行解僱或懲戒之前，有程序確認該對象是否曾提出檢舉、以及決定處分的人是否知悉此事，並留下紀錄（檢舉後1年內的解僱、懲戒會被推定為以檢舉為理由）。</div>
      <div class="opts" data-q="10"></div></div>
    <div class="q"><div class="qt"><span class="num">Q11</span>已依法定指針的內容（指定從事者、確保獨立性、防止範圍外共享、防止不利處遇等），整備公司內部的檢舉相關規程。</div>
      <div class="opts" data-q="11"></div></div>
    <div class="q"><div class="qt"><span class="num">Q12</span>已妥善保管檢舉對應的紀錄，並對員工實施教育、研修，以及揭露運作實績的概要。</div>
      <div class="opts" data-q="12"></div></div>
    <div class="q"><div class="qt"><span class="num">Q13</span>有向檢舉人適當通知調查結果與改正結果的運作方式。</div>
      <div class="opts" data-q="13"></div></div>
  </div>

  <div class="btnrow">
    <button type="button" class="go" onclick="ktdScore()">查看診斷結果</button>
    <p class="warn" id="ktdWarn">有尚未回答的題目。請回答員工人數與所有題目。</p>
  </div>
  </form>

  <div id="ktdResult">
    <div class="score">
      <div style="font-size:.9rem;">公益通報對應制度（Q1〜Q13）的達成度</div>
      <div class="pct" id="ktdPct"></div>
      <div class="lvl" id="ktdLvl"></div>
      <div class="msg" id="ktdMsg"></div>
    </div>
    <div id="ktdCats"></div>

    <div class="ktdcta">
      關於內部檢舉制度的整備（公司內部規程、離職協議書範本的檢討修改、從事者的指定、研修等），歡迎以中文或日文，寄到<a href="#contact" style="color:var(--ktd-navy); font-weight:700;">下方諮詢欄</a>的電子郵件地址聯繫。
    </div>
  </div>

  <div class="ktdnote">
    <strong>使用上的注意</strong><br>
    ・本診斷是依據公益通報者保護法（經令和7年法律第62號修正後者），以及依同法11條4項由內閣總理大臣訂定的指針（法定指針）的內容所製作的一般性資訊提供，並非針對個別案件的法律意見。<br>
    ・診斷結果僅供參考。實際是否已滿足法律上的義務，須依個別情況判斷。<br>
    ・輸入的內容不會被傳送到伺服器（僅在您的瀏覽器內處理）。
  </div>

</div>
</div>
<a class="back" href="../shindan.html">← 回到診斷工具一覽</a>""",
    js="""(function(){
  var opts=[["已做到",2],["部分做到",1],["尚未做到",0]];
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
  {name:"一 檢舉窗口、從事者、周知", qs:[1,2,3],
   advice:"設置窗口、以書面指定從事者，並讓對象知悉，是建立制度的起點。修正後的法律在條文上也明確要求必須讓員工等知悉這套制度。僅僅設了窗口而周知不足的狀態，被認為並不足夠。"},
  {name:"二 獨立性與排除利益衝突", qs:[4,5],
   advice:"讓涉及經營高層的案件不會被壓下來的機制（外部窗口或通往監察人等的管道），以及把案件關係人排除於對應業務之外的規則，是法定指針所要求制度的核心。"},
  {name:"三 檢舉人的保護", qs:[6,7,8],
   advice:"修正後的法律明文禁止試圖查出檢舉人身分的行為（檢舉人探索）與妨礙檢舉的行為，並規定「不得檢舉」的協議無效。檢查離職協議書、承諾書的範本，是施行前務必完成的項目。"},
  {name:"四 修法對應與日常運作", qs:[9,10,11,12,13],
   advice:"將自由工作者納入對象、檢舉後1年內的解僱與懲戒被推定為以檢舉為理由等，因應修法需要重新檢討日常的人事流程。特別是在解僱、懲戒之前確認有無檢舉並留下紀錄的做法，是面對推定規定的重要準備。"}
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
    ? '以貴公司的規模（301人以上）而言，建立內部檢舉制度與指定從事者是法律上的義務；修正後的法律並強化了違反時的行政措施（建議、指導、勸告，就指定從事者的義務則包括不遵從勸告時的命令，以及作出命令時的公布）、要求報告與進入檢查的權限，以及罰則。'
    : '以貴公司的規模（300人以下）而言，建立制度屬於努力義務；但禁止對檢舉人為不利處遇、禁止妨礙檢舉與「不得檢舉」協議無效、禁止檢舉人探索，以及對承辦個人的刑事罰，不論企業規模一律適用。';

  if(pct>=90){
    lvlEl.textContent='大致已建立'; lvlEl.className='lvl ok';
    msgEl.textContent='大致上已達到修正後法律所要求的水準。'+sizeNote+'建議繼續補強僅達「部分」的項目，並在施行後持續檢視運作狀況。';
  }else if(pct>=60){
    lvlEl.textContent='部分項目不足'; lvlEl.className='lvl mid';
    msgEl.textContent='基本制度已有，但在因應修法上仍有不足的項目。'+sizeNote+'施行日是2026年12月1日。建議參考下列各項結果，逐步補足不足之處。';
  }else{
    lvlEl.textContent='需要建立制度'; lvlEl.className='lvl ng';
    msgEl.textContent='修正後法律所要求的制度多數尚未建立。'+sizeNote+'尤其是以檢舉為理由的解僱、懲戒，新增了對決定處分的個人處6個月以下拘禁刑或30萬日圓以下罰金、對法人處3000萬日圓以下罰金（兩罰規定）；而且檢舉後1年內的解僱、懲戒會被推定為以檢舉為理由。建議及早為施行日（2026年12月1日）做好整備。';
  }

  var html='';
  ktdCatDef.forEach(function(c){
    var cgot=0, cmax=c.qs.length*2;
    c.qs.forEach(function(q){cgot+=vals[q];});
    var p=Math.round(cgot/cmax*100);
    var flag, cls;
    if(p>=90){flag='○ 已建立'; cls='ok';}
    else if(p>=50){flag='△ 部分不足'; cls='mid';}
    else {flag='× 需要建立'; cls='ng';}
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
)

# ===== 3 顧客騷擾對應制度 簡易診斷 =====
SHINDAN_ZH["kasuhara"] = dict(
    title="顧客騷擾對應制度 簡易診斷",
    tag="15題 ／ 5分鐘",
    summary="用15題檢視方針的明確化與周知、諮詢對應制度、對現場員工的支援，以及紀錄與防止再發生。交易對象（企業間交易）的言行也在對象範圍內。",
    desc="2026年10月1日施行的修正勞動施策綜合推進法33條，已將顧客騷擾的僱用管理措施定為所有僱主的義務。可用15題檢視方針的明確化、諮詢對應制度、現場處理程序等。輸入內容不會被傳送。",
    body="""<div class="ksd">
<div class="wrap">

  <div class="head">
    <h1>顧客騷擾對應制度 簡易診斷</h1>
    <p>自2026年（令和8年）10月1日起，不論企業規模，為防止顧客騷擾而在僱用管理上採取必要措施，已是日本所有僱主的義務（勞動施策綜合推進法33條）。<br>
    本診斷以厚生勞動省的指針（令和8年厚生勞動省告示第51號）的內容為基礎，讓您用15題檢視貴公司的對應制度。</p>
  </div>

  <div class="ksdlead">
    <strong>使用方式</strong>：請就每一題，選擇最接近貴公司現狀的選項。所需時間約3分鐘。<br>
    Q1〜Q13是指針所定的<strong>義務</strong>措施，Q14、Q15是指針認為宜加努力的作為。<br><br>
    <strong>所謂「部分做到」</strong>：指雖然有所作為但仍不充分的狀態。例如：實際上有在運作但沒有形成文件或規則／有規則但沒有讓員工知悉／只及於部分部門、部分店鋪或部分員工等情形。
  </div>

  <form id="ksdForm">

  <div class="ksdcat">
    <h2>一　公司方針的明確化與周知、宣導<small>指針4⑴</small></h2>
    <div class="q"><div class="qt"><span class="num">Q1</span>已用文件（公司內部刊物、內部網站、手冊等）明確表示公司將對顧客騷擾堅定應對、保護員工的方針，並讓包含管理職在內的員工知悉。</div>
      <div class="opts" data-q="1"></div></div>
    <div class="q"><div class="qt"><span class="num">Q2</span>已事先訂定顧客騷擾發生時的處理程序（向上級報告、不讓員工單獨應對、對話的錄音錄影、報警的判斷標準、向總公司或總部通報等），並讓員工知悉。</div>
      <div class="opts" data-q="2"></div></div>
    <div class="q"><div class="qt"><span class="num">Q3</span>已就公司的方針與處理程序實施研修、講習等。</div>
      <div class="opts" data-q="3"></div></div>
  </div>

  <div class="ksdcat">
    <h2>二　諮詢對應制度的建立<small>指針4⑵</small></h2>
    <div class="q"><div class="qt"><span class="num">Q4</span>已設置顧客騷擾的諮詢窗口（指定負責人、設置諮詢制度、委外處理，任一方式均可），並讓員工知悉。</div>
      <div class="opts" data-q="4"></div></div>
    <div class="q"><div class="qt"><span class="num">Q5</span>有讓窗口負責人能妥適處理的機制（彙整處理要點的手冊、針對負責人的研修、與相關部門連繫合作的機制等）。</div>
      <div class="opts" data-q="5"></div></div>
    <div class="q"><div class="qt"><span class="num">Q6</span>對於是否構成顧客騷擾尚屬微妙的案例，或仍處於「有發生之虞」的階段，也以廣泛受理諮詢的方式運作。</div>
      <div class="opts" data-q="6"></div></div>
  </div>

  <div class="ksdcat">
    <h2>三　發生後的迅速、妥適處理<small>指針4⑶</small></h2>
    <div class="q"><div class="qt"><span class="num">Q7</span>有在接到諮詢後迅速且正確確認事實關係的程序（向當事人或周遭員工訪談、確認錄音錄影等客觀證據等）。</div>
      <div class="opts" data-q="7"></div></div>
    <div class="q"><div class="qt"><span class="num">Q8</span>已準備對受害員工的照護措施（更換承辦人或改由多人應對、與行為人隔離、對心理健康不佳者的諮詢對應等）。</div>
      <div class="opts" data-q="8"></div></div>
    <div class="q"><div class="qt"><span class="num">Q9</span>發生後會採取防止再發生的措施，例如重新周知方針，以及分析並改善原因與背景（包含商品、服務、接待一方的問題）。</div>
      <div class="opts" data-q="9"></div></div>
  </div>

  <div class="ksdcat">
    <h2>四　抑止特別惡質案例的措施<small>指針4⑷</small></h2>
    <div class="q"><div class="qt"><span class="num">Q10</span>已事先訂定對特別惡質案例（例如反覆提出過度要求）的處理方針（報警、發出警告書、停止提供服務、禁止進入店鋪或設施、聲請假處分命令等），並讓員工知悉。</div>
      <div class="opts" data-q="10"></div></div>
    <div class="q"><div class="qt"><span class="num">Q11</span>有能實際執行上述處理的體制（相關部門間的合作、向總公司、法務部門或外部專家諮詢的管道等）。</div>
      <div class="opts" data-q="11"></div></div>
  </div>

  <div class="ksdcat">
    <h2>五　同時必須採取的措施<small>指針4⑸</small></h2>
    <div class="q"><div class="qt"><span class="num">Q12</span>已採取保護諮詢者等隱私的措施（在手冊中明文規定、對負責人辦理研修等），並讓員工知悉其隱私會受到保護。</div>
      <div class="opts" data-q="12"></div></div>
    <div class="q"><div class="qt"><span class="num">Q13</span>已在工作規則等文件中訂明不會因為員工提出顧客騷擾的諮詢等原因，而為解僱或其他不利處遇，並讓員工知悉。</div>
      <div class="opts" data-q="13"></div></div>
  </div>

  <div class="ksdcat">
    <h2>六　更宜加努力的作為<small>指針5、6、7</small></h2>
    <div class="q"><div class="qt"><span class="num">Q14</span>有提升員工顧客應對能力的作為（接待、申訴處理的研修等），或加深對顧客等的理解（消費者心理、身心障礙特性等）的作為。</div>
      <div class="opts" data-q="14"></div></div>
    <div class="q"><div class="qt"><span class="num">Q15</span>已周知員工注意自己對交易對象員工所為的言行，並已考慮在交易對象請求協助確認事實等情形時配合的體制。</div>
      <div class="opts" data-q="15"></div></div>
  </div>

  <div class="btnrow">
    <button type="button" class="go" onclick="ksdScore()">查看診斷結果</button>
    <p class="warn" id="ksdWarn">有尚未回答的題目。請回答所有題目。</p>
  </div>
  </form>

  <div id="ksdResult">
    <div class="score">
      <div style="font-size:.9rem;">法定義務措施（Q1〜Q13）的達成度</div>
      <div class="pct" id="ksdPct"></div>
      <div class="lvl" id="ksdLvl"></div>
      <div class="msg" id="ksdMsg"></div>
    </div>
    <div id="ksdCats"></div>

    <div class="ksdcta">
      關於顧客騷擾對應制度的整備（基本方針、處理手冊、工作規則的整備、研修等），歡迎以中文或日文，寄到<a href="#contact" style="color:var(--ksd-navy); font-weight:700;">下方諮詢欄</a>的電子郵件地址聯繫。
    </div>
  </div>

  <div class="ksdnote">
    <strong>使用上的注意</strong><br>
    ・本診斷是依據勞動施策綜合推進法33條，以及厚生勞動省「關於僱主就職場上因顧客等言行所生問題在僱用管理上應採取之措施等的指針」（令和8年厚生勞動省告示第51號）的內容所製作的一般性資訊提供，並非針對個別案件的法律意見。<br>
    ・診斷結果僅供參考。實際是否已滿足法定的措施義務，須依個別情況判斷。<br>
    ・輸入的內容不會被傳送到伺服器（僅在您的瀏覽器內處理）。
  </div>

</div>
</div>
<a class="back" href="../shindan.html">← 回到診斷工具一覽</a>""",
    js="""(function(){
  var opts=[["已做到",2],["部分做到",1],["尚未做到",0]];
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
  {name:"一 方針的明確化與周知、宣導", qs:[1,2,3], duty:true,
   advice:"以文字明訂並讓員工知悉「對顧客騷擾堅定應對、保護員工」的方針，是措施義務的起點。可以先從在經營者的對外宣示或公司手冊中明文記載，以及整備處理程序（報告路徑、不讓員工單獨應對、錄音錄影、報警標準等）著手。"},
  {name:"二 諮詢制度的建立", qs:[4,5,6], duty:true,
   advice:"設置並周知諮詢窗口是義務的核心。與其他騷擾窗口合併運作或委外處理，也是被允許的。另要求整備給窗口負責人的手冊與研修，以及在是否構成顧客騷擾尚屬微妙的階段也廣泛受理的運作方式。"},
  {name:"三 發生後的迅速、妥適處理", qs:[7,8,9], duty:true,
   advice:"事先決定事實確認的程序（包含確認客觀證據）、對受害員工的照護措施，以及防止再發生的措施，是法律所要求的。若停留在事情發生才臨時應變的狀態，不論在措施義務或保護員工的層面上都有風險。"},
  {name:"四 抑止惡質案例的措施", qs:[10,11], duty:true,
   advice:"事先明確訂定對特別惡質案例的處理方針（報警、警告書、停止提供服務、禁止進入、假處分等），並整備能實際執行的體制，屬於法定義務。不要全交給現場判斷，公司層面應先決定判斷標準與向上呈報的路徑。"},
  {name:"五 隱私保護與禁止不利處遇", qs:[12,13], duty:true,
   advice:"保護諮詢者隱私的措施，以及訂明並周知不因提出諮詢等原因而為不利處遇，都屬於法定義務。這部分往往需要一併檢討修改工作規則或相關規程。"},
  {name:"六 更宜加努力的作為", qs:[14,15], duty:false,
   advice:"提升顧客應對能力的研修，以及在與交易對象的關係上的處理（提醒自家員工注意、配合他公司的協助請求），在指針上屬於努力義務或宜加努力的作為，但對提高實效性很有幫助。"}
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
    lvlEl.textContent='大致已建立'; lvlEl.className='lvl ok';
    msgEl.textContent='法律所要求的措施大致上都已具備。建議定期檢視運作是否流於形式（員工對窗口的認知程度、研修的實施狀況等），並就下列僅達「部分」的項目加以補強。';
  }else if(pct>=60){
    lvlEl.textContent='部分項目不足'; lvlEl.className='lvl mid';
    msgEl.textContent='基本的措施已有，但從措施義務的角度仍有不足的項目。措施義務已經施行。建議參考下列各項結果，逐步補足不足之處。';
  }else{
    lvlEl.textContent='需要建立制度'; lvlEl.className='lvl ng';
    msgEl.textContent='法律所要求的措施多數尚未建立。措施義務自2026年10月1日起已經施行，可能成為行政機關（厚生勞動大臣。部分權限已委任都道府縣勞動局長）建議、指導、勸告的對象；若不遵從勸告，還可能被公布企業名稱（勞動施策綜合推進法42條）。建議先從方針的明文化與設置諮詢窗口著手，盡早開始整備。';
  }

  var html='';
  ksdCatDef.forEach(function(c){
    var got=0, max=c.qs.length*2;
    c.qs.forEach(function(q){got+=vals[q];});
    var p=Math.round(got/max*100);
    var flag, cls;
    if(p>=90){flag='○ 已建立'; cls='ok';}
    else if(p>=50){flag='△ 部分不足'; cls='mid';}
    else {flag='× 需要建立'; cls='ng';}
    html+='<div class="catres"><h3>'+c.name+(c.duty?'':'（努力義務、宜加努力的作為）')+'</h3>'
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
)

# ===== 4 勞資糾紛初期應對指南 =====
SHINDAN_ZH["romu-navi"] = dict(
    title="勞資糾紛初期應對指南",
    tag="從8種類型選擇",
    summary="從8種常見的勞資糾紛類型中選擇，即可了解一般的程序流程，以及初期該做的事與應避免的事。本指南不預測案件的結果。",
    desc="從解僱與不續約、加班費請求、團體協商、勞動審判、勞動基準監督署的調查、騷擾申訴、問題員工、停職與復職等8種類型中選擇，即可了解一般的程序流程與初期應對要點。",
    body="""<div class="lnv">
<div class="wrap">

  <div class="head">
    <h1>勞資糾紛初期應對指南</h1>
    <p>「收到員工一方寄來的書面」「公司內部發生了糾紛」——本指南為在日本經營公司的經營者、人事負責人，整理了常見勞資糾紛各類型的<strong>一般程序流程與初期應對要點</strong>。請選擇符合貴公司狀況的項目。</p>
  </div>

  <div class="lnvlead">
    ※本指南是一般性的資訊提供。實際的處理會因個案情況而有很大差異，個別案件的展望與方針，請提供資料後向律師諮詢確認。
  </div>

  <div class="grid" id="lnvGrid">
    <button data-p="lnvP1">收到爭執解僱或不續約的通知</button>
    <button data-p="lnvP2">收到加班費（未付工資）的請求</button>
    <button data-p="lnvP3">收到工會提出的團體協商要求</button>
    <button data-p="lnvP4">被聲請勞動審判</button>
    <button data-p="lnvP5">受到勞動基準監督署的調查或改善勸告</button>
    <button data-p="lnvP6">公司內部有騷擾的申訴</button>
    <button data-p="lnvP7">正在考慮如何處理有問題行為的員工</button>
    <button data-p="lnvP8">心理健康不佳員工的處理（停職、復職）</button>
  </div>

  <!-- 1 解僱・不續約 -->
  <div class="panel" id="lnvP1">
    <h2>收到爭執解僱或不續約的通知時</h2>
    <div class="sec"><h3>一般的經過</h3>
      <div class="flow"><span>本人或其律師寄來的通知書</span><i>→</i><span>協商</span><i>→</i><span>調解、勞動審判或訴訟</span><i>→</i><span>和解或判決等</span></div>
      <p style="margin-top:8px;">有在協商階段即告解決的案件，也有進入勞動審判或訴訟的案件。</p></div>
    <div class="sec"><h3>初期應對要點</h3><ul>
      <li>把導致解僱的經過資料（指導紀錄、警告書、會議紀錄、工作規則、解僱通知書與理由書）依時間順序整理。</li>
      <li>事後追加解僱理由可能受到限制，因此理由的整理要慎重進行。</li>
      <li>即使對方設有回覆期限，也不要急著做出欠缺考慮的回覆。回覆的內容可能在後續程序中成為證據。</li>
      <li class="caution">避免對本人或其律師作情緒性反應，也避免在社群媒體等處提及。</li></ul></div>
    <div class="sec"><h3>值得先了解的法律架構</h3>
      <p>解僱如果客觀上缺乏合理的理由，依社會通念也不被認為妥當，會因權利濫用而無效（勞動契約法16條）。解僱一旦被認定無效，除了須讓員工復職，解僱期間的工資支付（即所謂的回溯工資）也會成為問題，因此爭訟期間越長，金錢上的負擔可能越大。</p></div>
  </div>

  <!-- 2 加班費 -->
  <div class="panel" id="lnvP2">
    <h2>收到加班費（未付工資）的請求時</h2>
    <div class="sec"><h3>一般的經過</h3>
      <div class="flow"><span>請求書面（存證信函等）</span><i>→</i><span>要求提供資料（出勤卡等）</span><i>→</i><span>協商</span><i>→</i><span>勞動審判或訴訟</span></div></div>
    <div class="sec"><h3>初期應對要點</h3><ul>
      <li>保全工作時間的紀錄（出勤卡、差勤系統、電腦紀錄、工作日報等）與工資規程、僱用契約書。</li>
      <li>及早檢查公司計算加班費的方式（固定加班費、管理監督者、變形工作時間制、按件計酬等）有無弱點。制度若不符合法定要件，金額可能遠高於預期。</li>
      <li>如果公司還有其他工作型態相同的員工，要把影響擴及其他員工的可能性也納入考量再定方針。</li>
      <li class="caution">絕對不要銷毀或變更紀錄。</li></ul></div>
    <div class="sec"><h3>值得先了解的法律架構</h3>
      <p>工資請求權的消滅時效為5年，但在目前的過渡期間暫定為3年（退職金為5年。勞動基準法115條、143條）。此外，在訴訟中可能被命令支付與未付金額同額以內的附加金（同法114條）。對象期間會隨時間經過而移動，因此也需要把時效管理納入應對。</p></div>
  </div>

  <!-- 3 團體協商 -->
  <div class="panel" id="lnvP3">
    <h2>收到工會提出的團體協商要求時</h2>
    <div class="sec"><h3>一般的經過</h3>
      <div class="flow"><span>團體協商要求書</span><i>→</i><span>日期、地點等的協調</span><i>→</i><span>團體協商（有時會進行數次）</span><i>→</i><span>達成協議或進入勞動委員會的程序等</span></div></div>
    <div class="sec"><h3>初期應對要點</h3><ul>
      <li>確認要求書所載的要求事項與回覆期限，並在期限內聯繫對方，表達願意進行協商的態度（條件面的協調可以在此之後進行）。</li>
      <li>協商的日期、地點、出席者與時間，公司一方也可以提出對案來協調。使用外部會議室的例子也不少。</li>
      <li>先整理與要求事項相關的事實關係與資料，並決定出席者的分工，再進行協商。</li>
      <li class="caution">不要因為員工加入工會而給予不利處遇，也不要勸誘員工退出工會。</li></ul></div>
    <div class="sec"><h3>值得先了解的法律架構</h3>
      <p>無正當理由拒絕團體協商，構成不當勞動行為（工會法7條2款）。公司有誠實進行團體協商的義務，但並沒有必須照單全收對方要求的義務。重要的是盡力說明與協議的過程。</p></div>
  </div>

  <!-- 4 勞動審判 -->
  <div class="panel" id="lnvP4">
    <h2>被聲請勞動審判時</h2>
    <div class="sec"><h3>一般的經過</h3>
      <div class="flow"><span>聲請書送達</span><i>→</i><span>提出答辯書</span><i>→</i><span>第1次期日</span><i>→</i><span>調解成立或作出勞動審判</span><i>→</i><span>（有異議時）移審為訴訟</span></div></div>
    <div class="sec"><h3>初期應對要點</h3><ul>
      <li class="caution">到答辯書提出期限的準備時間很短，收到聲請書後要立刻開始行動。</li>
      <li>一般認為勞動審判在第1次期日就會大幅形成審判委員會的心證，因此必須在答辯書階段就把主張與證據提出完整。</li>
      <li>可以考慮讓能直接說明情況的人員（當時的主管等）出席期日。</li>
      <li>以解決金達成調解也是重要選項之一，建議及早在公司內部研議可以接受的解決水準。</li></ul></div>
    <div class="sec"><h3>值得先了解的法律架構</h3>
      <p>勞動審判程序除有特別情事外，必須在3次以內的期日終結審理（勞動審判法15條2項）。由於是在短期間集中審理，初期準備往往會直接影響結果。</p></div>
  </div>

  <!-- 5 勞基署 -->
  <div class="panel" id="lnvP5">
    <h2>受到勞動基準監督署的調查或改善勸告時</h2>
    <div class="sec"><h3>一般的經過</h3>
      <div class="flow"><span>調查通知或臨場檢查</span><i>→</i><span>提交資料、接受詢問</span><i>→</i><span>交付改善勸告書、指導票</span><i>→</i><span>提出改善報告書</span></div></div>
    <div class="sec"><h3>初期應對要點</h3><ul>
      <li>整理被要求的資料（勞動條件通知書、工資帳簿、出勤簿、36協定等），並誠實應對。</li>
      <li>確認改善勸告書所載的違反事項與報告期限，並擬定符合實際狀況的改善計畫。</li>
      <li>若被指出須回溯支付未付工資，釐清對象人員的範圍與期間就相當重要。</li>
      <li class="caution">虛偽報告或變更資料本身就會成為重大問題，絕對不要為之。</li></ul></div>
    <div class="sec"><h3>值得先了解的法律架構</h3>
      <p>改善勸告本身屬於行政指導，但若置之不理或作虛偽的應對，有可能招致移送檢察機關等更嚴重的後果。從防止再發生的角度，追溯到被指出事項的根本原因（工作時間管理或工資制度的問題）加以改善，相當重要。</p></div>
  </div>

  <!-- 6 騷擾申訴 -->
  <div class="panel" id="lnvP6">
    <h2>公司內部有騷擾的申訴時</h2>
    <div class="sec"><h3>一般的經過</h3>
      <div class="flow"><span>諮詢、申訴</span><i>→</i><span>事實關係的調查（訪談雙方與第三人）</span><i>→</i><span>認定與判斷</span><i>→</i><span>對受害者的照護措施與對行為人的措施</span><i>→</i><span>防止再發生的對策</span></div></div>
    <div class="sec"><h3>初期應對要點</h3><ul>
      <li>在確認諮詢者意願的同時，迅速著手事實確認（向諮詢者與被指為行為人的一方雙方，必要時並向第三人訪談）。</li>
      <li>留下訪談紀錄，並與客觀資料（電子郵件、通訊軟體訊息、錄音等）相互對照後再作判斷。</li>
      <li>調查期間注意雙方的接觸與隱私（不要用「先觀察看看」草率帶過）。</li>
      <li class="caution">因員工提出諮詢而給予不利處遇，是法律所禁止的。</li>
      <li>若要作懲戒處分，須慎重檢討工作規則上的依據與程序，以及處分輕重是否相當（勞動契約法15條）。</li></ul></div>
    <div class="sec"><h3>值得先了解的法律架構</h3>
      <p>關於職場霸凌、性騷擾，以及與懷孕生產、育兒照護等相關的騷擾，法律課予僱主整備諮詢制度、事後迅速妥適處理等措施義務。處理失當時，責任不僅止於行為人，公司本身也可能被追究責任（損害賠償等）。</p></div>
  </div>

  <!-- 7 問題員工 -->
  <div class="panel" id="lnvP7">
    <h2>正在考慮如何處理有問題行為的員工時</h2>
    <div class="sec"><h3>一般的經過</h3>
      <div class="flow"><span>告誡、指導（並作成紀錄）</span><i>→</i><span>以書面指導並給予改善機會</span><i>→</i><span>檢討調職、懲戒處分等</span><i>→</i><span>勸退與解僱是最後手段</span></div></div>
    <div class="sec"><h3>初期應對要點</h3><ul>
      <li>把問題行為具體記錄到「何時、何處、發生什麼事」的程度（僅以抽象的「工作態度不良」並不足夠）。</li>
      <li>告誡與指導不要只用口頭，也以書面或電子郵件進行，留下已給予改善機會的證據。</li>
      <li>未經階段性處理就突然解僱，被認定無效的風險很高。</li>
      <li class="caution">以逼使員工離職為目的而排除其工作、過度斥責，本身就可能被評價為騷擾或違法行為。</li></ul></div>
    <div class="sec"><h3>值得先了解的法律架構</h3>
      <p>懲戒處分與解僱，如果沒有客觀上合理的理由與社會通念上的相當性，都會因權利濫用而無效（勞動契約法15條、16條）。其有效性是從「問題行為的內容與程度」和「公司所踏過的程序」兩個面向判斷，因此日常的紀錄與階段性的處理會左右結論。</p></div>
  </div>

  <!-- 8 停職・復職 -->
  <div class="panel" id="lnvP8">
    <h2>心理健康不佳員工的處理（停職、復職）時</h2>
    <div class="sec"><h3>一般的經過</h3>
      <div class="flow"><span>掌握狀況、建議就醫</span><i>→</i><span>發布停職</span><i>→</i><span>療養與確認經過</span><i>→</i><span>判斷能否復職（主治醫師、職場醫師）</span><i>→</i><span>復職支援或停職期間屆滿的處理</span></div></div>
    <div class="sec"><h3>初期應對要點</h3><ul>
      <li>確認工作規則中的停職制度（停職期間、復職的要件、期間屆滿時的處理）。規定含糊不清就逕行運作，事後容易發生爭議。</li>
      <li>發布停職時，以書面向本人說明停職期間、復職的程序，以及期間屆滿時的處理。</li>
      <li>能否復職不要只憑主治醫師的診斷書決定，也要參酌職場醫師的意見與業務的實際狀況。主治醫師與公司判斷不一致的場面，很容易演變成爭議。</li>
      <li class="caution">不要把健康不佳員工的處理全部交給現場（主管欠缺考慮的言行，容易衍生出第二層的爭議）。</li></ul></div>
    <div class="sec"><h3>值得先了解的法律架構</h3>
      <p>公司應為必要的照顧，使員工能在確保生命、身體等安全的狀態下工作（勞動契約法5條）。處理心理健康不佳的案件，除了停職與復職的程序面，也必須從這項安全照護的角度一併檢討。</p></div>
  </div>

  <div class="lnvcta" id="lnvCta" style="display:none;">
    個別案件的展望與處理方針，需要在看過資料後才能檢討。關於勞資糾紛的處理，歡迎以中文或日文，寄到<a href="#contact" style="color:var(--lnv-main); font-weight:700;">下方諮詢欄</a>的電子郵件地址聯繫。
  </div>

  <div class="lnvnote">
    <strong>使用上的注意</strong><br>
    ・本指南是一般性的資訊提供，並非針對個別案件的法律意見。所記載的流程與要點不適用的案件也很多。<br>
    ・本指南不預測也不保證糾紛的結果。個別案件的展望，需要依具體的資料與事實關係加以檢討。<br>
    ・選擇的內容不會被傳送到伺服器（僅在您的瀏覽器內處理）。
  </div>

</div>
</div>
<a class="back" href="../shindan.html">← 回到診斷工具一覽</a>""",
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
)

# 一覧ページの見出し・リード文（繁体字）
SHINDAN_ZH_INDEX = dict(
    title="診斷工具",
    desc="可自行檢視職場騷擾防治、顧客騷擾對應、公益通報對應制度的整備狀況的診斷工具，以及勞資糾紛的類型別初期應對指南。輸入內容不會被傳送。",
    lead1="這是讓經營者與人事負責人，自行確認日本法律上課予義務的公司內部制度現狀的工具。回答設問後，會顯示不足的項目與接下來應著手的事項。",
    lead2="輸入的內容不會被傳送到伺服器（僅在您的瀏覽器內處理）。診斷結果僅供參考，並非針對個別案件的法律意見。",
)
