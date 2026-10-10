"""Bouwt tien posterversies (Instagram-feed 4:5, 1080x1350) van de Halloween Padel Special.

Drie richtingen op basis van de goedgekeurde pompoenspeler:
  01-03  Poort Padel-stijl (donkergroen + lime)
  04-06  All Court Academy-stijl (navy + oranje)
  07-10  serieuzer en enger

De tekst staat in TEKST hieronder en is voor alle versies gelijk; alleen de opmaak verschilt.
Gebruik: python3 -P build.py && ./render.sh
"""
from pathlib import Path

HERE = Path(__file__).parent

# TEKST
KICKER = 'Poort Padel × All Court Academy'
H1 = 'HALLOWEEN'
H2 = 'PADEL SPECIAL'
DATE = 'ZATERDAG 31 OKTOBER'
OFFER_A, OFFER_B, OFFER_C = 'KOM VERKLEED =', '50% KORTING', 'OP JE BAAN'
SUB = 'Boek je baan via <b>Playtomic</b> en stap in kostuum de baan op.'
FINE = 'Korting per verklede speler, alleen op zaterdag 31 oktober. Masker of schmink telt ook.'
WHERE = '<b>Neonweg 62 · Almere Poort</b><br>poortpadel.nl'

FONTS = """
@font-face{font-family:Creep;src:url(../fonts/Creepster-Regular.ttf)}
@font-face{font-family:Anton;src:url(../fonts/Anton-Regular.ttf)}
@font-face{font-family:Bungee;src:url(../fonts/Bungee-Regular.ttf)}
@font-face{font-family:Graduate;src:url(../fonts/Graduate-Regular.ttf)}
@font-face{font-family:Oswald;font-weight:200 700;src:url(../fonts/Oswald-VF.ttf)}
@font-face{font-family:Cinzel;font-weight:400 900;src:url(../fonts/Cinzel-VF.ttf)}
@font-face{font-family:Eater;src:url(../fonts/Eater-Regular.ttf)}
@font-face{font-family:Nosifer;src:url(../fonts/Nosifer-Regular.ttf)}
@font-face{font-family:Monoton;src:url(../fonts/Monoton-Regular.ttf)}
@font-face{font-family:Fraktur;src:url(../fonts/UnifrakturMaguntia-Book.ttf)}
@font-face{font-family:Fell;src:url(../fonts/IMFellEnglish-Regular.ttf)}
@font-face{font-family:Poppins;font-weight:900;font-style:italic;src:url(../fonts/Poppins-BlackItalic.ttf)}
@font-face{font-family:Poppins;font-weight:900;font-style:normal;src:url(../fonts/Poppins-Black.ttf)}
@font-face{font-family:Poppins;font-weight:800;font-style:italic;src:url(../fonts/Poppins-ExtraBoldItalic.ttf)}
@font-face{font-family:Poppins;font-weight:700;font-style:italic;src:url(../fonts/Poppins-BoldItalic.ttf)}
@font-face{font-family:Poppins;font-weight:600;font-style:normal;src:url(../fonts/Poppins-SemiBold.ttf)}
@font-face{font-family:Poppins;font-weight:500;font-style:normal;src:url(../fonts/Poppins-Medium.ttf)}
"""

BASE = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{position:relative;font-family:Poppins,Arial,sans-serif;color:#fff;-webkit-font-smoothing:antialiased}
.art{position:absolute;left:0;width:1080px;height:1446px;background-size:1080px 1446px;background-repeat:no-repeat}
.shade{position:absolute;left:0;right:0;bottom:0}
.abs{position:absolute}
.c{text-align:center}
.footer{position:absolute;left:56px;right:56px;bottom:30px;display:flex;align-items:center;justify-content:space-between;padding-top:16px}
.footer .pp{height:50px}
.footer .aca{height:48px}
.footer .where{text-align:center;font-weight:600;font-size:20px;line-height:1.3}
"""


def footer(cls=''):
    return (f'<div class="footer {cls}"><img class="pp" src="../build/logo-poort-padel-wit.png" alt="Poort Padel">'
            f'<div class="where">{WHERE}</div>'
            f'<img class="aca" src="../build/logo-all-court-academy-wit.png" alt="All Court Academy"></div>')


def offer(cls='offer'):
    return (f'<div class="{cls}"><div><div class="a">{OFFER_A}</div><div class="b">{OFFER_B}</div>'
            f'<div class="c2">{OFFER_C}</div></div></div>')


V = {}

# 01 Poort Padel: groene smash, Poort Padel-typografie, lime aanbieding
V['01-pp-groen-smash'] = ('01-pp-groen-smash.jpg', """
body{background:#0d1f1b}
.art{top:-40px}
.shade{height:700px;background:linear-gradient(to bottom,rgba(13,31,27,0),rgba(13,31,27,.85) 32%,#0d1f1b 62%)}
.block{left:60px;right:60px;top:640px}
.k{font-weight:800;font-style:italic;font-size:24px;letter-spacing:4px;color:#CDFD50;text-transform:uppercase;text-shadow:0 2px 10px #000,0 0 4px #000}
.h1{font-family:Creep;font-size:138px;line-height:.9;color:#CDFD50;letter-spacing:4px;text-shadow:0 0 30px rgba(205,253,80,.45),0 6px 0 #1d3a33}
.h2{font-weight:900;font-style:italic;font-size:66px;line-height:1;letter-spacing:6px;margin-top:-2px}
.date{display:inline-block;margin-top:14px;font-weight:900;font-style:italic;font-size:36px;border-top:4px solid #355B52;border-bottom:4px solid #355B52;padding:8px 22px}
.offer{display:inline-block;margin-top:20px;background:#CDFD50;color:#0d1f1b;transform:skewX(-10deg) rotate(-2deg);padding:12px 44px 14px;box-shadow:0 0 44px rgba(205,253,80,.35)}
.offer>div{transform:skewX(10deg)}
.offer .a,.offer .c2{font-weight:800;font-style:italic;font-size:26px;letter-spacing:2px}
.offer .b{font-weight:900;font-style:italic;font-size:80px;line-height:.95;letter-spacing:-2px}
.sub{margin-top:18px;font-weight:600;font-size:24px}.sub b{color:#CDFD50}
.fine{margin-top:6px;font-weight:500;font-size:17px;opacity:.7}
.footer{border-top:2px solid rgba(205,253,80,.45)}
.footer .where b{color:#CDFD50}
""", lambda: f"""
<div class="block abs c"><div class="k">{KICKER}</div><div class="h1">{H1}</div><div class="h2">{H2}</div>
<div class="date">{DATE}</div><br>{offer()}<div class="sub">{SUB}</div><div class="fine">{FINE}</div></div>{footer()}""")

# 02 Poort Padel: heldenpose, strak links uitgelijnd, P-patroon, lime sticker
V['02-pp-heldenpose'] = ('02-pp-heldenpose.jpg', """
body{background:#1c3a33}
.art{top:-20px}
.pat{position:absolute;left:0;right:0;top:760px;bottom:0;background:url(../build/p-pattern-groen.png) repeat;background-size:540px auto;-webkit-mask-image:linear-gradient(to bottom,transparent,#000 40%)}
.shade{height:640px;background:linear-gradient(to bottom,rgba(28,58,51,0),#1c3a33 28%)}
.block{left:64px;top:770px;width:660px}
.k{font-weight:800;font-style:italic;font-size:22px;letter-spacing:4px;color:#CDFD50;text-transform:uppercase}
.h1{font-family:Anton;font-size:150px;line-height:.95;letter-spacing:1px;margin-top:4px}
.h2{font-family:Anton;font-size:76px;line-height:1;color:#CDFD50;letter-spacing:2px}
.date{margin-top:14px;font-weight:900;font-style:italic;font-size:34px;letter-spacing:1px}
.sub{margin-top:10px;font-weight:600;font-size:21px;line-height:1.35;width:640px}.sub b{color:#CDFD50}
.fine{margin-top:6px;font-weight:500;font-size:16px;opacity:.7;width:620px}
.offer{position:absolute;right:58px;top:850px;width:300px;height:300px;border-radius:50%;background:#CDFD50;color:#1c3a33;display:flex;align-items:center;justify-content:center;text-align:center;transform:rotate(8deg);box-shadow:0 0 0 8px #1c3a33,0 0 0 12px #CDFD50,0 0 60px rgba(205,253,80,.4)}
.offer .a,.offer .c2{font-weight:800;font-style:italic;font-size:22px;letter-spacing:1px}
.offer .b{font-family:Anton;font-size:64px;line-height:1;margin:4px 0}
.footer{border-top:2px solid rgba(205,253,80,.45)}
.footer .where b{color:#CDFD50}
""", lambda: f"""
<div class="pat"></div>
<div class="block abs"><div class="k">{KICKER}</div><div class="h1">{H1}</div><div class="h2">{H2}</div>
<div class="date">{DATE}</div><div class="sub">{SUB}</div><div class="fine">{FINE}</div></div>
<div class="offer"><div><div class="a">{OFFER_A}</div><div class="b">50%<br>KORTING</div><div class="c2">{OFFER_C}</div></div></div>{footer()}""")

# 03 Poort Padel: door de glaswand, schuine actietypografie en lime lint
V['03-pp-glaswand'] = ('03-pp-glaswand.jpg', """
body{background:#0b1c18}
.art{top:-60px}
.shade{height:650px;background:linear-gradient(to bottom,rgba(11,28,24,0),rgba(11,28,24,.9) 30%,#0b1c18 60%)}
.block{left:0;right:0;top:700px;transform:rotate(-5deg)}
.k{display:inline-block;background:#0b1c18;font-weight:800;font-style:italic;font-size:22px;letter-spacing:4px;color:#CDFD50;text-transform:uppercase;padding:4px 16px}
.h1{font-weight:900;font-style:italic;font-size:142px;line-height:.92;letter-spacing:-3px;color:#fff;-webkit-text-stroke:0;text-shadow:6px 6px 0 #355B52,10px 10px 0 #CDFD50}
.h2{font-family:Creep;font-size:84px;line-height:1;color:#CDFD50;letter-spacing:6px;margin-top:4px}
.ribbon{position:absolute;left:-40px;right:-40px;top:1012px;background:#CDFD50;color:#0b1c18;transform:rotate(-5deg);padding:10px 0 12px;text-align:center;box-shadow:0 10px 40px rgba(0,0,0,.5)}
.ribbon .b{font-weight:900;font-style:italic;font-size:58px;line-height:1;letter-spacing:-1px}
.ribbon .b span{font-size:32px;letter-spacing:1px;vertical-align:middle}
.info{left:60px;right:60px;top:1120px}
.date{font-weight:900;font-style:italic;font-size:34px;letter-spacing:1px}
.sub{margin-top:6px;font-weight:600;font-size:22px}.sub b{color:#CDFD50}
.fine{margin-top:4px;font-weight:500;font-size:16px;opacity:.7}
.footer{bottom:24px}
.footer .where b{color:#CDFD50}
""", lambda: f"""
<div class="block abs c"><div class="k">{KICKER}</div><div class="h1">{H1}</div><div class="h2">{H2}</div></div>
<div class="ribbon"><div class="b"><span>{OFFER_A}</span> {OFFER_B} <span>{OFFER_C}</span></div></div>
<div class="info abs c"><div class="date">{DATE}</div><div class="sub">{SUB}</div><div class="fine">{FINE}</div></div>{footer()}""")

# 04 Academy: kidsclinic, speels en vrolijk, navy + oranje
V['04-aca-kidsclinic'] = ('04-aca-kidsclinic.jpg', """
body{background:#0B1420}
.art{top:-10px}
.shade{height:640px;background:linear-gradient(to bottom,rgba(11,20,32,0),rgba(11,20,32,.9) 25%,#0B1420 50%)}
.block{left:60px;right:60px;top:760px}
.k{display:inline-block;background:#fff;color:#0B1420;font-weight:800;font-style:italic;font-size:22px;letter-spacing:3px;text-transform:uppercase;padding:6px 18px;border-radius:30px}
.h1{font-family:Bungee;font-size:112px;line-height:1;color:#FF7A1A;margin-top:14px;text-shadow:0 6px 0 #7a3000}
.h2{font-family:Bungee;font-size:52px;line-height:1;color:#fff;letter-spacing:4px;margin-top:4px}
.row{display:flex;gap:22px;justify-content:center;align-items:stretch;margin-top:22px}
.date{background:#132235;border:3px solid #FF7A1A;border-radius:22px;padding:14px 22px;font-family:Bungee;font-size:30px;line-height:1.1;display:flex;align-items:center}
.offer{background:#FF7A1A;color:#0B1420;border-radius:22px;padding:12px 30px;box-shadow:0 8px 0 #7a3000}
.offer .a,.offer .c2{font-weight:800;font-style:italic;font-size:22px;letter-spacing:1px}
.offer .b{font-family:Bungee;font-size:52px;line-height:1}
.sub{margin-top:22px;font-weight:600;font-size:22px}.sub b{color:#CCFF00}
.fine{margin-top:4px;font-weight:500;font-size:16px;opacity:.7}
.footer{border-top:2px solid rgba(255,122,26,.5)}
.footer .where b{color:#FF7A1A}
""", lambda: f"""
<div class="block abs c"><div class="k">{KICKER}</div><div class="h1">{H1}</div><div class="h2">{H2}</div>
<div class="row"><div class="date">ZATERDAG<br>31 OKTOBER</div>{offer()}</div>
<div class="sub">{SUB}</div><div class="fine">{FINE}</div></div>{footer()}""")

# 05 Academy: varsity / college-sportposter
V['05-aca-varsity'] = ('05-aca-varsity.jpg', """
body{background:#0B1420}
.art{top:-70px}
.shade{height:560px;background:linear-gradient(to bottom,rgba(11,20,32,0),#0B1420 22%)}
.block{left:50px;right:50px;top:790px}
.k{display:inline-block;background:#0B1420;padding:4px 16px;font-family:Graduate;font-size:22px;letter-spacing:4px;color:#FBF2DD}
.h1{font-family:Graduate;font-size:118px;line-height:1;color:#FF7A1A;letter-spacing:2px;-webkit-text-stroke:3px #FBF2DD;text-shadow:7px 7px 0 #FBF2DD;margin-top:6px}
.h2{font-family:Graduate;font-size:46px;line-height:1;color:#FBF2DD;letter-spacing:10px;margin-top:14px}
.line{display:flex;align-items:center;gap:18px;justify-content:center;margin-top:18px}
.line i{flex:1;height:3px;background:#FF7A1A}
.date{font-family:Graduate;font-size:30px;color:#FBF2DD;letter-spacing:3px}
.pennant{position:absolute;left:0;top:1078px;height:156px;width:700px;background:#FF7A1A;clip-path:polygon(0 0,100% 50%,0 100%);color:#0B1420;padding:16px 0 0 50px}
.pennant .a{font-family:Graduate;font-size:20px;letter-spacing:2px}
.pennant .b{font-family:Graduate;font-size:56px;line-height:1}
.pennant .c2{font-family:Graduate;font-size:20px;letter-spacing:2px}
.info{right:50px;top:1100px;width:300px;text-align:right}
.sub{font-weight:600;font-size:19px;line-height:1.3}.sub b{color:#FF7A1A}
.fine{margin-top:6px;font-weight:500;font-size:14px;opacity:.7}
.footer{border-top:2px solid rgba(251,242,221,.4)}
.footer .where b{color:#FF7A1A}
""", lambda: f"""
<div class="block abs c"><div class="k">{KICKER.upper()}</div><div class="h1">{H1}</div><div class="h2">{H2}</div>
<div class="line"><i></i><div class="date">{DATE}</div><i></i></div></div>
<div class="pennant"><div class="a">{OFFER_A}</div><div class="b">{OFFER_B}</div><div class="c2">{OFFER_C}</div></div>
<div class="info abs"><div class="sub">{SUB}</div><div class="fine">{FINE}</div></div>{footer()}""")

# 06 Academy: trainingssessie, scorebord met drie vakken
V['06-aca-training'] = ('06-aca-training.jpg', """
body{background:#0B1420}
.art{top:-40px}
.shade{height:640px;background:linear-gradient(to bottom,rgba(11,20,32,0),rgba(11,20,32,.92) 28%,#0B1420 52%)}
.block{left:60px;right:60px;top:740px}
.k{display:inline-block;background:#0B1420;padding:2px 16px;font-family:Oswald;font-weight:500;font-size:24px;letter-spacing:6px;color:#FF7A1A;text-transform:uppercase}
.h1{font-family:Oswald;font-weight:700;font-size:150px;line-height:.95;letter-spacing:2px;text-transform:uppercase}
.h2{font-family:Oswald;font-weight:700;font-size:58px;line-height:1;letter-spacing:16px;color:#FF7A1A;margin-top:2px}
.board{display:grid;grid-template-columns:1fr 1.5fr 1fr;margin-top:24px;border:3px solid #FF7A1A;border-radius:14px;overflow:hidden}
.board>div{padding:12px 8px;display:flex;flex-direction:column;justify-content:center}
.board>div+div{border-left:3px solid #FF7A1A}
.board .l{font-family:Oswald;font-weight:500;font-size:18px;letter-spacing:3px;color:#9fb0c4;text-transform:uppercase}
.board .v{font-family:Oswald;font-weight:700;font-size:40px;line-height:1.05;text-transform:uppercase}
.board .mid{background:#FF7A1A;color:#0B1420}
.board .mid .l{color:#0B1420}
.board .mid .v{font-size:62px}
.sub{margin-top:18px;font-weight:600;font-size:22px}.sub b{color:#FF7A1A}
.fine{margin-top:4px;font-weight:500;font-size:16px;opacity:.7}
.footer{border-top:2px solid rgba(255,122,26,.5)}
.footer .where b{color:#FF7A1A}
""", lambda: f"""
<div class="block abs c"><div class="k">{KICKER}</div><div class="h1">{H1}</div><div class="h2">{H2}</div>
<div class="board"><div><span class="l">Zaterdag</span><span class="v">31 okt</span></div>
<div class="mid"><span class="l">Kom verkleed</span><span class="v">50% korting</span></div>
<div><span class="l">Korting</span><span class="v">op je baan</span></div></div>
<div class="sub">{SUB}</div><div class="fine">{FINE}</div></div>{footer()}""")

# 07 Eng: horrorfilmposter met filmcredits
V['07-eng-horrorfilm'] = ('07-eng-horrorfilm.jpg', """
body{background:#05080b}
.art{top:-30px}
.shade{height:560px;background:linear-gradient(to bottom,rgba(5,8,11,0),rgba(5,8,11,.85) 35%,#05080b 70%)}
.top{left:60px;right:60px;top:46px;font-family:Cinzel;font-weight:600;font-size:22px;letter-spacing:8px;color:#d9d2c5;text-transform:uppercase}
.tag{margin-bottom:6px;text-shadow:0 0 10px #000,0 0 20px #000;font-family:Cinzel;font-weight:400;font-size:28px;letter-spacing:2px;color:#d9d2c5;font-style:italic}
.block{left:40px;right:40px;top:730px}
.h1{font-family:Cinzel;font-weight:900;font-size:128px;line-height:1;letter-spacing:10px;color:#f1e9dc;text-shadow:0 0 30px rgba(255,110,20,.55),0 0 80px rgba(255,90,0,.35)}
.h2{font-family:Cinzel;font-weight:700;font-size:40px;letter-spacing:22px;color:#FF7A1A;margin-top:6px}
.offer{margin-top:26px;display:inline-block;border-top:1px solid #FF7A1A;border-bottom:1px solid #FF7A1A;padding:10px 26px}
.offer .t{font-family:Cinzel;font-weight:700;font-size:34px;letter-spacing:4px;color:#f1e9dc}
.offer .t b{color:#FF7A1A;font-weight:900}
.date{margin-top:20px;font-family:Cinzel;font-weight:700;font-size:30px;letter-spacing:8px;color:#f1e9dc}
.credits{left:110px;right:110px;top:1150px;font-family:Oswald;font-weight:300;font-size:19px;line-height:1.3;letter-spacing:2px;color:#9a948a;text-transform:uppercase}
.credits b{font-weight:500;color:#d9d2c5}
.footer{bottom:26px}
.footer .where{font-family:Oswald;font-weight:400;letter-spacing:2px;color:#d9d2c5}
.footer .where b{color:#FF7A1A;font-weight:500}
""", lambda: f"""
<div class="top abs c">Poort Padel &amp; All Court Academy presenteren</div>
<div class="block abs c"><div class="tag">Wie verkleed komt, speelt voor de helft.</div><div class="h1">{H1}</div><div class="h2">{H2}</div>
<div class="offer"><div class="t">KOM VERKLEED = <b>50% KORTING</b> OP JE BAAN</div></div>
<div class="date">ALLEEN OP DE BAAN · 31 OKTOBER</div></div>
<div class="credits abs c">Boek je baan via <b>Playtomic</b> en stap in kostuum de baan op · {FINE} · <b>Zaterdag 31 oktober</b></div>{footer()}""")

# 08 Eng: verlaten baan bij het kerkhof, grafsteen als aanbieding
V['08-eng-kerkhofbaan'] = ('08-eng-kerkhofbaan.jpg', """
body{background:#0e1414}
.art{top:-20px}
.shade{height:640px;background:linear-gradient(to bottom,rgba(14,20,20,0),rgba(14,20,20,.82) 35%,#0e1414 70%)}
.k{left:60px;right:60px;top:50px;font-family:Fell;font-size:30px;font-style:italic;color:#cfd6d2;letter-spacing:1px;text-shadow:0 2px 10px #000}
.block{left:40px;right:40px;top:760px}
.h1{font-family:Eater;font-size:116px;line-height:1;color:#e9e4d6;letter-spacing:2px;text-shadow:0 0 24px rgba(255,122,26,.35),0 4px 0 #000}
.h2{font-family:Fell;font-size:52px;color:#FF7A1A;letter-spacing:10px;margin-top:-2px}
.date{font-family:Fell;font-size:34px;color:#e9e4d6;letter-spacing:4px;margin-top:4px}
.stone{position:absolute;left:330px;width:420px;top:1000px;height:230px;background:linear-gradient(#5d6663,#3f4745);border-radius:200px 200px 10px 10px;border:4px solid #2a302f;box-shadow:inset 0 0 40px rgba(0,0,0,.6),0 12px 30px rgba(0,0,0,.7);text-align:center;padding-top:36px;color:#1b2120}
.stone .a,.stone .c2{font-family:Fell;font-size:24px;letter-spacing:2px;color:#d6dbd8;text-shadow:0 -1px 0 #000}
.stone .b{font-family:Cinzel;font-weight:900;font-size:60px;line-height:1.05;color:#FF7A1A;text-shadow:0 2px 0 #000}
.side{top:1030px;width:260px;font-family:Fell;font-size:21px;line-height:1.3;color:#cfd6d2}
.side.l{left:50px;text-align:right}.side.r{right:50px}
.side b{color:#FF7A1A;font-weight:normal}
.footer{border-top:1px solid rgba(233,228,214,.3)}
.footer .where{font-family:Fell;font-weight:normal;font-size:22px}
.footer .where b{color:#FF7A1A;font-weight:normal}
""", lambda: f"""
<div class="k abs c">Poort Padel &amp; All Court Academy nodigen u uit…</div>
<div class="block abs c"><div class="h1">{H1}</div><div class="h2">{H2}</div><div class="date">Zaterdag 31 oktober</div></div>
<div class="side l abs">Boek je baan via <b>Playtomic</b> en stap in kostuum de baan op.</div>
<div class="stone"><div class="a">KOM VERKLEED</div><div class="b">50%<br></div><div class="b" style="font-size:40px">KORTING</div><div class="c2">OP JE BAAN</div></div>
<div class="side r abs">Per verklede speler, alleen op 31 oktober. Masker of schmink telt ook.</div>{footer()}""")

# 09 Eng: jaren-80 VHS-horror met rode neon
V['09-eng-vhs-neon'] = ('09-eng-vhs-neon.jpg', """
body{background:#050307}
.art{top:-30px}
.shade{height:560px;background:linear-gradient(to bottom,rgba(5,3,7,0),rgba(5,3,7,.75) 35%,rgba(5,3,7,.9) 70%)}
.scan{position:absolute;inset:0;background:repeating-linear-gradient(to bottom,rgba(0,0,0,.18) 0 2px,transparent 2px 5px);pointer-events:none}
.osd{font-family:Oswald;font-weight:500;font-size:30px;letter-spacing:3px;color:#fff;text-shadow:2px 0 #ff2a4a,-2px 0 #2af0ff}
.osd.tl{left:50px;top:40px}.osd.tr{right:50px;top:40px}
.block{left:30px;right:30px;top:745px}
.k{font-family:Oswald;font-weight:400;font-size:22px;letter-spacing:8px;color:#ff9fb0;text-transform:uppercase;display:inline-block;background:#050307;padding:3px 16px}
.h1{font-family:Monoton;font-size:108px;line-height:1.05;color:#ff2a4a;letter-spacing:4px;text-shadow:0 0 10px #ff2a4a,0 0 30px #ff2a4a,0 0 60px #b0003a;margin-top:6px}
.h2{font-weight:900;font-style:italic;font-size:62px;line-height:1;letter-spacing:4px;background:linear-gradient(#ffffff 0%,#d9d9e8 45%,#7a7a96 50%,#f0f0ff 100%);-webkit-background-clip:text;color:transparent;filter:drop-shadow(0 3px 0 #ff2a4a)}
.offer{display:inline-block;margin-top:16px;border:4px solid #ff2a4a;border-radius:10px;padding:10px 34px;box-shadow:0 0 22px #ff2a4a,inset 0 0 22px rgba(255,42,74,.5)}
.offer .a,.offer .c2{font-family:Oswald;font-weight:500;font-size:24px;letter-spacing:4px}
.offer .b{font-weight:900;font-style:italic;font-size:64px;line-height:1;text-shadow:0 0 18px rgba(255,42,74,.8)}
.sub{margin-top:16px;font-weight:600;font-size:22px}.sub b{color:#ff5c77}
.fine{margin-top:4px;font-weight:500;font-size:16px;opacity:.7}
.footer{border-top:2px solid rgba(255,42,74,.5)}
.footer .where b{color:#ff5c77}
""", lambda: f"""
<div class="osd tl abs">▶ PLAY</div><div class="osd tr abs">ZA 31·10 &nbsp;SP</div>
<div class="block abs c"><div class="k">{KICKER}</div><div class="h1">{H1}</div><div class="h2">{H2}</div>
{offer()}<div class="sub">{SUB}</div><div class="fine">{FINE}</div></div>{footer()}<div class="scan"></div>""")

# 10 Eng: gotische houtsnede, fraktur en oranje stempel
V['10-eng-houtsnede'] = ('10-eng-houtsnede.jpg', """
body{background:#0a0908}
.art{top:-14px}
.shade{height:560px;background:linear-gradient(to bottom,rgba(10,9,8,0),#0a0908 18%)}
.frame{position:absolute;left:24px;right:24px;top:24px;bottom:24px;border:3px solid #e9dfc8;outline:1px solid #e9dfc8;outline-offset:-12px;pointer-events:none}
.block{left:60px;right:60px;top:862px}
.k{font-family:Fell;font-size:24px;font-style:italic;color:#e9dfc8;letter-spacing:1px}
.h1{font-family:Fraktur;font-size:128px;line-height:.95;color:#e9dfc8;margin-top:2px}
.h2{font-family:Cinzel;font-weight:700;font-size:38px;letter-spacing:18px;color:#e9dfc8;margin-top:6px}
.orn{color:#d9661c;font-size:22px;letter-spacing:12px;margin:2px 0}
.date{font-family:Cinzel;font-weight:700;font-size:30px;letter-spacing:6px;color:#d9661c}
.stamp{position:absolute;right:64px;top:560px;width:220px;height:220px;border-radius:50%;background:#d9661c;color:#0a0908;display:flex;align-items:center;justify-content:center;text-align:center;transform:rotate(-12deg);box-shadow:0 0 0 6px #0a0908,0 0 0 9px #d9661c}
.stamp .a,.stamp .c2{font-family:Cinzel;font-weight:900;font-size:17px;letter-spacing:1px}
.stamp .b{font-family:Cinzel;font-weight:900;font-size:40px;line-height:1}
.sub{margin-top:14px;font-family:Fell;font-size:25px;color:#e9dfc8}.sub b{color:#d9661c;font-weight:normal}
.fine{margin-top:2px;font-family:Fell;font-style:italic;font-size:19px;color:#b9b09c}
.footer{left:70px;right:70px;bottom:52px}
.footer .where{font-family:Fell;font-weight:normal;font-size:21px;color:#e9dfc8}
.footer .where b{color:#d9661c;font-weight:normal}
.footer .pp{height:42px}.footer .aca{height:40px}
""", lambda: f"""
<div class="block abs c"><div class="k">Poort Padel &amp; All Court Academy presenteren</div><div class="h1">Halloween</div>
<div class="h2">{H2}</div><div class="orn">✦ ✦ ✦</div><div class="date">{DATE}</div>
<div class="sub">Kom verkleed en speel voor de helft. Boek via <b>Playtomic</b>.</div><div class="fine">{FINE}</div></div>
<div class="stamp"><div><div class="a">KOM VERKLEED</div><div class="b">50%<br>KORTING</div><div class="c2">OP JE BAAN</div></div></div>
{footer()}<div class="frame"></div>""")


# 11-14: de enge filmsfeer van 07 met de actie en opmaak van 03 (schuin, lime lint) of 01 (gecentreerd, lime balk)
def spooky(src, art, base, rgb, top=None, shade_h=None):
    _, css, body = V[src]
    css = css.replace('#0b1c18', base).replace('rgba(11,28,24', 'rgba(' + rgb).replace('#0d1f1b', base).replace('rgba(13,31,27', 'rgba(' + rgb)
    if top is not None:
        css += '.art{top:%dpx}' % top
    if shade_h is not None:
        css += '.shade{height:%dpx}' % shade_h
    return (art, css, body)

V['11-eng-glaswand-film'] = spooky('03-pp-glaswand', '11-eng-glaswand-film.jpg', '#06100f', '6,16,15', top=-70)
V['12-eng-smash-kapotglas'] = spooky('01-pp-groen-smash', '12-eng-smash-kapotglas.jpg', '#070d10', '7,13,16', top=-30)
V['13-eng-kerkhof-glaswand'] = spooky('03-pp-glaswand', '13-eng-kerkhof-glaswand.jpg', '#0b0f12', '11,15,18', top=-60)
V['14-eng-duik-scherven'] = spooky('01-pp-groen-smash', '14-eng-duik-scherven.jpg', '#080d12', '8,13,18', top=0)


for name, (art, css, body) in V.items():
    html = f"""<!doctype html><html lang="nl"><head><meta charset="utf-8"><title>Halloween Padel {name}</title>
<style>{FONTS}{BASE}{css}</style></head><body>
<div class="art" style="background-image:url(../artwork/varianten/{art})"></div><div class="shade"></div>
{body()}
</body></html>"""
    (HERE / f'{name}.html').write_text(html, encoding='utf-8')
    print(name)
