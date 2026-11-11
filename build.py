import base64, os
BASE="/home/shikho/shareable report card"
LOGO=open("/home/shikho/Desktop/Laptop Backup/Brac-Teacher-Demo-main (3)/Brac-Teacher-Demo-main/public/shikho-logo.svg",encoding="utf-8").read().strip()
def b64(p): return base64.b64encode(open(os.path.join(BASE,p),'rb').read()).decode()
imgs={k:"data:image/png;base64,"+b64("email-assets/"+v) for k,v in {
 "result":"01-result-page.png","subject":"02-subject-page.png","chapter":"03-chapter-page.png",
 "study":"04-study-page.png","leader":"05-leaderboard.png"}.items()}

ICONS={
 "target":'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
 "book":'<path d="M12 7v13"/><path d="M4 19V5a1 1 0 0 1 1-1h4a3 3 0 0 1 3 3 3 3 0 0 1 3-3h4a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1h-6a2 2 0 0 0-2 2 2 2 0 0 0-2-2H4"/>',
 "grid":'<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
 "calendar":'<rect x="3" y="4.5" width="18" height="17" rx="2.5"/><path d="M16 2.5v4M8 2.5v4M3 9.5h18"/>',
 "trophy":'<path d="M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M7 5H4.5a2 2 0 0 0 0 4H7M17 5h2.5a2 2 0 0 1 0 4H17"/><path d="M12 14v3M8.5 21h7M10 17.5h4"/>',
 "columns":'<rect x="3" y="4" width="18" height="16" rx="2.5"/><path d="M9 4v16M15 4v16"/>',
 "send":'<path d="M21 3 10.5 13.5"/><path d="M21 3l-6.5 18-4-8-8-4z"/>',
 "chat":'<path d="M21 14a2 2 0 0 1-2 2H8l-4 4V6a2 2 0 0 1 2-2h13a2 2 0 0 1 2 2z"/>',
 "help":'<circle cx="12" cy="12" r="9.2"/><path d="M9.3 9a2.8 2.8 0 0 1 5.4 1c0 1.8-2.7 2.5-2.7 2.5"/><path d="M12 17h.01"/>',
 "check":'<rect x="7.5" y="2.5" width="9" height="4" rx="1.3"/><path d="M16 4.5h2.5a1.8 1.8 0 0 1 1.8 1.8v13.4a1.8 1.8 0 0 1-1.8 1.8H5.5a1.8 1.8 0 0 1-1.8-1.8V6.3a1.8 1.8 0 0 1 1.8-1.8H8"/><path d="m9 14 2 2 4-4"/>',
 "card":'<rect x="2.5" y="5.5" width="19" height="13" rx="2.5"/><path d="M2.5 10h19M6 15h4"/>',
 "wa":'<path d="M20.5 11.6A8.4 8.4 0 1 1 7 4.6"/><path d="M20.5 11.6a8.4 8.4 0 0 1-12 7.4L3.5 20.5l1.6-4.8"/><path d="M8.5 9c0 4 2.5 6.5 6.5 6.5"/>',
 "sms":'<path d="M21 14a2 2 0 0 1-2 2H8l-4 4V6a2 2 0 0 1 2-2h13a2 2 0 0 1 2 2z"/><path d="M8 10h8M8 13h5"/>',
 "spark":'<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M18 6l-2.5 2.5M8.5 15.5 6 18"/>',
 "play":'<circle cx="12" cy="12" r="9.2"/><path d="M10 8.5v7l6-3.5z" fill="currentColor" stroke="none"/>',
 "external":'<path d="M15 3h6v6"/><path d="M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>',
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
--red:#D5415E;--yellow:#E0A800;
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

/* ---------- HERO ---------- */
.hero{position:relative;overflow:hidden;border-radius:26px;padding:30px;box-shadow:var(--sh2);
background:radial-gradient(120% 140% at 85% 10%,#9A2FA0 0%,rgba(154,47,160,0) 42%),linear-gradient(135deg,#12264D,#355DAB 72%)}
.hero .grid{display:grid;grid-template-columns:1fr 288px;gap:30px;align-items:center;position:relative;z-index:1}
.hero .eyebrow{font-size:.72rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#FFC0E6}
.hero h1{color:#fff;font-size:2.1rem;font-weight:800;letter-spacing:-.01em;margin:10px 0 8px}
.hero p{color:#CFDBF2;margin:0 0 18px;font-size:1.04rem;max-width:40em}
.hero p b{color:#fff;font-weight:700}
.herocard{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.22);border-radius:20px;padding:20px 22px;color:#fff;box-shadow:0 14px 34px rgba(0,0,0,.22)}
.herocard .hc-top{font-size:.72rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:#BFD2F3}
.herocard .hc-score{font-size:3.1rem;font-weight:800;line-height:1.05;margin:6px 0 2px;color:#fff}
.herocard .hc-score span{font-size:1.5rem;font-weight:700;color:#A7F3D0;margin-left:3px}
.herocard .hc-bar{height:10px;border-radius:999px;background:rgba(255,255,255,.18);overflow:hidden;margin:8px 0 12px}
.herocard .hc-bar i{display:block;height:100%;width:92%;border-radius:999px;background:linear-gradient(90deg,#6EE7B7,#34D399)}
.herocard .hc-row{display:flex;justify-content:space-between;font-size:.9rem;color:#CFDBF2;font-weight:600}
.hero .pills{display:flex;flex-wrap:wrap;gap:9px}
.hero .pill{display:flex;align-items:center;gap:8px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.22);color:#fff;border-radius:999px;padding:8px 14px;font-size:.92rem;font-weight:600}
.hero .pill i{width:7px;height:7px;border-radius:50%;flex:0 0 auto}

/* ---------- SECTION HEADER ---------- */
.sec{margin-top:40px}
.shead{display:flex;align-items:center;gap:14px;margin-bottom:16px}
.sico{flex:0 0 auto;width:46px;height:46px;border-radius:14px;display:grid;place-items:center;color:#fff;box-shadow:var(--sh)}
.g-navy{background:linear-gradient(145deg,#4a74c4,#2A4A8C)}
.g-mag{background:linear-gradient(145deg,#f23bab,#C00078)}
.g-orange{background:linear-gradient(145deg,#f7a93a,#E07C00)}
.g-good{background:linear-gradient(145deg,#39b873,#1F7D46)}
.g-purple{background:linear-gradient(145deg,#a94dbd,#731d86)}
.g-teal{background:linear-gradient(145deg,#1cb0b6,#0A777C)}
.shead .k{font-size:.68rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--ink3)}
.shead h2{font-size:1.32rem;font-weight:800;color:var(--ink);letter-spacing:-.01em}
.slead{color:var(--ink2);margin:-6px 0 14px;padding-left:60px;font-family:var(--bn)}
.slead b{color:var(--ink);font-weight:800}

/* ---------- SCREEN CARDS ---------- */
.screen{--a:var(--navy);--as:var(--navy-s);position:relative;overflow:hidden;display:grid;grid-template-columns:220px 1fr;gap:24px;align-items:center;
background:#fff;border:1px solid var(--line);border-radius:20px;padding:20px 22px 20px 26px;margin:14px 0;box-shadow:var(--sh)}
.screen::before{content:"";position:absolute;left:0;top:0;bottom:0;width:7px;background:var(--a)}
.screen.a-navy{--a:#355DAB;--as:var(--navy-s)}
.screen.a-mag{--a:#E2008D;--as:var(--mag-s)}
.screen.a-teal{--a:#0E8F94;--as:var(--teal-s)}
.screen.a-orange{--a:#E07C00;--as:var(--orange-s)}
.screen.a-purple{--a:#8B2FA0;--as:var(--purple-s)}
.shot{position:relative;border-radius:15px;overflow:hidden;border:1px solid var(--line);box-shadow:var(--sh2);background:#fff}
.shot img{width:100%;height:340px;object-fit:cover;object-position:top center;display:block}
.shot::after{content:"";position:absolute;left:0;right:0;bottom:0;height:52px;background:linear-gradient(rgba(255,255,255,0),#fff);pointer-events:none}
.shot .badge{position:absolute;top:10px;left:10px;z-index:2;width:34px;height:34px;border-radius:11px;background:var(--a);color:#fff;display:grid;place-items:center;box-shadow:0 4px 12px rgba(0,0,0,.25)}
.screen .bd h3{font-size:1.16rem;font-weight:800;color:var(--a);margin-bottom:10px}
.screen .bd ul{margin:0;padding:0;list-style:none}
.screen .bd li{position:relative;padding-left:24px;margin:9px 0;color:var(--ink2);font-size:1rem}
.screen .bd li::before{content:"";position:absolute;left:2px;top:9px;width:9px;height:9px;border-radius:3px;background:var(--a)}
.screen .bd li b{color:var(--ink);font-weight:700}

/* ---------- GENERIC BLOCK ---------- */
.block{background:var(--paper);border:1px solid var(--line);border-radius:20px;padding:22px;box-shadow:var(--sh)}
.tile-row{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px}
.tile{border-radius:16px;padding:16px 16px 18px;border:1px solid var(--line);position:relative;overflow:hidden;background:#fff}
.tile .ti{width:40px;height:40px;border-radius:12px;display:grid;place-items:center;color:#fff;margin-bottom:10px}
.tile h4{font-size:1.05rem;font-weight:800;margin:0 0 2px;color:var(--ink)}
.tile p{margin:0;font-size:.9rem;color:var(--ink3)}
.tile.b-navy{background:var(--navy-s);border-color:#D4DFF5}
.tile.b-orange{background:var(--orange-s);border-color:#F3DFB6}
.tile.b-purple{background:var(--purple-s);border-color:#E7CFEC}

/* tab-bar style switcher (Overview) */
.tabbar{display:grid;grid-template-columns:1fr 1fr 1fr;gap:7px;background:#EFEDE6;border:1px solid var(--line);border-radius:18px;padding:7px}
.tabbar .seg{border-radius:13px;padding:16px 10px 15px;text-align:center;background:transparent}
.tabbar .seg.active{background:#fff;box-shadow:var(--sh)}
.tabbar .seg .ti{width:40px;height:40px;border-radius:12px;display:grid;place-items:center;color:#fff;margin:0 auto 9px}
.tabbar .seg h4{font-size:1.04rem;font-weight:800;margin:0 0 2px;color:var(--ink)}
.tabbar .seg p{margin:0;font-size:.86rem;color:var(--ink3)}

/* Figma CTA */
.figmacta{display:flex;align-items:center;gap:14px;margin-top:16px;text-decoration:none;color:var(--ink);
background:linear-gradient(135deg,#fff,#F4EEFA);border:1px solid #E4D7F0;border-left:5px solid var(--purple);border-radius:16px;padding:15px 18px;box-shadow:var(--sh)}
.figmacta .fi{flex:0 0 auto;width:44px;height:44px;border-radius:12px;background:linear-gradient(145deg,#a94dbd,#731d86);color:#fff;display:grid;place-items:center}
.figmacta .txt{flex:1}
.figmacta .txt b{display:block;font-weight:800;font-family:var(--bn);line-height:1.3}
.figmacta .txt span{font-size:.9rem;color:var(--ink3)}
.figmacta .arr{color:var(--purple);font-size:1.35rem;font-weight:800;flex:0 0 auto}

.meter{margin-top:18px;background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:18px}
.meter .lbl{font-size:.82rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--ink3);margin-bottom:10px}
.meter .track{height:14px;border-radius:999px;background:linear-gradient(90deg,#D5415E,#E0A800 50%,#2C9A5C)}
.meter .legs{display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:12px}
.meter .leg{display:flex;align-items:center;gap:8px;font-size:.95rem;color:var(--ink2);font-family:var(--bn)}
.meter .leg i{width:12px;height:12px;border-radius:4px;flex:0 0 auto}
.meter .mnote{margin-top:12px;padding-top:11px;border-top:1px solid var(--line2);font-size:.9rem;color:var(--ink3);font-family:var(--bn)}
.callout{margin-top:16px;background:var(--mag-s);border:1px solid #F3C9E2;border-left:4px solid var(--mag);border-radius:0 14px 14px 0;padding:14px 16px;color:#8A1560;font-weight:700;font-family:var(--bn)}
.callout b{color:var(--mag)}

/* ---------- FLOW ---------- */
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

/* ---------- SCRIPT CARDS ---------- */
.cardgrid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.scard{background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px 18px;box-shadow:var(--sh);display:flex;flex-direction:column}
.scard .prob{display:inline-flex;align-items:center;gap:7px;align-self:flex-start;font-family:var(--bn);font-weight:800;font-size:.95rem;color:#9A3412;background:var(--orange-s);border:1px solid #F1D49A;border-radius:999px;padding:5px 12px;margin-bottom:11px}
.scard .prob i{width:8px;height:8px;border-radius:50%;background:var(--orange)}
.scard .say{position:relative;background:var(--mag-s);border-radius:12px;padding:12px 14px;color:#7D1552;font-family:var(--bn);font-size:.97rem;line-height:1.6}
.scard .say .q{font-size:.66rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--mag);margin-bottom:5px}

/* ---------- FAQ ---------- */
.qa{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px;box-shadow:var(--sh)}
.qa .q{display:flex;gap:8px;font-weight:800;color:var(--navy2);font-family:var(--bn);margin-bottom:5px}
.qa .q .m{color:var(--mag);font-weight:900;flex:0 0 auto}
.qa .a{color:var(--ink2);font-family:var(--bn);font-size:.96rem}

/* ---------- CHECKLIST ---------- */
.checks{display:grid;grid-template-columns:1fr 1fr;gap:10px 16px}
.chk{display:flex;align-items:center;gap:11px;background:#fff;border:1px solid var(--line);border-radius:12px;padding:11px 14px;font-family:var(--bn);color:var(--ink);box-shadow:var(--sh)}
.chk .ck{flex:0 0 auto;width:26px;height:26px;border-radius:50%;background:var(--good-s);color:var(--good);display:grid;place-items:center}
.chk .ck svg{width:15px;height:15px}

footer{margin-top:46px;color:var(--ink3);font-size:.85rem;text-align:center;font-family:var(--bn)}

@media(max-width:700px){
 body{font-size:16px}
 .hero{padding:22px}
 .hero .grid{grid-template-columns:1fr;gap:20px}
 .hero h1{font-size:1.85rem}
 .screen{grid-template-columns:1fr;gap:16px;padding:18px 18px 18px 22px}
 .shot{max-width:280px;margin:0 auto}
 .tile-row{grid-template-columns:1fr}
 .slead{padding-left:0}
 .tabbar .seg{padding:13px 6px}
 .tabbar .seg p{font-size:.78rem}
 .flowgrid,.cardgrid,.checks{grid-template-columns:1fr}
}
"""

def screen(acc,icon,img,title,pts):
    lis="".join("<li>%s</li>"%p for p in pts)
    return (f'<article class="screen a-{acc}"><div class="shot"><span class="badge">{ic(icon,20)}</span>'
            f'<img src="{img}" alt="{title}"></div><div class="bd"><h3 class="bn">{title}</h3>'
            f'<ul class="bn">{lis}</ul></div></article>')

def conn(label=""):
    arrow='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M6 13l6 6 6-6"/></svg>'
    lab=f'<span class="albl">{label}</span>' if label else ''
    return f'<div class="conn">{lab}{arrow}</div>'

BODY=f"""
<div class="accentbar"></div>
<div class="topbar"><div class="in">{LOGO.replace('<svg','<svg class="logo"',1)}<span class="tag">Internal · Guideline</span></div></div>
<div class="wrap">

<div class="hero">
 <div class="grid">
  <div class="htext">
    <div class="eyebrow">Customer Care · Internal Guideline</div>
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
 <div class="shead"><span class="sico g-teal">{ic('columns')}</span><div><div class="k">Overview · 01</div><h2 class="bn">Report-এ কী আছে</h2></div></div>
 <p class="slead bn">Report খুললে নিচে <b>৩টি Tab</b> দেখা যাবে — প্রতিটিতে আলাদা তথ্য।</p>
 <div class="block">
  <div class="tabbar">
    <div class="seg active"><span class="ti g-navy">{ic('target',20)}</span><h4 class="bn">রেজাল্ট</h4><p class="bn">Score ও বিষয়</p></div>
    <div class="seg"><span class="ti g-orange">{ic('calendar',20)}</span><h4 class="bn">পড়াশোনা</h4><p class="bn">Class ও Activity</p></div>
    <div class="seg"><span class="ti g-purple">{ic('trophy',20)}</span><h4 class="bn">লিডারবোর্ড</h4><p class="bn">Rank</p></div>
  </div>
  <div class="meter">
    <div class="lbl bn">Score-এর রঙ — কী বোঝায়</div>
    <div class="track"></div>
    <div class="legs">
      <span class="leg"><i style="background:#D5415E"></i>লাল — Practice দরকার</span>
      <span class="leg"><i style="background:#E0A800"></i>হলুদ — আরও সুযোগ আছে</span>
      <span class="leg"><i style="background:#2C9A5C"></i>সবুজ — ভালো করছে</span>
    </div>
    <div class="mnote bn">এই রঙ <b>Overall Score</b>, প্রতিটি <b>Subject</b> ও <b>Chapter</b>-এর ফলাফলে দেখা যায়।</div>
  </div>
  <div class="callout bn"><b>App বা Login লাগে না।</b> Report Link-এ চাপ দিলেই খোলে।</div>
 </div>
</div>

<div class="sec">
 <div class="shead"><span class="sico g-navy">{ic('grid')}</span><div><div class="k">Screen Guide · 02</div><h2 class="bn">কোন Screen-এ কী দেখায়</h2></div></div>
 {screen('navy','target',imgs['result'],"রেজাল্ট — Overall Score",["<b>সার্বিক স্কোর ও ব্যান্ড</b> — আগের মাসের তুলনা সহ","<b>বিষয়ভিত্তিক স্কোর</b> — রঙ দিয়ে ভালো / দুর্বল","নিয়মিততা, শিক্ষকের নোট ও সেরা অর্জন"])}
 {screen('mag','book',imgs['subject'],"Subject — বিষয়ে চাপ দিলে",["<b>গড় স্কোর</b> ও এই বিষয়ে র‍্যাঙ্ক","ক্লাস কমপ্লিশন ও এক্সাম স্কোর","<b>চ্যাপ্টার পারফরম্যান্স</b> — দুর্বল / মডারেট / ভালো"])}
 {screen('teal','grid',imgs['chapter'],"Chapter — চ্যাপ্টারে চাপ দিলে",["<b>এক্সাম স্কোর</b>, র‍্যাঙ্ক ও গ্রেড","ক্লাস ও এক্সামের হিসাব","<b>সংশ্লিষ্ট ভিডিও ও Lesson</b> — আবার দেখে Practice"])}
 {screen('orange','calendar',imgs['study'],"পড়াশোনা — Class ও Activity",["<b>লাইভ ক্লাস</b> — কত করেছে, মিস করেছে","<b>Calendar</b> — দিন ধরে রঙে অ্যাটেন্ডেন্স","চ্যাপ্টার এক্সাম ও লার্নিং এক্টিভিটি"])}
 {screen('purple','trophy',imgs['leader'],"লিডারবোর্ড — Rank",["সেরা তিনজন (Medal সহ)","র‍্যাঙ্ক তালিকা","<b>নিজের সন্তানের র‍্যাঙ্ক</b> ও মোট শিক্ষার্থী"])}
 <a class="figmacta" href="https://www.figma.com/design/qdjZtQmPsqhhQE13BIiRMH/Parent---Shareable-Report-Card--DH-?node-id=1-7030&t=YYFieAgPdPNnD5ey-0" target="_blank" rel="noopener">
   <span class="fi">{ic('external',22)}</span>
   <span class="txt"><b class="bn">Figma-তে সম্পূর্ণ page ডিজাইন দেখুন</b><span>Full-page designs for every screen</span></span>
   <span class="arr">→</span>
 </a>
</div>

<div class="sec">
 <div class="shead"><span class="sico g-good">{ic('send')}</span><div><div class="k">How to send · 03</div><h2 class="bn">Link কীভাবে পাঠাবেন</h2></div></div>
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
     {conn()}
     <div class="node bn"><span class="nn">2</span><b style="margin-left:2px">“Share Report Card”</b> নির্বাচন করুন</div>
     {conn()}
     <div class="node wa bn"><span class="ni" style="background:#25D366">{ic('wa',18)}</span><b style="margin-right:4px">WhatsApp</b>-এ Link পাঠান</div>
     {conn("WhatsApp না থাকলে")}
     <div class="node sms2 bn"><span class="ni" style="background:var(--navy)">{ic('sms',18)}</span><b style="margin-right:4px">SMS</b>-এ Link পাঠান</div>
   </div>
  </div>
 </div>
</div>

<div class="sec">
 <div class="shead"><span class="sico g-mag">{ic('chat')}</span><div><div class="k">Agent scripts · 04</div><h2 class="bn">সমস্যা হলে কী বলবেন</h2></div></div>
 <div class="cardgrid">
  <div class="scard"><span class="prob bn"><i></i>Report / Link পাওয়া যাচ্ছে না</span><div class="say"><div class="q">বলতে পারেন</div>"আপনার সন্তানের Report-এর Link-টা WhatsApp-এ আবার পাঠিয়ে দিচ্ছি। একটু দেখবেন পেয়েছেন কি না? Link-এ চাপ দিলেই Report খুলে যাবে।"</div></div>
  <div class="scard"><span class="prob bn"><i></i>Link খুলছে না</span><div class="say"><div class="q">বলতে পারেন</div>"একবার Internet Connection-টা দেখবেন? আমি Link-টা আবার পাঠাচ্ছি। না খুললে Chrome-এ চেষ্টা করুন। এরপরও সমস্যা হলে বিষয়টা আমরা চেক করব।"</div></div>
  <div class="scard"><span class="prob bn"><i></i>Score বুঝতে সমস্যা</span><div class="say"><div class="q">বলতে পারেন</div>"গত মাসে Class আর Exam-এ কেমন করেছে, তার ভিত্তিতে Overall Score। পাশে 'কীভাবে নির্ধারিত হয়' আছে, চাপ দিলে বিস্তারিত পাবেন।"</div></div>
  <div class="scard"><span class="prob bn"><i></i>কিছু জায়গায় তথ্য নেই (--)</span><div class="say"><div class="q">বলতে পারেন</div>"গত মাসে ওই Activity-র তথ্য না থাকলে এখানে কিছু দেখাবে না। তবে Activity থাকার পরও না দেখালে বিষয়টা আমরা চেক করব।"</div></div>
 </div>
</div>

<div class="sec">
 <div class="shead"><span class="sico g-purple">{ic('help')}</span><div><div class="k">FAQ · 05</div><h2 class="bn">সাধারণ জিজ্ঞাসা</h2></div></div>
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
 <div class="shead"><span class="sico g-orange">{ic('check')}</span><div><div class="k">Escalation · 06</div><h2 class="bn">আমাদের কাছে পাঠানোর আগে</h2></div></div>
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

<footer>Shikho Learning Report · Agent Guideline · Internal use only</footer>
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
