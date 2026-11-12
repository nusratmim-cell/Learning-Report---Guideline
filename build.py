import base64, os
BASE="/home/shikho/shareable report card"
LOGO=open("/home/shikho/Desktop/Laptop Backup/Brac-Teacher-Demo-main (3)/Brac-Teacher-Demo-main/public/shikho-logo.svg",encoding="utf-8").read().strip()
def b64(p): return base64.b64encode(open(os.path.join(BASE,p),'rb').read()).decode()
imgs={k:"data:image/png;base64,"+b64("email-assets/"+v) for k,v in {
 "result":"01-result-page.png","subject":"02-subject-page.png","chapter":"03-chapter-page.png",
 "study":"04-study-page.png","leader":"05-leaderboard.png"}.items()}

ICONS={
 "target":'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
 "calendar":'<rect x="3" y="4.5" width="18" height="17" rx="2.5"/><path d="M16 2.5v4M8 2.5v4M3 9.5h18"/>',
 "trophy":'<path d="M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M7 5H4.5a2 2 0 0 0 0 4H7M17 5h2.5a2 2 0 0 1 0 4H17"/><path d="M12 14v3M8.5 21h7M10 17.5h4"/>',
 "send":'<path d="M21 3 10.5 13.5"/><path d="M21 3l-6.5 18-4-8-8-4z"/>',
 "chat":'<path d="M21 14a2 2 0 0 1-2 2H8l-4 4V6a2 2 0 0 1 2-2h13a2 2 0 0 1 2 2z"/>',
 "help":'<circle cx="12" cy="12" r="9.2"/><path d="M9.3 9a2.8 2.8 0 0 1 5.4 1c0 1.8-2.7 2.5-2.7 2.5"/><path d="M12 17h.01"/>',
 "check":'<rect x="7.5" y="2.5" width="9" height="4" rx="1.3"/><path d="M16 4.5h2.5a1.8 1.8 0 0 1 1.8 1.8v13.4a1.8 1.8 0 0 1-1.8 1.8H5.5a1.8 1.8 0 0 1-1.8-1.8V6.3a1.8 1.8 0 0 1 1.8-1.8H8"/><path d="m9 14 2 2 4-4"/>',
 "wa":'<path d="M20.5 11.6A8.4 8.4 0 1 1 7 4.6"/><path d="M20.5 11.6a8.4 8.4 0 0 1-12 7.4L3.5 20.5l1.6-4.8"/><path d="M8.5 9c0 4 2.5 6.5 6.5 6.5"/>',
 "sms":'<path d="M21 14a2 2 0 0 1-2 2H8l-4 4V6a2 2 0 0 1 2-2h13a2 2 0 0 1 2 2z"/><path d="M8 10h8M8 13h5"/>',
 "alert":'<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
 "spark":'<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>',
 "hand":'<path d="M9 11V5.5a1.5 1.5 0 0 1 3 0V11M12 11V4.5a1.5 1.5 0 0 1 3 0V11M15 11V6.5a1.5 1.5 0 0 1 3 0V13a6 6 0 0 1-6 6h-1.3a5 5 0 0 1-3.7-1.7L4.6 14a1.6 1.6 0 0 1 2.3-2.2L9 13.5"/>',
 "maximize":'<path d="M8 3H5a2 2 0 0 0-2 2v3M21 8V5a2 2 0 0 0-2-2h-3M3 16v3a2 2 0 0 0 2 2h3M16 21h3a2 2 0 0 0 2-2v-3"/>',
 "play":'<circle cx="12" cy="12" r="9.2"/><path d="M10 8.5v7l6-3.5z" fill="currentColor" stroke="none"/>',
}
def ic(name,size=22): return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>'

CSS="""
:root{color-scheme:light;
--ground:#F6F4EF;--paper:#fff;--ink:#191C24;--ink2:#4B5060;--ink3:#80859A;
--line:#E6E2D9;--line2:#F0EDE6;
--navy:#355DAB;--navy2:#2A4A8C;--navy-s:#EAF0FB;
--mag:#E2008D;--mag-s:#FCEAF4;
--orange:#EF8A04;--orange-s:#FDF0DA;
--good:#2C9A5C;--good-s:#E4F3EA;
--purple:#8B2FA0;--purple-s:#F6EAF8;
--teal:#0E8F94;--teal-s:#DDF1F2;
--red:#D5415E;--red-s:#FCEAED;--yellow:#E0A800;
--sans:"Inter","Hind Siliguri",system-ui,sans-serif;--bn:"Hind Siliguri","Inter",system-ui,sans-serif;
--sh:0 2px 8px rgba(24,30,60,.06),0 1px 2px rgba(24,30,60,.04);--sh2:0 16px 40px rgba(24,30,60,.12);}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);font-size:16.5px;line-height:1.65;-webkit-font-smoothing:antialiased}
.bn{font-family:var(--bn)}
.accentbar{height:5px;background:linear-gradient(90deg,var(--navy),var(--mag) 55%,var(--orange))}
.topbar{background:#fff;border-bottom:1px solid var(--line)}
.topbar .in{max-width:900px;margin:0 auto;padding:9px 22px;display:flex;align-items:center;justify-content:space-between;gap:12px}
.topbar svg.logo{height:26px;width:auto;display:block}
.topbar .tag{font-size:.68rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--navy2);background:var(--navy-s);border:1px solid #D4DFF5;border-radius:999px;padding:5px 12px;white-space:nowrap}
.wrap{max-width:900px;margin:0 auto;padding:22px 22px 80px}
h1,h2,h3{margin:0;line-height:1.24}

.hero{position:relative;overflow:hidden;border-radius:26px;padding:30px;box-shadow:var(--sh2);
background:radial-gradient(120% 140% at 85% 10%,#9A2FA0 0%,rgba(154,47,160,0) 42%),linear-gradient(135deg,#12264D,#355DAB 72%)}
.hero .grid{display:grid;grid-template-columns:1fr 288px;gap:30px;align-items:center;position:relative;z-index:1}
.hero .eyebrow{font-size:.72rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#FFC0E6}
.hero h1{color:#fff;font-size:2.1rem;font-weight:800;letter-spacing:-.01em;margin:10px 0 8px}
.hero p{color:#CFDBF2;margin:0 0 18px;font-size:1.04rem;max-width:40em}
.hero p b{color:#fff;font-weight:700}
.hero .pills{display:flex;flex-wrap:wrap;gap:9px}
.hero .pill{display:flex;align-items:center;gap:8px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.22);color:#fff;border-radius:999px;padding:8px 14px;font-size:.92rem;font-weight:600}
.hero .pill i{width:7px;height:7px;border-radius:50%;flex:0 0 auto}
.herocard{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.22);border-radius:20px;padding:20px 22px;color:#fff;box-shadow:0 14px 34px rgba(0,0,0,.22)}
.herocard .hc-top{font-size:.72rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:#BFD2F3}
.herocard .hc-score{font-size:3.1rem;font-weight:800;line-height:1.05;margin:6px 0 2px;color:#fff}
.herocard .hc-score span{font-size:1.5rem;font-weight:700;color:#A7F3D0;margin-left:3px}
.herocard .hc-bar{height:10px;border-radius:999px;background:rgba(255,255,255,.18);overflow:hidden;margin:8px 0 12px}
.herocard .hc-bar i{display:block;height:100%;width:92%;border-radius:999px;background:linear-gradient(90deg,#6EE7B7,#34D399)}
.herocard .hc-row{display:flex;justify-content:space-between;font-size:.9rem;color:#CFDBF2;font-weight:600}

.sec{margin-top:40px}
.shead{display:flex;align-items:center;gap:14px;margin-bottom:14px}
.sico{flex:0 0 auto;width:46px;height:46px;border-radius:14px;display:grid;place-items:center;color:#fff;box-shadow:var(--sh)}
.g-navy{background:linear-gradient(145deg,#4a74c4,#2A4A8C)}
.g-mag{background:linear-gradient(145deg,#f23bab,#C00078)}
.g-orange{background:linear-gradient(145deg,#f7a93a,#E07C00)}
.g-good{background:linear-gradient(145deg,#39b873,#1F7D46)}
.g-purple{background:linear-gradient(145deg,#a94dbd,#731d86)}
.g-teal{background:linear-gradient(145deg,#1cb0b6,#0A777C)}
.g-red{background:linear-gradient(145deg,#ef5e78,#B8304B)}
.shead .k{font-size:.68rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--ink3)}
.shead h2{font-size:1.32rem;font-weight:800;color:var(--ink);letter-spacing:-.01em}
.slead{color:var(--ink2);margin:-4px 0 14px;padding-left:60px;font-family:var(--bn)}
.slead b{color:var(--ink);font-weight:800}
.block{background:var(--paper);border:1px solid var(--line);border-radius:20px;padding:22px;box-shadow:var(--sh)}

/* problem / solution */
.problem{display:grid;grid-template-columns:1fr 46px 1fr;gap:12px;align-items:stretch}
.pcard{border-radius:16px;padding:18px 20px;border:1px solid}
.pcard.bad{background:var(--red-s);border-color:#F3C9D1}
.pcard.good{background:var(--good-s);border-color:#C6E6D2}
.pcard .pl{display:flex;align-items:center;gap:8px;font-size:.72rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;margin-bottom:8px}
.pcard.bad .pl{color:#B8304B}.pcard.good .pl{color:#1F7D46}
.pcard .pl .d{width:26px;height:26px;border-radius:8px;display:grid;place-items:center;color:#fff}
.pcard.bad .pl .d{background:var(--red)}.pcard.good .pl .d{background:var(--good)}
.pcard p{margin:0;font-family:var(--bn);color:var(--ink);font-size:1rem}
.pcard p b{font-weight:800}
.parrow{display:grid;place-items:center;color:var(--ink3)}

/* clickable demo */
.demo{display:grid;grid-template-columns:300px 1fr;gap:28px;align-items:start}
.phone{width:300px;background:#0E1730;border-radius:30px;padding:12px 12px 0;box-shadow:var(--sh2);align-self:start}
.phone .scr{height:498px;overflow-y:auto;background:#fff;border-radius:20px 20px 0 0;scrollbar-width:thin}
.phone .scr img{width:100%;display:block;cursor:zoom-in}
.phone .ptabs{display:flex;background:#fff;border-top:1px solid var(--line);border-radius:0 0 20px 20px;overflow:hidden}
.phone .ptabs button{flex:1;border:none;background:#fff;padding:9px 2px 10px;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:3px;color:var(--ink3);font-family:var(--bn);font-size:.74rem;font-weight:700;border-top:2px solid transparent}
.phone .ptabs button.on{color:var(--navy2);border-top-color:var(--navy)}
.phone .ptabs button svg{opacity:.85}
.dside .dcrumb{font-size:.78rem;font-weight:700;color:var(--mag);font-family:var(--bn);min-height:1.1em;margin-bottom:4px}
.dside h3{font-size:1.18rem;font-weight:800;color:var(--navy2);margin-bottom:10px}
.dside ul{margin:0 0 4px;padding:0;list-style:none}
.dside li{position:relative;padding-left:22px;margin:9px 0;color:var(--ink2);font-size:1rem;font-family:var(--bn)}
.dside li::before{content:"";position:absolute;left:0;top:9px;width:9px;height:9px;border-radius:3px;background:var(--navy)}
.dside li b{color:var(--ink);font-weight:700}
.ddrill{display:flex;flex-wrap:wrap;gap:9px;margin:14px 0 2px}
.ddrill button{font-family:var(--bn);font-weight:700;font-size:.92rem;cursor:pointer;border-radius:999px;padding:9px 15px}
.ddrill .drillb{background:var(--navy-s);border:1px solid #CFDCF6;color:var(--navy2)}
.ddrill .backb{background:#fff;border:1px solid var(--line);color:var(--ink2)}
.dlegend{display:flex;flex-wrap:wrap;gap:7px 14px;margin:16px 0 0;padding-top:14px;border-top:1px solid var(--line2)}
.dlegend .lg{display:flex;align-items:center;gap:7px;font-size:.9rem;color:var(--ink2);font-family:var(--bn)}
.dlegend .lg i{width:11px;height:11px;border-radius:4px}
.dhint{display:flex;align-items:center;gap:8px;margin-top:14px;font-size:.88rem;color:var(--ink3);font-family:var(--bn)}
.dhint .mi{flex:0 0 auto;width:26px;height:26px;border-radius:8px;background:var(--mag-s);color:var(--mag);display:grid;place-items:center}

.lightbox{position:fixed;inset:0;z-index:50;display:none;background:rgba(9,13,28,.86);padding:28px;overflow:auto}
.lightbox.open{display:flex;align-items:flex-start;justify-content:center}
.lightbox img{width:380px;max-width:92vw;height:auto;border-radius:16px;box-shadow:0 20px 60px rgba(0,0,0,.5);display:block;margin:auto}
.lbx{position:fixed;top:16px;right:18px;width:42px;height:42px;border-radius:50%;border:none;background:rgba(255,255,255,.15);color:#fff;font-size:1.3rem;cursor:pointer;line-height:1}

/* how a parent gets it (flow) */
.flowgrid{display:grid;grid-template-columns:1fr 1.4fr;gap:16px;align-items:start}
.lane{border-radius:18px;padding:18px;border:1px solid var(--line);background:#fff}
.lane.paid{background:var(--good-s);border-color:#C6E6D2}
.lane.manual{background:var(--navy-s);border-color:#D4DFF5}
.lane .lh{display:flex;align-items:center;gap:9px;margin-bottom:14px;font-weight:800;font-family:var(--bn);color:var(--ink)}
.lane .lh .pb{font-size:.66rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;padding:4px 9px;border-radius:999px;color:#fff}
.pb.gp{background:var(--good)}.pb.bp{background:var(--navy)}
.node{display:flex;align-items:center;gap:12px;background:#fff;border:1px solid var(--line);border-radius:13px;padding:11px 13px;box-shadow:var(--sh);font-family:var(--bn);font-size:.98rem;color:var(--ink)}
.node .nn{flex:0 0 auto;width:28px;height:28px;border-radius:50%;background:var(--navy-s);color:var(--navy2);font-weight:800;font-size:.85rem;display:grid;place-items:center;font-family:var(--sans)}
.node .ni{flex:0 0 auto;width:30px;height:30px;border-radius:9px;display:grid;place-items:center;color:#fff}
.node.wa{border-color:#2BB673;box-shadow:0 0 0 2px rgba(37,211,102,.14),var(--sh)}
.node.sms2{border-color:#B9C8EC}
.conn{display:flex;flex-direction:column;align-items:center;gap:2px;padding:6px 0;color:var(--ink3)}
.conn svg{opacity:.65}
.conn .albl{font-size:.78rem;color:var(--mag);font-weight:700;font-family:var(--bn)}
.lane.paid .big{display:flex;align-items:center;gap:12px;background:#fff;border:1px solid #C6E6D2;border-radius:13px;padding:13px 14px;font-family:var(--bn);color:var(--ink)}
.lane.paid .big .ni{width:38px;height:38px;border-radius:11px;background:var(--good);color:#fff;display:grid;place-items:center;flex:0 0 auto}
.lane.paid .big b{font-weight:800;display:block;line-height:1.3}
.lane.paid .big span.sub{color:var(--ink3);font-weight:600;font-size:.9rem}
.lane.paid .pnote{margin:12px 2px 0;color:#1F7D46;font-family:var(--bn);font-size:.92rem;font-weight:600;display:flex;align-items:center;gap:7px}

/* pitch lines */
.pitch{display:flex;flex-direction:column;gap:12px}
.pline{display:flex;gap:14px;background:#fff;border:1px solid var(--line);border-left:4px solid var(--mag);border-radius:0 14px 14px 0;padding:15px 18px;box-shadow:var(--sh)}
.pline .pn{flex:0 0 auto;width:30px;height:30px;border-radius:50%;background:var(--mag);color:#fff;font-weight:800;display:grid;place-items:center}
.pline .pt{font-family:var(--bn);color:#7D1552;font-size:1.02rem;line-height:1.6}

/* scripts + faq + checklist */
.cardgrid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.scard{background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px 18px;box-shadow:var(--sh);display:flex;flex-direction:column}
.scard .prob{display:inline-flex;align-items:center;gap:7px;align-self:flex-start;font-family:var(--bn);font-weight:800;font-size:.95rem;color:#9A3412;background:var(--orange-s);border:1px solid #F1D49A;border-radius:999px;padding:5px 12px;margin-bottom:11px}
.scard .prob i{width:8px;height:8px;border-radius:50%;background:var(--orange)}
.scard .say{background:var(--mag-s);border-radius:12px;padding:12px 14px;color:#7D1552;font-family:var(--bn);font-size:.97rem;line-height:1.6}
.scard .say .q{font-size:.66rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--mag);margin-bottom:5px}
.qa{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px;box-shadow:var(--sh)}
.qa .q{display:flex;gap:8px;font-weight:800;color:var(--navy2);font-family:var(--bn);margin-bottom:5px}
.qa .q .m{color:var(--mag);font-weight:900;flex:0 0 auto}
.qa .a{color:var(--ink2);font-family:var(--bn);font-size:.96rem}
.checks{display:grid;grid-template-columns:1fr 1fr;gap:10px 16px}
.chk{display:flex;align-items:center;gap:11px;background:#fff;border:1px solid var(--line);border-radius:12px;padding:11px 14px;font-family:var(--bn);color:var(--ink);box-shadow:var(--sh)}
.chk .ck{flex:0 0 auto;width:26px;height:26px;border-radius:50%;background:var(--good-s);color:var(--good);display:grid;place-items:center}
.chk .ck svg{width:15px;height:15px}

footer{margin-top:46px;color:var(--ink3);font-size:.85rem;text-align:center;font-family:var(--bn)}
@media(max-width:760px){
 body{font-size:16px}
 .hero{padding:22px}.hero .grid{grid-template-columns:1fr;gap:20px}.hero h1{font-size:1.85rem}
 .slead{padding-left:0}
 .problem{grid-template-columns:1fr}.parrow{transform:rotate(90deg)}
 .demo{grid-template-columns:1fr;gap:20px}.phone{margin:0 auto}
 .flowgrid,.cardgrid,.checks{grid-template-columns:1fr}
}
"""

def scr_tab(s,icon,label,on=False):
    return f'<button data-s="{s}"{" class=on" if on else ""}>{ic(icon,19)}<span>{label}</span></button>'

BODY=f"""
<div class="accentbar"></div>
<div class="topbar"><div class="in">{LOGO.replace('<svg','<svg class="logo"',1)}<span class="tag">Retention · Internal</span></div></div>
<div class="wrap">

<div class="hero">
 <div class="grid">
  <div class="htext">
    <div class="eyebrow">For Retention Agents</div>
    <h1>Shikho Learning Report</h1>
    <p>A monthly report sent to every guardian on the <b>1st working day</b> of each month — a snapshot of how their child studied on Shikho the previous month.</p>
    <div class="pills bn">
      <span class="pill"><i style="background:#67E8C0"></i>Overall Score</span>
      <span class="pill"><i style="background:#FFC978"></i>Attendance</span>
      <span class="pill"><i style="background:#FF8FD0"></i>Rank</span>
      <span class="pill"><i style="background:#9EC2FF"></i>Teacher's Note</span>
    </div>
  </div>
  <div class="herocard">
    <div class="hc-top bn">সার্বিক স্কোর · উদাহরণ</div>
    <div class="hc-score bn">৯২<span>%</span></div>
    <div class="hc-bar"><i></i></div>
    <div class="hc-row bn"><span>ক্লাস ৮৮%</span><span>এক্সাম ৯৬%</span></div>
  </div>
 </div>
</div>

<div class="sec">
 <div class="shead"><span class="sico g-red">{ic('alert')}</span><div><div class="k">The why · 01</div><h2>কী সমস্যা আমরা সমাধান করছি</h2></div></div>
 <div class="problem">
  <div class="pcard bad">
    <div class="pl"><span class="d">{ic('alert',16)}</span>যে সমস্যা</div>
    <p class="bn">অভিভাবক দেখতে পান না তাঁর সন্তান নিয়মিত পড়ছে কি না। <b>Visibility না থাকলে সন্দেহ তৈরি হয়</b> — আর কোর্স renew করতে চান না।</p>
  </div>
  <div class="parrow">{ic('send',22)}</div>
  <div class="pcard good">
    <div class="pl"><span class="d">{ic('check',16)}</span>Report যা করে</div>
    <p class="bn">প্রতি মাসে একটা পরিষ্কার ছবি — স্কোর, অ্যাটেন্ডেন্স, র‍্যাঙ্ক, শিক্ষকের নোট। <b>উন্নতি চোখে দেখলে অভিভাবক আস্থা পান</b>, আর পড়া চালিয়ে যান।</p>
  </div>
 </div>
</div>

<div class="sec">
 <div class="shead"><span class="sico g-navy">{ic('target')}</span><div><div class="k">Try it · 02</div><h2>রিপোর্টটা নিজে চালিয়ে দেখুন</h2></div></div>
 <p class="slead bn">নিচের Tab-এ চাপ দিন, scroll করুন, যেকোনো screen-এ চাপ দিলে <b>বড় করে</b> দেখা যাবে — অভিভাবক ঠিক এটাই দেখেন।</p>
 <div class="block">
  <div class="demo">
   <div class="phone">
     <div class="scr" id="scr"><img id="demoImg" alt="Learning Report screen"></div>
     <div class="ptabs">
       {scr_tab('result','target','রেজাল্ট',True)}
       {scr_tab('study','calendar','পড়াশোনা')}
       {scr_tab('leader','trophy','লিডারবোর্ড')}
     </div>
   </div>
   <div class="dside">
     <div class="dcrumb bn" id="dcrumb"></div>
     <h3 class="bn" id="dtitle"></h3>
     <ul id="dpoints"></ul>
     <div class="ddrill" id="ddrill"></div>
     <div class="dlegend">
       <span class="lg bn"><i style="background:#D5415E"></i>লাল — Practice দরকার</span>
       <span class="lg bn"><i style="background:#E0A800"></i>হলুদ — মাঝারি</span>
       <span class="lg bn"><i style="background:#2C9A5C"></i>সবুজ — ভালো</span>
     </div>
     <div class="dhint bn"><span class="mi">{ic('maximize',15)}</span>এই রঙ Overall Score, প্রতিটি Subject ও Chapter-এ দেখা যায়।</div>
   </div>
  </div>
 </div>
</div>

<div class="sec">
 <div class="shead"><span class="sico g-good">{ic('send')}</span><div><div class="k">Access · 03</div><h2>অভিভাবক কীভাবে এটা পাবেন</h2></div></div>
 <p class="slead bn">প্রতি মাসের <b>১ম কর্মদিবসে</b> আগের মাসের রিপোর্ট লিংক পৌঁছে যায়।</p>
 <div class="block">
  <div class="flowgrid">
   <div class="lane paid">
     <div class="lh bn"><span class="pb gp">Paid</span>Paid Student</div>
     <div class="big bn"><span class="ni">{ic('sms',20)}</span><span><b>Automatic SMS</b><span class="sub">প্রতি মাসে Link চলে যায়</span></span></div>
     <div class="pnote bn">{ic('check',16)} আলাদা করে কিছু পাঠাতে হয় না।</div>
   </div>
   <div class="lane manual">
     <div class="lh bn"><span class="pb bp">Trial / Free</span>CRM থেকে হাতে পাঠান</div>
     <div class="node bn"><span class="nn">1</span>CRM-এ <b style="margin-left:4px">Lead Details</b> খুলুন</div>
     <div class="conn"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M6 13l6 6 6-6"/></svg></div>
     <div class="node bn"><span class="nn">2</span><b style="margin-left:2px">“Share Report Card”</b> নির্বাচন করুন</div>
     <div class="conn"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M6 13l6 6 6-6"/></svg></div>
     <div class="node wa bn"><span class="ni" style="background:#25D366">{ic('wa',18)}</span><b style="margin-right:4px">WhatsApp</b>-এ Link পাঠান</div>
     <div class="conn"><span class="albl">WhatsApp না থাকলে</span><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M6 13l6 6 6-6"/></svg></div>
     <div class="node sms2 bn"><span class="ni" style="background:var(--navy)">{ic('sms',18)}</span><b style="margin-right:4px">SMS</b>-এ Link পাঠান</div>
   </div>
  </div>
 </div>
</div>

<div class="sec">
 <div class="shead"><span class="sico g-mag">{ic('hand')}</span><div><div class="k">Pitch · 04</div><h2>অভিভাবককে কীভাবে বলবেন</h2></div></div>
 <p class="slead bn">কথার মাঝে এই ৩টা লাইন বললেই যথেষ্ট —</p>
 <div class="pitch">
  <div class="pline"><span class="pn">1</span><span class="pt">“প্রতি মাসের ১ তারিখে আপনি SMS-এ একটা রিপোর্ট লিংক পাবেন — ওখানে দেখবেন আপনার সন্তান গত মাসে কেমন পড়েছে।”</span></div>
  <div class="pline"><span class="pn">2</span><span class="pt">“কোন বিষয়ে ভালো, কোথায় দুর্বল, কতটা ক্লাস করেছে আর র‍্যাঙ্ক কত — সব এক জায়গায়, কোনো App বা Login ছাড়াই।”</span></div>
  <div class="pline"><span class="pn">3</span><span class="pt">“প্রতি মাসে রিপোর্ট দেখলেই বুঝবেন উন্নতি হচ্ছে কি না — তাই পড়াটা চালিয়ে যাওয়াই বুদ্ধিমানের কাজ।”</span></div>
 </div>
</div>

<div class="sec">
 <div class="shead"><span class="sico g-orange">{ic('chat')}</span><div><div class="k">If stuck · 05</div><h2>সমস্যা হলে কী বলবেন</h2></div></div>
 <div class="cardgrid">
  <div class="scard"><span class="prob bn"><i></i>Report / Link পাওয়া যাচ্ছে না</span><div class="say"><div class="q">বলতে পারেন</div>"আপনার সন্তানের Report-এর Link-টা WhatsApp-এ আবার পাঠিয়ে দিচ্ছি। একটু দেখবেন পেয়েছেন কি না? Link-এ চাপ দিলেই Report খুলে যাবে।"</div></div>
  <div class="scard"><span class="prob bn"><i></i>Link খুলছে না</span><div class="say"><div class="q">বলতে পারেন</div>"একবার Internet Connection-টা দেখবেন? আমি Link-টা আবার পাঠাচ্ছি। না খুললে Chrome-এ চেষ্টা করুন। এরপরও সমস্যা হলে বিষয়টা আমরা চেক করব।"</div></div>
  <div class="scard"><span class="prob bn"><i></i>Score বুঝতে সমস্যা</span><div class="say"><div class="q">বলতে পারেন</div>"গত মাসে Class আর Exam-এ কেমন করেছে, তার ভিত্তিতে Overall Score। পাশে 'কীভাবে নির্ধারিত হয়' আছে, চাপ দিলে বিস্তারিত পাবেন।"</div></div>
  <div class="scard"><span class="prob bn"><i></i>কিছু জায়গায় তথ্য নেই (--)</span><div class="say"><div class="q">বলতে পারেন</div>"গত মাসে ওই Activity-র তথ্য না থাকলে এখানে কিছু দেখাবে না। তবে Activity থাকার পরও না দেখালে বিষয়টা আমরা চেক করব।"</div></div>
 </div>
</div>

<div class="sec">
 <div class="shead"><span class="sico g-purple">{ic('help')}</span><div><div class="k">FAQ · 06</div><h2>সাধারণ জিজ্ঞাসা</h2></div></div>
 <div class="cardgrid">
  <div class="qa"><div class="q bn"><span class="m">Q</span>Report কি শুধু Paid-দের জন্য?</div><div class="a bn">না। Paid, Trial ও Free — সবার Report দেখা যায়, শুধু Link পাওয়ার নিয়ম আলাদা।</div></div>
  <div class="qa"><div class="q bn"><span class="m">Q</span>Report দেখতে App লাগবে?</div><div class="a bn">না। শুধু Report Link থাকলেই Browser থেকে দেখা যায়।</div></div>
  <div class="qa"><div class="q bn"><span class="m">Q</span>Score কম কেন?</div><div class="a bn">গত মাসের Class ও Exam অনুযায়ী Score তৈরি হয়। কোন Subject/Chapter-এ কম, তা Report-এ দেখা যায়।</div></div>
  <div class="qa"><div class="q bn"><span class="m">Q</span>Attendance কীভাবে হিসাব?</div><div class="a bn">গত মাসের মোট Live Class-এর মধ্যে কতগুলো Attend করেছে, সেই অনুযায়ী।</div></div>
  <div class="qa"><div class="q bn"><span class="m">Q</span>Rank কীভাবে হয়?</div><div class="a bn">একই Program বা Batch-এর অন্য শিক্ষার্থীর সঙ্গে তুলনা করে।</div></div>
  <div class="qa"><div class="q bn"><span class="m">Q</span>Report কি অন্য কেউ দেখবে?</div><div class="a bn">যার কাছে Link থাকবে সে দেখতে পারবে। তাই Link Share না করাই ভালো।</div></div>
 </div>
</div>

<div class="sec">
 <div class="shead"><span class="sico g-teal">{ic('check')}</span><div><div class="k">Escalation · 07</div><h2>আমাদের কাছে পাঠানোর আগে</h2></div></div>
 <p class="slead bn">নিজে সমাধান করা না গেলে বিষয়টি টিমের কাছে <b>escalate</b> করুন — সাথে নিচের তথ্যগুলো দিন:</p>
 <div class="block">
  <div class="checks">
   <div class="chk bn"><span class="ck">{ic('check',15)}</span>Student-এর নাম ও Class</div>
   <div class="chk bn"><span class="ck">{ic('check',15)}</span>Registered Phone Number</div>
   <div class="chk bn"><span class="ck">{ic('check',15)}</span>কোন Screen-এ সমস্যা</div>
   <div class="chk bn"><span class="ck">{ic('check',15)}</span>কী দেখার কথা, কী দেখাচ্ছে</div>
   <div class="chk bn"><span class="ck">{ic('check',15)}</span>সম্ভব হলে Screenshot</div>
   <div class="chk bn"><span class="ck">{ic('check',15)}</span>সমস্যাটি কখন থেকে</div>
  </div>
 </div>
</div>

<footer>Shikho Learning Report · Retention Guideline · Internal use only</footer>
</div>

<div class="lightbox" id="lb"><button class="lbx" id="lbx">&times;</button><img id="lbimg" alt="enlarged screen"></div>
"""

IMGJS="{"+",".join(f'"{k}":"{v}"' for k,v in imgs.items())+"}"
JS=r"""
var IMG=__IMG__;
var S={
 result:{t:"রেজাল্ট — Overall Score",p:["<b>সার্বিক স্কোর ও ব্যান্ড</b> — আগের মাসের তুলনা সহ","<b>বিষয়ভিত্তিক স্কোর</b> — রঙ দিয়ে ভালো / দুর্বল","নিয়মিততা, শিক্ষকের নোট ও সেরা অর্জন"],drill:["subject","chapter"]},
 subject:{t:"Subject — বিষয়ে চাপ দিলে",parent:"result",p:["<b>গড় স্কোর</b> ও এই বিষয়ে র‍্যাঙ্ক","ক্লাস কমপ্লিশন ও এক্সাম স্কোর","<b>চ্যাপ্টার পারফরম্যান্স</b> — দুর্বল / মডারেট / ভালো"]},
 chapter:{t:"Chapter — চ্যাপ্টারে চাপ দিলে",parent:"result",p:["<b>এক্সাম স্কোর</b>, র‍্যাঙ্ক ও গ্রেড","ক্লাস ও এক্সামের হিসাব","<b>সংশ্লিষ্ট ভিডিও ও Lesson</b> — আবার দেখে Practice"]},
 study:{t:"পড়াশোনা — Class ও Activity",p:["<b>লাইভ ক্লাস</b> — কত করেছে, মিস করেছে","<b>Calendar</b> — দিন ধরে রঙে অ্যাটেন্ডেন্স","চ্যাপ্টার এক্সাম ও লার্নিং এক্টিভিটি"]},
 leader:{t:"লিডারবোর্ড — Rank",p:["সেরা তিনজন (Medal সহ)","র‍্যাঙ্ক তালিকা","<b>নিজের সন্তানের র‍্যাঙ্ক</b> ও মোট শিক্ষার্থী"]}
};
var DRILL={subject:"বিষয়ে ঢুকুন",chapter:"চ্যাপ্টারে ঢুকুন"};
var MAIN={result:"result",subject:"result",chapter:"result",study:"study",leader:"leader"};
function setScreen(k){
 var s=S[k]; if(!s) return;
 document.getElementById('demoImg').src=IMG[k];
 document.getElementById('scr').scrollTop=0;
 document.getElementById('dtitle').innerHTML=s.t;
 document.getElementById('dpoints').innerHTML=s.p.map(function(x){return '<li>'+x+'</li>';}).join('');
 var tb=document.querySelectorAll('.ptabs button');
 for(var i=0;i<tb.length;i++){tb[i].classList.toggle('on', tb[i].getAttribute('data-s')===MAIN[k]);}
 var d='';
 if(s.drill){ d=s.drill.map(function(x){return '<button class="drillb" data-s="'+x+'">'+DRILL[x]+' ›</button>';}).join(''); }
 if(s.parent){ d='<button class="backb" data-s="'+s.parent+'">‹ রেজাল্টে ফিরুন</button>'; }
 document.getElementById('ddrill').innerHTML=d;
 document.getElementById('dcrumb').textContent = s.parent ? ('রেজাল্ট › '+s.t.split(' ')[0]) : '';
}
document.addEventListener('click',function(e){
 var t=e.target.closest ? e.target.closest('[data-s]') : null;
 if(t){ setScreen(t.getAttribute('data-s')); return; }
 if(e.target.id==='demoImg'){ var lb=document.getElementById('lb'); document.getElementById('lbimg').src=e.target.src; lb.classList.add('open'); return; }
 if(e.target.id==='lb'||e.target.id==='lbx'){ document.getElementById('lb').classList.remove('open'); }
});
document.addEventListener('keydown',function(e){ if(e.key==='Escape') document.getElementById('lb').classList.remove('open'); });
setScreen('result');
""".replace("__IMG__",IMGJS)

HTML=f"""<!doctype html><html lang="bn"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Shikho Learning Report Guideline</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Hind+Siliguri:wght@400;500;600;700&display=swap">
<style>{CSS}</style></head><body>{BODY}
<script>{JS}</script>
</body></html>"""
out=os.path.join(BASE,"Learning Report - Care Team Guide.html")
open(out,"w",encoding="utf-8").write(HTML)
print("written %.2f MB -> %s"%(len(HTML.encode())/1e6,out))
