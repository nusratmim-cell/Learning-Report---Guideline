import base64, os
BASE="/home/shikho/shareable report card"
LOGO=open("/home/shikho/Desktop/Laptop Backup/Brac-Teacher-Demo-main (3)/Brac-Teacher-Demo-main/public/shikho-logo.svg",encoding="utf-8").read().strip()
def b64(p): return base64.b64encode(open(os.path.join(BASE,p),'rb').read()).decode()
vid="data:video/mp4;base64,"+b64("email-assets/walkthrough.mp4")
imgs={k:"data:image/png;base64,"+b64("email-assets/"+v) for k,v in {
 "result":"01-result-page.png","subject":"02-subject-page.png","chapter":"03-chapter-page.png",
 "study":"04-study-page.png","leader":"05-leaderboard.png"}.items()}

CSS="""
:root{color-scheme:light;--ground:#F7F6F2;--paper:#fff;--ink:#1A1D26;--ink2:#474D5C;--ink3:#7C8090;
--line:#E6E3DB;--line2:#F0EEE8;--navy:#355DAB;--navy2:#2D4797;--navy-soft:#EDF1FB;
--mag:#E2008D;--mag-soft:#FCEBF5;--orange:#FAA700;--red:#FF1C5A;
--amber-bg:#FBF2D7;--amber-fg:#8A5D04;--good:#2C7A4B;--warn:#9A6A06;--bad:#B8304B;
--sans:"Inter","Hind Siliguri",system-ui,sans-serif;--bn:"Hind Siliguri","Inter",system-ui,sans-serif;
--shadow:0 2px 6px rgba(28,34,66,.06),0 1px 2px rgba(28,34,66,.04);--shadow-lg:0 14px 34px rgba(28,34,66,.10);}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);font-size:17px;line-height:1.72;-webkit-font-smoothing:antialiased}
.accentbar{height:5px;background:linear-gradient(90deg,var(--navy),var(--mag) 55%,var(--orange))}
.wrap{max-width:760px;margin:0 auto;padding:0 20px 72px}
h1,h2,h3{line-height:1.26;margin:0}
p{margin:0 0 12px}
.bn{font-family:var(--bn)}
.topbar{border-bottom:1px solid var(--line);background:#fff}
.topbar .in{max-width:760px;margin:0 auto;padding:9px 20px;display:flex;align-items:center;justify-content:space-between;gap:12px}
.topbar .in .l{display:flex;align-items:center;gap:11px}
.topbar .in .l svg{height:26px;width:auto;display:block}
.topbar .in .tag{font-size:.7rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--navy2);background:var(--navy-soft);border:1px solid #D7DFF6;border-radius:999px;padding:5px 12px;white-space:nowrap}
header.top{background:linear-gradient(160deg,#FFFFFF,#EFF2FC);border:1px solid var(--line);border-radius:18px;padding:22px 24px;margin-top:22px;box-shadow:var(--shadow)}
header .eyebrow{font-size:.72rem;font-weight:800;letter-spacing:.11em;text-transform:uppercase;color:var(--mag)}
header h1{font-size:1.8rem;color:var(--navy2);margin:8px 0 0;font-weight:800;letter-spacing:-.01em}
header .uline{width:58px;height:4px;border-radius:3px;background:linear-gradient(90deg,var(--navy),var(--mag));margin:10px 0 12px}
header .sub{color:var(--ink2);font-size:1rem}

/* ---- visual-first hero: the walkthrough leads the page ---- */
.hero{margin-top:18px;background:linear-gradient(160deg,#10203F,#243E78);border-radius:22px;padding:24px 20px 26px;box-shadow:var(--shadow-lg);display:flex;flex-direction:column;align-items:center;text-align:center}
.hero .eyebrow{font-size:.72rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#FF69C2;margin-bottom:4px}
.hero h2{color:#fff;font-size:1.22rem;font-weight:800;margin:0 0 16px}
.hero .frame{position:relative;width:100%;max-width:290px}
.hero video{width:100%;display:block;border-radius:24px;border:3px solid rgba(255,255,255,.14);background:#000;box-shadow:0 20px 50px rgba(0,0,0,.45)}
.hero .cap{color:#C9D4EE;font-size:.92rem;margin-top:16px;max-width:420px}

.gallery-intro{color:var(--ink2);font-size:1rem}
section{margin-top:44px}
section>h2{display:flex;align-items:center;gap:14px;font-size:1.3rem;color:var(--navy2);font-weight:800;margin-bottom:8px}
section>h2 .n{flex:0 0 auto;width:34px;height:34px;border-radius:10px;display:grid;place-items:center;
background:linear-gradient(145deg,var(--navy),var(--mag));color:#fff;font-size:.9rem;font-weight:800;box-shadow:var(--shadow)}
section>.lead{color:var(--ink2);margin:0 0 14px;padding-left:48px}
h3.lbl{font-size:1.03rem;color:var(--ink);margin:18px 0 4px;font-weight:700}
ul,ol{margin:6px 0 14px;padding-left:22px}li{margin:5px 0}
.say{background:var(--mag-soft);border-left:3px solid var(--mag);border-radius:0 12px 12px 0;padding:13px 16px;margin:12px 0 4px}
.say .t{font-size:.7rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--mag);margin-bottom:5px}
.say p{margin:0;color:#7d1552;font-family:var(--bn)}
.note{background:var(--amber-bg);border-left:3px solid var(--orange);border-radius:0 12px 12px 0;padding:13px 16px;margin:14px 0;color:var(--amber-fg);font-size:.98rem}
.note b{font-weight:700}
.callout{background:var(--navy-soft);border:1px solid #D7DFF6;border-left:4px solid var(--mag);border-radius:0 12px 12px 0;padding:13px 16px;margin:14px 0 4px;color:var(--navy2);font-size:1.02rem;font-weight:600}
.callout b{color:var(--mag);font-weight:800}
.chips{display:flex;flex-wrap:wrap;gap:9px;margin:4px 0 2px}
.chip{background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:8px 14px;font-size:.95rem;color:var(--ink);box-shadow:var(--shadow);font-family:var(--bn);display:flex;align-items:center;gap:8px}
.chip .d{width:8px;height:8px;border-radius:50%;flex:0 0 auto}
.flow{display:flex;flex-direction:column;align-items:center;margin:14px 0 4px}
.fbox{width:100%;max-width:450px;background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:12px 16px;box-shadow:var(--shadow);display:flex;align-items:center;gap:12px;font-size:1rem;color:var(--ink)}
.fbox .fn{flex:0 0 auto;width:27px;height:27px;border-radius:50%;background:var(--navy-soft);color:var(--navy2);font-weight:800;font-size:.86rem;display:grid;place-items:center;font-family:var(--sans)}
.fbox.wa{border:1px solid #27C76A;border-left:4px solid #25D366}
.fbox.sms{border:1px solid #C7D2F2;border-left:4px solid var(--navy)}
.farrow{color:var(--ink3);font-size:1.35rem;line-height:1;padding:6px 0;display:flex;flex-direction:column;align-items:center;gap:3px}
.farrow .albl{font-size:.8rem;color:var(--mag);font-weight:700;font-family:var(--bn)}
.tabs{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin:10px 0 6px}
.tab{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:14px 12px;text-align:center;box-shadow:var(--shadow);position:relative;overflow:hidden}
.tab::before{content:"";position:absolute;top:0;left:0;right:0;height:4px}
.tab.t1::before{background:var(--navy)}.tab.t2::before{background:var(--good)}.tab.t3::before{background:var(--orange)}
.tab .tt{font-weight:800;color:var(--navy2);font-family:var(--bn);margin-top:2px}
.tab .td{font-size:.82rem;color:var(--ink3);font-family:var(--bn);margin-top:2px}

/* ---- screen cards: image is the hero, text is a short caption ---- */
.screen{display:grid;grid-template-columns:240px 1fr;gap:26px;align-items:center;background:var(--paper);border:1px solid var(--line);border-radius:20px;padding:22px;margin:16px 0;box-shadow:var(--shadow)}
.shot{position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--line);box-shadow:var(--shadow-lg);background:#fff}
.shot img{width:100%;height:360px;object-fit:cover;object-position:top center;display:block}
.shot::after{content:"";position:absolute;left:0;right:0;bottom:0;height:60px;background:linear-gradient(rgba(255,255,255,0),#fff);pointer-events:none}
.screen .bd h3{font-size:1.14rem;color:var(--navy2);margin-bottom:10px;font-weight:800}
.screen .bd ul{margin:0;padding-left:0;list-style:none}
.screen .bd li{position:relative;padding-left:24px;margin:9px 0;color:var(--ink2);font-size:1rem}
.screen .bd li::before{content:"";position:absolute;left:0;top:9px;width:9px;height:9px;border-radius:3px;background:linear-gradient(145deg,var(--navy),var(--mag))}
.screen .bd li b{color:var(--ink);font-weight:700}
.step{background:var(--paper);border:1px solid var(--line);border-left:3px solid var(--navy);border-radius:0 12px 12px 0;padding:12px 16px;margin:10px 0;box-shadow:var(--shadow)}
.step .sh{font-weight:800;color:var(--navy2)}
.sit{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin:14px 0;box-shadow:var(--shadow)}
.sit h3{font-size:1.06rem;color:var(--ink);font-weight:800;margin-bottom:8px}
.qa{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:14px 18px;margin:10px 0;box-shadow:var(--shadow)}
.qa .q{font-weight:800;color:var(--navy2);font-family:var(--bn);margin-bottom:4px}
.qa .a{color:var(--ink2);font-family:var(--bn)}
footer{margin-top:48px;color:var(--ink3);font-size:.86rem;text-align:center;font-family:var(--bn)}
@media(max-width:620px){body{font-size:16px}.screen{grid-template-columns:1fr;gap:16px}.shot{max-width:280px;margin:0 auto}.shot img{height:340px}.tabs{grid-template-columns:1fr}section>.lead{padding-left:0}}
"""

def screen(img,title,items):
    lis="".join("<li>%s</li>"%i for i in items)
    return f'<div class="screen"><div class="shot"><img src="{img}" alt="{title}"></div><div class="bd"><h3 class="bn">{title}</h3><ul class="bn">{lis}</ul></div></div>'

BODY=f"""
<div class="accentbar"></div>
<div class="topbar"><div class="in"><span class="l">{LOGO}</span><span class="tag">Internal · Guideline</span></div></div>
<div class="wrap">
<header class="top">
  <div class="eyebrow">Customer Care · Guideline</div>
  <h1>Shikho Learning Report</h1>
  <div class="uline"></div>
  <div class="sub bn">আগে ভিডিওতে রিপোর্টটা একবার দেখে নিন — তারপর নিচের screen ও প্রশ্নোত্তর।</div>
</header>

<div class="hero">
  <div class="eyebrow">৬০ সেকেন্ডের ওয়াকথ্রু</div>
  <h2 class="bn">পুরো Learning Report একবারে</h2>
  <div class="frame"><video controls muted playsinline preload="metadata"><source src="{vid}" type="video/mp4"></video></div>
  <div class="cap bn">Guardian-কে বোঝানোর আগে এই ভিডিওটা দেখে নিলেই পুরো রিপোর্টের ধারণা হয়ে যাবে।</div>
</div>

<section>
  <h2><span class="n">01</span><span class="bn">কোন Screen-এ কী দেখায়</span></h2>
  <p class="lead bn">প্রতিটি screen-এ মূল যে জিনিসগুলো থাকে — Guardian-কে দেখিয়ে বোঝানোর জন্য।</p>
  {screen(imgs['result'],"রেজাল্ট — Overall Score",["<b>সার্বিক স্কোর ও ব্যান্ড</b> — আগের মাসের তুলনা সহ","<b>বিষয়ভিত্তিক স্কোর</b> — রঙ দিয়ে ভালো / দুর্বল","নিয়মিততা, শিক্ষকের নোট ও সেরা অর্জন"])}
  {screen(imgs['subject'],"Subject — বিষয়ে চাপ দিলে",["<b>গড় স্কোর</b> ও এই বিষয়ে র‍্যাঙ্ক","ক্লাস কমপ্লিশন ও এক্সাম স্কোর","<b>চ্যাপ্টার পারফরম্যান্স</b> — দুর্বল / মডারেট / ভালো"])}
  {screen(imgs['chapter'],"Chapter — চ্যাপ্টারে চাপ দিলে",["<b>এক্সাম স্কোর</b>, র‍্যাঙ্ক ও গ্রেড","ক্লাস ও এক্সামের হিসাব","<b>সংশ্লিষ্ট ভিডিও ও Lesson</b> — আবার দেখে Practice"])}
  {screen(imgs['study'],"পড়াশোনা — Class ও Activity",["<b>লাইভ ক্লাস</b> — কত করেছে, মিস করেছে","<b>Calendar</b> — দিন ধরে রঙে অ্যাটেন্ডেন্স","চ্যাপ্টার এক্সাম ও লার্নিং এক্টিভিটি"])}
  {screen(imgs['leader'],"লিডারবোর্ড — Rank",["সেরা তিনজন (Medal সহ)","র‍্যাঙ্ক তালিকা","<b>নিজের সন্তানের র‍্যাঙ্ক</b> ও মোট শিক্ষার্থী"])}
</section>

<section>
  <h2><span class="n">02</span><span class="bn">Report-এ কী আছে</span></h2>
  <p class="lead bn">মূলত ৩টি Tab —</p>
  <div class="tabs">
    <div class="tab t1"><div class="tt">রেজাল্ট</div><div class="td">Score ও বিষয়</div></div>
    <div class="tab t2"><div class="tt">পড়াশোনা</div><div class="td">Class ও Activity</div></div>
    <div class="tab t3"><div class="tt">লিডারবোর্ড</div><div class="td">Rank</div></div>
  </div>
  <h3 class="lbl bn">Score-এর রঙ</h3>
  <div class="chips">
    <span class="chip"><span class="d" style="background:#2C7A4B"></span>সবুজ — ভালো করছে</span>
    <span class="chip"><span class="d" style="background:#E0A800"></span>হলুদ — আরও সুযোগ আছে</span>
    <span class="chip"><span class="d" style="background:#D5415E"></span>লাল — Practice দরকার</span>
  </div>
  <div class="callout bn"><b>App বা Login লাগে না।</b> Report Link-এ চাপ দিলেই খোলে।</div>
</section>

<section>
  <h2><span class="n">03</span><span class="bn">Link কীভাবে পাঠাবেন</span></h2>
  <p class="lead bn"><b>Paid:</b> প্রতি মাসে Automatic SMS যায়।&nbsp; <b>Trial / Free:</b> CRM থেকে হাতে পাঠাতে হয় —</p>
  <div class="flow bn">
    <div class="fbox"><span class="fn">1</span>CRM-এ <b>Lead Details</b> খুলুন</div>
    <div class="farrow">↓</div>
    <div class="fbox"><span class="fn">2</span><b>“Share Report Card”</b> নির্বাচন করুন</div>
    <div class="farrow">↓</div>
    <div class="fbox wa"><span class="fn">3</span><b>WhatsApp</b>-এ Link পাঠান</div>
    <div class="farrow"><span class="albl">WhatsApp না থাকলে</span>↓</div>
    <div class="fbox sms"><span class="fn">4</span><b>SMS</b>-এ Link পাঠান</div>
  </div>
</section>

<section>
  <h2><span class="n">04</span><span class="bn">সমস্যা হলে কী বলবেন</span></h2>
  <div class="sit"><h3 class="bn">Report / Link পাওয়া যাচ্ছে না</h3>
    <div class="say"><div class="t">বলতে পারেন</div><p>"আপনার সন্তানের Report-এর Link-টা WhatsApp-এ আবার পাঠিয়ে দিচ্ছি। একটু দেখবেন পেয়েছেন কি না? Link-এ চাপ দিলেই Report খুলে যাবে।"</p></div></div>
  <div class="sit"><h3 class="bn">Link খুলছে না</h3>
    <div class="say"><div class="t">বলতে পারেন</div><p>"একবার Internet Connection-টা দেখবেন? আমি Link-টা আবার পাঠাচ্ছি। না খুললে Chrome-এ চেষ্টা করুন। এরপরও সমস্যা হলে বিষয়টা আমরা চেক করে দেখব।"</p></div></div>
  <div class="sit"><h3 class="bn">Score বুঝতে সমস্যা হচ্ছে</h3>
    <div class="say"><div class="t">বলতে পারেন</div><p>"গত মাসে Class আর Exam-এ কেমন করেছে, সেটার ভিত্তিতে Overall Score দেখানো হচ্ছে। Score-এর পাশে 'কীভাবে নির্ধারিত হয়' আছে, ওখানে চাপ দিলে বিস্তারিত পাবেন।"</p></div></div>
  <div class="sit"><h3 class="bn">কিছু জায়গায় তথ্য নেই (--)</h3>
    <div class="say"><div class="t">বলতে পারেন</div><p>"গত মাসে ওই Activity-র তথ্য না থাকলে এখানে কিছু দেখাবে না। তবে Activity থাকার পরও না দেখালে বিষয়টা আমরা চেক করে দেখব।"</p></div></div>
</section>

<section>
  <h2><span class="n">05</span><span class="bn">সাধারণ জিজ্ঞাসা (FAQ)</span></h2>
  <div class="qa"><div class="q">Report কি শুধু Paid Student-দের জন্য?</div><div class="a">না। Paid, Trial ও Free — সবার Report দেখা যাবে, শুধু Link পাওয়ার নিয়ম আলাদা।</div></div>
  <div class="qa"><div class="q">Report দেখতে App লাগবে?</div><div class="a">না। শুধু Report Link থাকলেই Browser থেকে দেখা যাবে।</div></div>
  <div class="qa"><div class="q">Score কম কেন?</div><div class="a">গত মাসের Class ও Exam অনুযায়ী Score তৈরি হয়। কোন Subject বা Chapter-এ কম, সেটা Report-এ দেখা যায়।</div></div>
  <div class="qa"><div class="q">Attendance কীভাবে হিসাব হয়?</div><div class="a">গত মাসের মোট Live Class-এর মধ্যে কতগুলো Attend করেছে, সেই অনুযায়ী।</div></div>
  <div class="qa"><div class="q">Rank কীভাবে হয়?</div><div class="a">একই Program বা Batch-এর অন্য শিক্ষার্থীর সঙ্গে তুলনা করে।</div></div>
  <div class="qa"><div class="q">Report কি অন্য কেউ দেখতে পারবে?</div><div class="a">যার কাছে Link থাকবে সে দেখতে পারবে। তাই Link Share না করাই ভালো।</div></div>
</section>

<section>
  <h2><span class="n">06</span><span class="bn">সমস্যায় যা তথ্য লাগবে</span></h2>
  <div class="chips">
    <span class="chip">Student-এর নাম ও Class</span>
    <span class="chip">Registered Phone</span>
    <span class="chip">কোন Screen-এ সমস্যা</span>
    <span class="chip">কী দেখার কথা, কী দেখাচ্ছে</span>
    <span class="chip">Screenshot</span>
    <span class="chip">কখন থেকে হচ্ছে</span>
  </div>
</section>

<footer>Shikho Learning Report · Guideline · Internal</footer>
</div>
"""
HTML=f"""<!doctype html><html lang="bn"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Shikho Learning Report Guideline</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Hind+Siliguri:wght@400;500;600;700&display=swap">
<style>{CSS}</style></head><body>{BODY}</body></html>"""
out=os.path.join(BASE,"Learning Report - Care Team Guide.html")
open(out,"w",encoding="utf-8").write(HTML)
print("written %.2f MB -> %s"%(len(HTML.encode())/1e6,out))
