import base64, os
BASE="/home/shikho/shareable report card"
LOGO=open("/home/shikho/Desktop/Laptop Backup/Brac-Teacher-Demo-main (3)/Brac-Teacher-Demo-main/public/shikho-logo.svg",encoding="utf-8").read().strip()
def b64(p): return base64.b64encode(open(os.path.join(BASE,p),'rb').read()).decode()
imgs={k:"data:image/png;base64,"+b64("email-assets/"+v) for k,v in {
 "result":"01-result-page.png","subject":"02-subject-page.png","study":"04-study-page.png","leader":"05-leaderboard.png"}.items()}

def to_bn(n): return str(n).translate(str.maketrans("0123456789","০১২৩৪৫৬৭৮৯"))

CSS="""
:root{color-scheme:light;
--ground:#F6F5F1;--paper:#fff;--ink:#1D2433;--muted:#5B6475;--faint:#8A91A1;
--line:#DDE0E7;--line2:#EDEEF2;--indigo:#4353CA;--indigo2:#333FA3;--indigo-s:#ECEEFB;
--ring:#E8336D;--amber-bg:#FFF8E8;--amber-br:#E7B44C;--amber-fg:#8A5D04;--good:#2C9A5C;
--disp:"Baloo Da 2","Hind Siliguri",system-ui,sans-serif;--bn:"Hind Siliguri","Inter",system-ui,sans-serif;}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--ground);color:var(--ink);font-family:var(--bn);font-size:16.5px;line-height:1.62;-webkit-font-smoothing:antialiased}
.accentbar{height:5px;background:linear-gradient(90deg,var(--indigo),#6A5AE0 55%,var(--ring))}
.topbar{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:20}
.topbar .in{max-width:1000px;margin:0 auto;padding:10px 22px;display:flex;align-items:center;justify-content:space-between;gap:12px}
.topbar svg.logo{height:26px;width:auto;display:block}
.topbar .tag{font-size:.68rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--indigo2);background:var(--indigo-s);border:1px solid #CFD4F3;border-radius:999px;padding:5px 12px;white-space:nowrap}
.wrap{max-width:1000px;margin:0 auto;padding:26px 22px 90px}
h1,h2,h3{font-family:var(--disp);font-weight:700;line-height:1.2}
.disp{font-family:var(--disp)}

/* intro */
.intro{display:grid;grid-template-columns:1fr 300px;gap:34px;align-items:start;background:var(--paper);border:1px solid var(--line);border-radius:22px;padding:30px;box-shadow:0 2px 10px rgba(24,30,60,.05)}
.intro h1{font-size:2rem;color:var(--ink);letter-spacing:-.01em}
.intro .sub{color:var(--muted);font-size:1.05rem;margin-top:4px}
.intro h2{font-size:1.16rem;margin:22px 0 8px;color:var(--indigo2);display:flex;align-items:center;gap:9px}
.intro h2 .b{width:8px;height:20px;border-radius:4px;background:var(--indigo)}
.intro ul{list-style:none;display:flex;flex-direction:column;gap:7px}
.intro li{position:relative;padding-left:26px;color:var(--ink)}
.intro li::before{content:"";position:absolute;left:4px;top:10px;width:8px;height:8px;border-radius:50%;background:var(--indigo)}
.intro p{color:var(--ink)}
.note{margin-top:20px;border:1px solid var(--amber-br);background:var(--amber-bg);border-radius:12px;padding:12px 15px;color:var(--amber-fg);font-size:.97rem}
.note b{font-weight:700}
.cover{position:sticky;top:78px}
.coverphone{border:1px solid #C9CCD5;border-radius:26px;padding:10px;background:#fff;box-shadow:0 16px 40px rgba(24,30,60,.12)}
.coverphone .cwin{height:360px;overflow:hidden;border-radius:18px;border:1px solid var(--line)}
.coverphone img{width:100%;display:block}
.cover .cap{text-align:center;color:var(--muted);font-size:.9rem;margin-top:10px}

/* send sub-box */
.send{margin-top:18px;border:1px solid var(--line);border-radius:14px;padding:14px 16px;background:#FAFAFC}
.send .sh{font-weight:700;font-family:var(--disp);color:var(--ink);margin-bottom:9px;display:flex;align-items:center;gap:8px}
.send .sh .pb{font-size:.62rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:#fff;background:var(--indigo);border-radius:999px;padding:3px 8px}
.flow{display:flex;flex-wrap:wrap;align-items:center;gap:8px}
.fstep{display:flex;align-items:center;gap:8px;background:#fff;border:1px solid var(--line);border-radius:10px;padding:7px 11px;font-size:.93rem}
.fstep .n{width:20px;height:20px;border-radius:50%;background:var(--indigo-s);color:var(--indigo2);font-weight:800;font-size:.76rem;display:grid;place-items:center}
.fstep.wa{border-color:#2BB673}.fstep.sms{border-color:#B9C8EC}
.farr{color:var(--faint);font-weight:800}

/* TOC */
.toc{margin-top:40px}
.toc .th{font-family:var(--disp);font-size:1.3rem;font-weight:700;margin-bottom:4px}
.toc .ts{color:var(--muted);margin-bottom:16px}
.tgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.tc{display:flex;align-items:center;gap:13px;text-decoration:none;color:var(--ink);background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:15px 16px;box-shadow:0 2px 8px rgba(24,30,60,.05);transition:border-color .15s,transform .15s}
.tc:hover{border-color:var(--indigo);transform:translateY(-2px)}
.tc .num{flex:0 0 auto;width:36px;height:36px;border-radius:11px;background:var(--indigo);color:#fff;font-family:var(--disp);font-weight:700;font-size:1.05rem;display:grid;place-items:center}
.tc b{font-family:var(--disp);font-weight:700;font-size:1.02rem;display:block}
.tc span{color:var(--muted);font-size:.86rem}

/* screen sections */
.screen{margin-top:48px;scroll-margin-top:76px}
.shd{display:flex;align-items:center;gap:14px;margin-bottom:4px}
.shd .snum{flex:0 0 auto;width:42px;height:42px;border-radius:12px;background:var(--indigo);color:#fff;font-family:var(--disp);font-weight:700;font-size:1.2rem;display:grid;place-items:center}
.shd h2{font-size:1.5rem;color:var(--ink)}
.sdesc{color:var(--muted);font-size:1rem;margin:2px 0 0}
.scols{display:grid;grid-template-columns:270px 1fr;gap:34px;align-items:start;margin-top:18px}
.phone{position:sticky;top:78px;width:270px;background:#0E1730;border-radius:28px;padding:11px;box-shadow:0 16px 40px rgba(24,30,60,.14)}
.phone .scr{height:540px;overflow-y:auto;background:#fff;border-radius:19px;scrollbar-width:thin}
.phone .scr img{width:100%;display:block;cursor:zoom-in}
.phscroll{text-align:center;color:var(--faint);font-size:.82rem;margin-top:8px;font-family:var(--bn)}
.howto{background:var(--indigo-s);border:1px solid #CFD4F3;border-radius:14px;padding:14px 16px;margin-bottom:18px}
.howto .ht-h{font-family:var(--disp);font-weight:700;color:var(--indigo2);margin-bottom:8px;display:flex;align-items:center;gap:8px}
.howto .ht-h::before{content:"";width:16px;height:16px;border-radius:50%;border:3px solid var(--ring);display:inline-block}
.howto p{margin:5px 0;color:var(--ink);font-size:.98rem}
.howto p b{color:var(--indigo2)}
.howto .more{margin-top:8px;padding-top:8px;border-top:1px solid #D4D9F4;color:var(--muted);font-size:.92rem}
.parts{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.part{display:flex;gap:12px;background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:13px 15px;box-shadow:0 1px 4px rgba(24,30,60,.04)}
.part .pdot{flex:0 0 auto;width:28px;height:28px;border-radius:50%;background:var(--indigo-s);color:var(--indigo2);font-family:var(--disp);font-weight:700;font-size:.92rem;display:grid;place-items:center}
.part .pbody b{font-weight:700;color:var(--ink);display:block;margin-bottom:1px}
.part .pbody p{color:var(--muted);font-size:.93rem;line-height:1.5}

/* pitch */
.pitch-sec{margin-top:50px;scroll-margin-top:76px}
.pitch{display:flex;flex-direction:column;gap:14px;margin-top:6px}
.pline{display:flex;gap:16px;align-items:center;background:var(--paper);border:1px solid var(--line);border-left:5px solid var(--indigo);border-radius:0 16px 16px 0;padding:18px 22px;box-shadow:0 2px 8px rgba(24,30,60,.05)}
.pline .pn{flex:0 0 auto;width:44px;height:44px;border-radius:50%;background:var(--indigo);color:#fff;font-family:var(--disp);font-weight:700;font-size:1.4rem;display:grid;place-items:center}
.pline q{font-size:1.14rem;color:var(--ink);line-height:1.5;quotes:"\\201C" "\\201D"}

footer{margin-top:50px;padding-top:18px;border-top:1px solid var(--line);color:var(--faint);font-size:.86rem;text-align:center}

.lightbox{position:fixed;inset:0;z-index:50;display:none;background:rgba(9,13,28,.86);padding:26px;overflow:auto}
.lightbox.open{display:flex;align-items:flex-start;justify-content:center}
.lightbox img{width:360px;max-width:92vw;height:auto;border-radius:16px;box-shadow:0 20px 60px rgba(0,0,0,.5);margin:auto}
.lbx{position:fixed;top:16px;right:18px;width:42px;height:42px;border-radius:50%;border:none;background:rgba(255,255,255,.15);color:#fff;font-size:1.3rem;cursor:pointer}

@media(max-width:820px){
 .intro{grid-template-columns:1fr;gap:22px}.cover{position:static}.coverphone{max-width:280px;margin:0 auto}
 .tgrid{grid-template-columns:1fr}
 .scols{grid-template-columns:1fr;gap:18px}.phone{position:static;margin:0 auto}
 .parts{grid-template-columns:1fr}
 .pline q{font-size:1.04rem}
}
"""

def phone(img,scroll=True):
    s='<div class="phscroll">↕ scroll করে পুরো screen দেখুন · ছবিতে চাপ দিলে বড়</div>' if scroll else ''
    return f'<div><div class="phone"><div class="scr"><img class="zoom" src="{img}" alt="screen"></div></div>{s}</div>'

def parts(items):
    rows="".join(f'<li class="part"><span class="pdot">{to_bn(i)}</span><div class="pbody"><b>{n}</b><p>{d}</p></div></li>' for i,(n,d) in enumerate(items,1))
    return f'<ol class="parts">{rows}</ol>'

def screen(sid,num,title,desc,img,items,howto=""):
    hb=f'<div class="howto"><div class="ht-h">যেভাবে এই পাতায় আসবেন</div>{howto}</div>' if howto else ''
    return f"""<section class="screen" id="{sid}">
 <div class="shd"><span class="snum">{to_bn(num)}</span><div><h2>{title}</h2></div></div>
 <p class="sdesc">{desc}</p>
 <div class="scols">{phone(img)}<div class="pcol">{hb}{parts(items)}</div></div>
</section>"""

RESULT=[("১৬৭৮০","এই নম্বরে কল করে বাবা-মা প্রশ্ন করতে পারবেন।"),
("সন্তানের তথ্য","সন্তানের নাম, ছবি, ক্লাস, স্কুল আর কোর্সের নাম।"),
("সর্বমোট স্কোর","সব বিষয় মিলিয়ে গড় নম্বর। পাশে দেখায় গত মাসের চেয়ে কত বেড়েছে বা কমেছে।"),
("ক্লাস ও এক্সাম","ক্লাসে আর পরীক্ষায় আলাদা করে কত %।"),
("বিষয়ভিত্তিক পারফরম্যান্স","প্রতিটি বিষয়ের নম্বর। পাশে লেখা থাকে ভালো, মাঝারি বা উন্নতির প্রয়োজন।"),
("কতটা নিয়মিত","মাসে কয়টি লাইভ ক্লাস হয়েছে, সন্তান কয়টি করেছে।"),
("শিক্ষকের নোট","শিখোর একাডেমিক ডিরেক্টরের একটি ছোট নোট।"),
("সবচেয়ে ভালো যা করেছে","সন্তানের সেরা ফলাফলের কার্ড। বাবা-মা ডাউনলোড বা শেয়ার করতে পারেন।"),
("সপ্তাহে কেমন যাচ্ছে","প্রতি সপ্তাহের ক্লাস আর এক্সামের হিসাব, গ্রাফে।"),
("রেজাল্ট, পড়াশোনা, লিডারবোর্ড","নিচের এই ৩টি বাটনে ট্যাপ করলে অন্য পাতা খোলে।")]
SUBJECT=[("গড় স্কোর","এই বিষয়ে সন্তানের গড় নম্বর।"),
("র‍্যাঙ্ক","এই বিষয়ে সবার মধ্যে সন্তান কততম।"),
("ক্লাস কমপ্লিশন","এই বিষয়ের কয়টি ক্লাস করেছে।"),
("চ্যাপ্টার এক্সাম স্কোর","অধ্যায়ের পরীক্ষায় গড় নম্বর।"),
("লার্নিং এক্টিভিটির হিসাব","কুইজ কতবার দিয়েছে, কয়টি রিসোর্স দেখেছে।"),
("চ্যাপ্টারের পারফরম্যান্স","অধ্যায়গুলো ৩ ভাগে দেখায়: উন্নতির প্রয়োজন, মডারেট, ভালো।")]
STUDY=[("লাইভ ক্লাস","মোট ক্লাসের মধ্যে কয়টি করেছে। নিচে দেখায় লাইভে ছিল, রেকর্ডিং দেখেছে, মিস করেছে।"),
("বিষয়ভিত্তিক ক্লাস","প্রতিটি বিষয়ে কয়টি ক্লাস হয়েছে, কয়টি করেছে, কয়টি মিস।"),
("তারিখ ধরে দেখুন","ক্যালেন্ডারে প্রতিটি দিনের রঙ দেখে বোঝা যায় সেদিন ক্লাস করেছে কি না।"),
("চ্যাপ্টার এক্সাম","কয়টি পরীক্ষা দিয়েছে, কয়টিতে অর্ধেকের বেশি নম্বর পেয়েছে।"),
("লার্নিং এক্টিভিটি","ভিডিও, রেকর্ডিং, কুইজ আর রিসোর্স কতগুলো দেখেছে।")]
LEADER=[("সেরা ৩ জন","মেডেলসহ প্রথম তিনজন।"),
("র‍্যাঙ্ক তালিকা","বাকিদের নাম, স্কুল আর নম্বর।"),
("আপনার সন্তানের র‍্যাঙ্ক","নিচে সবসময় দেখায় সন্তান কততম, আর মোট কতজন।")]

BODY=f"""
<div class="accentbar"></div>
<div class="topbar"><div class="in">{LOGO.replace('<svg','<svg class="logo"',1)}<span class="tag">এজেন্ট গাইড · Internal</span></div></div>
<div class="wrap">

<div class="intro">
 <div>
  <h1>শিখো রিপোর্ট কার্ড: এজেন্টদের গাইড</h1>
  <p class="sub">বাবা-মা রিপোর্ট কার্ডে কী দেখবেন, আর ফোনে কীভাবে বলবেন।</p>
  <h2><span class="b"></span>বাবা-মায়ের সমস্যা</h2>
  <ul>
   <li>বাবা-মা টাকা দেন, কিন্তু সন্তান পড়ছে কি না দেখতে পান না।</li>
   <li>সন্তান ক্লাস করেছে কি না, পরীক্ষায় কত পেয়েছে, তা জানেন না।</li>
   <li>কোন বিষয়ে দুর্বল, তা অনেক দেরিতে জানতে পারেন।</li>
  </ul>
  <h2><span class="b"></span>রিপোর্ট কার্ড কী</h2>
  <p>রিপোর্ট কার্ড একটি লিংক। এতে সন্তানের পুরো মাসের পড়াশোনার হিসাব থাকে।</p>
  <h2><span class="b"></span>বাবা-মা কীভাবে পাবেন</h2>
  <ul>
   <li>জানুয়ারি থেকে চালু হবে।</li>
   <li>প্রতি মাসে বাবা-মায়ের ফোনে একটি লিংক যাবে।</li>
   <li>লিংকে ট্যাপ করলেই রিপোর্ট খুলবে। অ্যাপ বা লগইন লাগবে না।</li>
  </ul>
  <div class="send">
    <div class="sh"><span class="pb">Trial / Free</span>এজেন্ট হিসেবে কীভাবে পাঠাবেন</div>
    <div class="flow">
      <span class="fstep"><span class="n">১</span>CRM · Lead Details</span><span class="farr">›</span>
      <span class="fstep"><span class="n">২</span>“Share Report Card”</span><span class="farr">›</span>
      <span class="fstep wa"><span class="n">৩</span>WhatsApp</span><span class="farr">/</span>
      <span class="fstep sms"><span class="n">৪</span>SMS</span>
    </div>
  </div>
  <div class="note"><b>খেয়াল রাখুন:</b> জানুয়ারির আগে ডিজাইন কিছুটা বদলাতে পারে।</div>
 </div>
 <div class="cover">
  <div class="coverphone"><div class="cwin"><img class="zoom" src="{imgs['result']}" alt="রিপোর্ট কার্ড"></div></div>
  <div class="cap">লিংক খুললে বাবা-মা এই পাতা দেখবেন</div>
 </div>
</div>

<div class="toc">
 <div class="th disp">সূচিপত্র</div>
 <div class="ts">যে অংশ দেখতে চান, তার নামে চাপ দিন।</div>
 <div class="tgrid">
  <a class="tc" href="#result"><span class="num">১</span><div><b>রেজাল্ট</b><span>প্রথম যে পাতা</span></div></a>
  <a class="tc" href="#subject"><span class="num">২</span><div><b>বিষয়ের পাতা</b><span>বিষয়ে ট্যাপ করলে</span></div></a>
  <a class="tc" href="#study"><span class="num">৩</span><div><b>পড়াশোনা</b><span>Class ও Activity</span></div></a>
  <a class="tc" href="#leaderboard"><span class="num">৪</span><div><b>লিডারবোর্ড</b><span>Rank</span></div></a>
  <a class="tc" href="#pitch"><span class="num">৫</span><div><b>ফোনে কীভাবে বলবেন</b><span>৩টি কথা</span></div></a>
 </div>
</div>

{screen('result',1,'রেজাল্ট','লিংক খুললে বাবা-মা প্রথমে এই পাতা দেখবেন।',imgs['result'],RESULT)}

{screen('subject',2,'বিষয়ের পাতা','রেজাল্ট পাতায় কোনো বিষয়ে ট্যাপ করলে এই পাতা খোলে।',imgs['subject'],SUBJECT,
 howto='<p><b>ধাপ ১:</b> রেজাল্ট পাতায় যেকোনো বিষয়ের নামে ট্যাপ করুন।</p><p><b>ধাপ ২:</b> এই পাতাটি খুলবে।</p><div class="more">উপরের তীর চিহ্নে ট্যাপ করলে আবার রেজাল্ট পাতায় ফেরা যায়।</div>')}

{screen('study',3,'পড়াশোনা','স্ক্রিনের নিচে ‘পড়াশোনা’ বাটনে ট্যাপ করলে এই পাতা খোলে।',imgs['study'],STUDY,
 howto='<p><b>ধাপ ১:</b> স্ক্রিনের নিচে ‘পড়াশোনা’ বাটনে ট্যাপ করুন।</p><p><b>ধাপ ২:</b> এই পাতাটি খুলবে।</p>')}

{screen('leaderboard',4,'লিডারবোর্ড','স্ক্রিনের নিচে ‘লিডারবোর্ড’ বাটনে ট্যাপ করলে এই পাতা খোলে।',imgs['leader'],LEADER,
 howto='<p><b>ধাপ ১:</b> স্ক্রিনের নিচে ‘লিডারবোর্ড’ বাটনে ট্যাপ করুন।</p><p><b>ধাপ ২:</b> এই পাতাটি খুলবে।</p><div class="more">একই কোর্সের অন্য শিক্ষার্থীদের সাথে সন্তানের তুলনা।</div>')}

<div class="pitch-sec" id="pitch">
 <div class="shd"><span class="snum">৫</span><div><h2>ফোনে কীভাবে বলবেন</h2></div></div>
 <p class="sdesc">বাবা-মাকে এই ৩টি কথা বলুন।</p>
 <div class="pitch">
  <div class="pline"><span class="pn">১</span><q>জানুয়ারি থেকে প্রতি মাসে আপনার ফোনে সন্তানের রিপোর্ট কার্ড যাবে।</q></div>
  <div class="pline"><span class="pn">২</span><q>এতে দেখবেন সন্তান কয়টি ক্লাস করেছে, পরীক্ষায় কত পেয়েছে, কোন বিষয়ে দুর্বল।</q></div>
  <div class="pline"><span class="pn">৩</span><q>কোনো অ্যাপ লাগবে না। লিংকে চাপ দিলেই খুলবে।</q></div>
 </div>
 <div class="note"><b>খেয়াল রাখুন:</b> নির্দিষ্ট তারিখ বা নতুন কোনো ফিচারের কথা দেবেন না। ডিজাইন বদলালে বাবা-মা ভুল বুঝতে পারেন।</div>
</div>

<footer>শিখো রিপোর্ট কার্ড · এজেন্ট গাইড · Internal use only</footer>
</div>
<div class="lightbox" id="lb"><button class="lbx" id="lbx">&times;</button><img id="lbimg" alt="বড় করে"></div>
"""

JS=r"""
document.addEventListener('click',function(e){
 if(e.target.classList && e.target.classList.contains('zoom')){ var lb=document.getElementById('lb'); document.getElementById('lbimg').src=e.target.src; lb.classList.add('open'); return; }
 if(e.target.id==='lb'||e.target.id==='lbx'){ document.getElementById('lb').classList.remove('open'); }
});
document.addEventListener('keydown',function(e){ if(e.key==='Escape') document.getElementById('lb').classList.remove('open'); });
"""

HTML=f"""<!doctype html><html lang="bn"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>শিখো রিপোর্ট কার্ড — এজেন্ট গাইড</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Baloo+Da+2:wght@600;700&family=Hind+Siliguri:wght@400;500;600;700&family=Inter:wght@400;600;700&display=swap">
<style>{CSS}</style></head><body>{BODY}
<script>{JS}</script>
</body></html>"""
out=os.path.join(BASE,"Learning Report - Care Team Guide.html")
open(out,"w",encoding="utf-8").write(HTML)
print("written %.2f MB -> %s"%(len(HTML.encode())/1e6,out))
