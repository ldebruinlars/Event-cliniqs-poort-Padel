"""Schrijft vier poster-varianten (poster-a.html t/m poster-d.html) met dezelfde tekst en assets.
Tekst en spelers staan hieronder één keer; de lay-out verschilt per variant.
Daarna: ./render.sh poster-a.html poster-a  (enz.)"""

T = {
    'kicker': 'Training + onderlinge wedstrijd · publiek welkom',
    'h1': 'Twee Spaanse padelprofs',
    'h2': 'trainen bij Poort Padel',
    'lead': 'Kom kijken naar hun training en hun onderlinge wedstrijd in Almere Poort.',
    'date': 'Zondag 27 september 2026',
    'time': '18<span class="c">:</span>30 – 20<span class="c">:</span>00',  # dubbele punt rechtop en met ruimte (class c)
    'cta': 'Gratis toegang',
    'cta2': 'kom kijken',
    'where': 'Neonweg 62 · Almere Poort',
    'site': 'poortpadel.nl',
    'tag': 'MEET • SMASH • RELAX',
}
P1 = {'first': 'Guille', 'last': 'Collado', 'rank': 'Top 40 van de wereld',
      'facts': 'Wereldkampioen U-18 2023<br>Meervoudig Spaans kampioen · Dropshot', 'handle': '@guilleecollado__',
      'img': 'build/collado-profile-duotone.jpg'}
P2 = {'first': 'Enrique', 'last': 'Goenaga', 'rank': 'Top 60 van de wereld',
      'facts': 'Tweevoudig Spaans kampioen<br>HEAD Padel', 'handle': '@enri_goenaga',
      'img': 'build/goenaga-duotone.jpg'}

from PIL import Image


def make_pattern(color, alpha, out, pw=86, gx=30, gy=26):
    """Tegel met twee verspringende P's uit het Poort Padel-logo; kleur/alpha bepalen hoe subtiel het patroon is."""
    g = Image.open('build/p-poort-padel.png').convert('RGBA')
    g = g.resize((pw, int(g.height * pw / g.width)), Image.LANCZOS)
    a = g.split()[3].point(lambda v: int(v * alpha))
    glyph = Image.new('RGBA', g.size, color + (0,)); glyph.putalpha(a)
    tw, th = 2 * (pw + gx), 2 * (g.height + gy)
    tile = Image.new('RGBA', (tw, th), (0, 0, 0, 0))
    tile.alpha_composite(glyph, (0, 0)); tile.alpha_composite(glyph, (pw + gx, g.height + gy))
    tile.save(out)


make_pattern((255, 255, 255), 0.085, 'build/p-pattern-groen.png')
make_pattern((20, 48, 42), 0.07, 'build/p-pattern-lime.png')

FONTS = """
@font-face{font-family:"Poppins";font-weight:900;font-style:italic;src:url(fonts/Poppins-BlackItalic.ttf)}
@font-face{font-family:"Poppins";font-weight:900;font-style:normal;src:url(fonts/Poppins-Black.ttf)}
@font-face{font-family:"Poppins";font-weight:800;font-style:italic;src:url(fonts/Poppins-ExtraBoldItalic.ttf)}
@font-face{font-family:"Poppins";font-weight:700;font-style:italic;src:url(fonts/Poppins-BoldItalic.ttf)}
@font-face{font-family:"Poppins";font-weight:600;font-style:normal;src:url(fonts/Poppins-SemiBold.ttf)}
@font-face{font-family:"Poppins";font-weight:500;font-style:normal;src:url(fonts/Poppins-Medium.ttf)}
"""

BASE = """
:root{--lime:#CDFD50;--green:#355B52;--green-dark:#1F3B35;--ink:#14302A;--white:#FFFFFF;--pad:56px}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden;background:var(--green) url(build/p-pattern-groen.png) 0 0 repeat}
body{font-family:"Poppins",Arial,sans-serif;color:var(--white);position:relative;-webkit-font-smoothing:antialiased}
.upper{text-transform:uppercase}
/* logobalk bovenaan: All Court Academy x Poort Padel, duidelijk los van de kop */
.band{position:absolute;top:0;left:0;right:0;height:112px;background:var(--green-dark);display:flex;align-items:center;justify-content:space-between;padding:0 var(--pad);border-bottom:3px solid var(--lime)}
.band .logos{display:flex;align-items:center;gap:22px}
.band .logos img.aca{height:52px}
.band .logos img.pp{height:46px}
.band .logos .x{color:var(--lime);font-weight:900;font-size:30px;line-height:1}
.tag{background:var(--lime);color:var(--ink);font-weight:700;font-style:italic;font-size:17px;letter-spacing:3px;padding:8px 20px;transform:skewX(-12deg)}
.tag span{display:inline-block;transform:skewX(12deg)}
.kicker{display:inline-block;background:var(--green-dark);color:var(--white);border:2px solid rgba(255,255,255,.35);font-weight:800;font-style:italic;font-size:20px;letter-spacing:1.5px;padding:8px 20px;transform:skewX(-12deg)}
.kicker span{display:inline-block;transform:skewX(12deg)}
.headline{font-weight:900;font-style:italic;line-height:1.02;letter-spacing:-1px}
.lime{color:var(--lime)}
.c{font-style:normal;letter-spacing:0;margin:0 .05em 0 .03em;position:relative;top:-.03em}
.panel{position:absolute;overflow:hidden}
.panel img{position:absolute;width:100%;height:100%;object-fit:cover}
.panel::after{content:"";position:absolute;left:0;right:0;bottom:0;height:62%;background:linear-gradient(to top,rgba(10,26,22,.96) 0%,rgba(10,26,22,.75) 45%,rgba(10,26,22,0) 100%)}
.caption{position:absolute;z-index:2}
.caption.l{text-align:left}.caption.r{text-align:right}
.caption .flag{font-size:18px;font-weight:600;letter-spacing:2px;opacity:.9;margin-bottom:4px}
.caption .first{font-weight:700;font-style:italic;font-size:30px;letter-spacing:1px;line-height:1}
.caption .last{font-weight:900;font-style:italic;font-size:64px;line-height:.98;letter-spacing:-1px;margin:2px 0 10px}
.caption .rank{display:inline-block;background:var(--lime);color:var(--ink);font-weight:800;font-style:italic;font-size:20px;letter-spacing:1.5px;padding:6px 14px;transform:skewX(-12deg);margin-bottom:10px}
.caption .rank span{display:inline-block;transform:skewX(12deg)}
.caption .fact{font-size:19px;font-weight:500;line-height:1.35;opacity:.95;text-transform:none}
.caption .handle{font-size:18px;font-weight:600;color:var(--lime);margin-top:6px;text-transform:none}
.cta{display:inline-block;background:var(--lime);color:var(--ink);font-weight:900;font-style:italic;font-size:30px;line-height:1;padding:16px 34px;transform:skewX(-12deg)}
.cta span{display:inline-block;transform:skewX(12deg)}
.cta small{font-size:24px;font-weight:700;letter-spacing:1px;margin-left:10px}
.footer{position:absolute;left:var(--pad);right:var(--pad);bottom:36px;display:flex;align-items:baseline;justify-content:space-between;border-top:2px solid rgba(205,253,80,.5);padding-top:16px}
.footer .where{font-size:23px;font-weight:600}
.footer .where b{color:var(--lime);font-weight:800;font-style:italic;font-size:25px}
.footer .site{font-size:22px;font-weight:600;letter-spacing:3px;color:var(--lime)}
"""

PATTERN_JS = ""


def band():
    return f"""<div class="band">
  <div class="logos"><img class="aca" src="build/logo-all-court-academy-wit.png" alt="All Court Academy"><span class="x">×</span><img class="pp" src="build/logo-poort-padel-wit.png" alt="Poort Padel"></div>
  <div class="tag"><span>{T['tag']}</span></div>
</div>"""


def caption(p, side):
    return f"""<div class="caption {side} upper">
    <div class="flag">Spanje</div>
    <div class="first">{p['first']}</div>
    <div class="last">{p['last']}</div>
    <div class="rank"><span>{p['rank']}</span></div>
    <div class="fact">{p['facts']}</div>
    <div class="handle">{p['handle']}</div>
  </div>"""


def footer():
    return f"""<div class="footer"><div class="where"><b>POORT PADEL</b> · {T['where']}</div><div class="site upper">{T['site']}</div></div>"""


def page(title, css, body):
    return f"""<!doctype html><html lang="nl"><head><meta charset="utf-8"><title>{title}</title><style>{FONTS}{BASE}{css}</style></head>
<body>
{body}
{PATTERN_JS}</body></html>"""


# ---------- A: tweeluik, rustige kop ----------
CSS_A = """
.kick{position:absolute;top:146px;left:var(--pad)}
.headline{position:absolute;top:200px;left:var(--pad);right:var(--pad);font-size:60px}
.photos{position:absolute;top:352px;left:0;right:0;height:640px;background:var(--green-dark)}
.panel{top:0;bottom:0}
.panel.left{left:0;width:615px;clip-path:polygon(0 0,100% 0,calc(100% - 150px) 100%,0 100%)}
.panel.right{left:465px;width:615px;clip-path:polygon(150px 0,100% 0,100% 100%,0 100%)}
.panel.left img{object-position:45% 0%}
.panel.right img{object-position:60% 0%}
.stripe{position:absolute;top:0;bottom:0;left:0;width:100%;background:var(--lime);clip-path:polygon(606px 0,624px 0,474px 100%,456px 100%)}
.caption{bottom:34px}.caption.l{left:var(--pad)}.caption.r{right:var(--pad)}
.when{position:absolute;top:1016px;left:var(--pad);right:var(--pad)}
.when .date{font-weight:900;font-style:italic;font-size:60px;line-height:1;color:var(--lime);letter-spacing:-1px}
.when .time{font-weight:900;font-style:italic;font-size:90px;line-height:1;letter-spacing:-3px;margin-top:6px}
.when .cta{margin:16px 0 0 8px}
"""
BODY_A = f"""{band()}
<div class="kick"><div class="kicker"><span>{T['kicker']}</span></div></div>
<div class="headline upper"><span class="lime">{T['h1']}</span><br>{T['h2']}</div>
<div class="photos">
  <div class="panel left"><img src="{P1['img']}" alt="{P1['first']} {P1['last']}"></div>
  <div class="panel right"><img src="{P2['img']}" alt="{P2['first']} {P2['last']}"></div>
  <div class="stripe"></div>
  {caption(P1, 'l')}
  {caption(P2, 'r')}
</div>
<div class="when upper">
  <div class="date">{T['date']}</div>
  <div class="time">{T['time']}</div>
  <div class="cta"><span>{T['cta']} <small>· {T['cta2']}</small></span></div>
</div>
{footer()}"""

# ---------- B: datum bovenaan in lime blok ----------
CSS_B = """
.datebox{position:absolute;top:140px;left:var(--pad);right:var(--pad);background:var(--lime);color:var(--ink);transform:skewX(-8deg);padding:22px 36px;display:flex;align-items:center;justify-content:space-between}
.datebox>div{transform:skewX(8deg)}
.datebox .date{font-weight:900;font-style:italic;font-size:37px;line-height:1;letter-spacing:-1px}
.datebox .time{font-weight:900;font-style:italic;font-size:72px;line-height:1;letter-spacing:-2px;margin-top:4px}
.datebox .free{text-align:right;font-weight:900;font-style:italic;font-size:30px;line-height:1.05;border-left:3px solid var(--ink);padding-left:26px}
.datebox .free small{display:block;font-size:20px;font-weight:700;letter-spacing:1.5px;margin-top:6px}
.headline{position:absolute;top:352px;left:var(--pad);right:var(--pad);font-size:58px}
.lead{position:absolute;top:478px;left:var(--pad);right:var(--pad);font-size:21px;font-weight:500;opacity:.92}
.photos{position:absolute;top:530px;left:0;right:0;height:660px;background:var(--green-dark)}
.panel{top:0;bottom:0}
.panel.left{left:0;width:615px;clip-path:polygon(0 0,100% 0,calc(100% - 150px) 100%,0 100%)}
.panel.right{left:465px;width:615px;clip-path:polygon(150px 0,100% 0,100% 100%,0 100%)}
.panel.left img{object-position:45% 0%}
.panel.right img{object-position:60% 0%}
.stripe{position:absolute;top:0;bottom:0;left:0;width:100%;background:var(--lime);clip-path:polygon(606px 0,624px 0,474px 100%,456px 100%)}
.caption{bottom:34px}.caption.l{left:var(--pad)}.caption.r{right:var(--pad)}
.footer{bottom:56px}
"""
BODY_B = f"""{band()}
<div class="datebox upper">
  <div><div class="date">{T['date']}</div><div class="time">{T['time']}</div></div>
  <div class="free">{T['cta']}<small>{T['cta2']}</small></div>
</div>
<div class="headline upper">{T['h1']}<br><span class="lime">{T['h2']}</span></div>
<div class="lead">{T['lead']}</div>
<div class="photos">
  <div class="panel left"><img src="{P1['img']}" alt="{P1['first']} {P1['last']}"></div>
  <div class="panel right"><img src="{P2['img']}" alt="{P2['first']} {P2['last']}"></div>
  <div class="stripe"></div>
  {caption(P1, 'l')}
  {caption(P2, 'r')}
</div>
{footer()}"""

# ---------- C: gestapeld, foto's over de volle breedte ----------
CSS_C = """
.kick{position:absolute;top:140px;left:var(--pad)}
.headline{position:absolute;top:192px;left:var(--pad);right:var(--pad);font-size:56px}
.photos{position:absolute;top:320px;left:0;right:0;height:760px;background:var(--green-dark)}
.panel{left:0;width:100%}
.panel.top{top:0;height:420px;clip-path:polygon(0 0,100% 0,100% 82%,0 100%)}
.panel.bottom{top:344px;height:416px;clip-path:polygon(0 18%,100% 0,100% 100%,0 100%)}
.panel.top img{object-position:50% 8%}
.panel.bottom img{object-position:50% 12%}
.panel::after{height:80%;background:linear-gradient(to right,rgba(10,26,22,.95) 0%,rgba(10,26,22,.7) 40%,rgba(10,26,22,0) 70%)}
.panel.bottom::after{background:linear-gradient(to left,rgba(10,26,22,.95) 0%,rgba(10,26,22,.7) 40%,rgba(10,26,22,0) 70%)}
.stripe{position:absolute;left:0;width:100%;top:0;height:100%;background:var(--lime);clip-path:polygon(0 54%,100% 44%,100% 46.4%,0 56.4%)}
.caption.l{left:var(--pad);top:60px}.caption.r{right:var(--pad);bottom:40px}
.caption .last{font-size:60px}
.when{position:absolute;top:1104px;left:var(--pad);right:var(--pad);display:flex;align-items:center;justify-content:space-between}
.when .date{font-weight:900;font-style:italic;font-size:40px;line-height:1;color:var(--lime);letter-spacing:-1px}
.when .time{font-weight:900;font-style:italic;font-size:74px;line-height:1;letter-spacing:-2px;margin-top:4px}
.when .cta{font-size:26px;padding:14px 26px}
.when .cta small{display:block;margin:6px 0 0;font-size:19px}
.footer{bottom:30px;padding-top:12px}
"""
BODY_C = f"""{band()}
<div class="kick"><div class="kicker"><span>{T['kicker']}</span></div></div>
<div class="headline upper">{T['h1']} <span class="lime">{T['h2']}</span></div>
<div class="photos">
  <div class="panel top"><img src="{P1['img']}" alt="{P1['first']} {P1['last']}" style="object-position:70% 8%"></div>
  <div class="panel bottom"><img src="{P2['img']}" alt="{P2['first']} {P2['last']}" style="object-position:30% 12%"></div>
  <div class="stripe"></div>
  {caption(P1, 'l')}
  {caption(P2, 'r')}
</div>
<div class="when upper">
  <div><div class="date">{T['date']}</div><div class="time">{T['time']}</div></div>
  <div class="cta"><span>{T['cta']}<small>{T['cta2']}</small></span></div>
</div>
{footer()}"""

# ---------- D: lime achtergrond, donkergroene tekst ----------
CSS_D = """
html,body{background:var(--lime) url(build/p-pattern-lime.png) 0 0 repeat}
body{color:var(--ink)}
.band{background:var(--green-dark);border-bottom:none}
.kick{position:absolute;top:146px;left:var(--pad)}
.kicker{background:var(--green-dark);color:var(--lime);border-color:var(--green-dark)}
.headline{position:absolute;top:200px;left:var(--pad);right:var(--pad);font-size:60px;color:var(--ink)}
.headline .inv{display:inline-block;background:var(--green-dark);color:var(--lime);padding:2px 18px 6px;transform:skewX(-8deg);margin-top:6px}
.headline .inv span{display:inline-block;transform:skewX(8deg)}
.photos{position:absolute;top:360px;left:0;right:0;height:640px;background:var(--green-dark)}
.panel{top:0;bottom:0}
.panel.left{left:0;width:615px;clip-path:polygon(0 0,100% 0,calc(100% - 150px) 100%,0 100%)}
.panel.right{left:465px;width:615px;clip-path:polygon(150px 0,100% 0,100% 100%,0 100%)}
.panel.left img{object-position:45% 0%}
.panel.right img{object-position:60% 0%}
.stripe{position:absolute;top:0;bottom:0;left:0;width:100%;background:var(--lime);clip-path:polygon(606px 0,624px 0,474px 100%,456px 100%)}
.caption{bottom:34px;color:var(--white)}.caption.l{left:var(--pad)}.caption.r{right:var(--pad)}
.when{position:absolute;top:1024px;left:var(--pad);right:var(--pad)}
.when .date{font-weight:900;font-style:italic;font-size:60px;line-height:1;letter-spacing:-1px}
.when .time{font-weight:900;font-style:italic;font-size:90px;line-height:1;letter-spacing:-3px;margin-top:6px}
.cta{background:var(--green-dark);color:var(--lime);margin:16px 0 0 8px}
.footer{border-top:2px solid rgba(20,48,42,.4)}
.footer .where b,.footer .site{color:var(--ink)}
"""
BODY_D = f"""{band()}
<div class="kick"><div class="kicker"><span>{T['kicker']}</span></div></div>
<div class="headline upper">{T['h1']}<br><span class="inv"><span>{T['h2']}</span></span></div>
<div class="photos">
  <div class="panel left"><img src="{P1['img']}" alt="{P1['first']} {P1['last']}"></div>
  <div class="panel right"><img src="{P2['img']}" alt="{P2['first']} {P2['last']}"></div>
  <div class="stripe"></div>
  {caption(P1, 'l')}
  {caption(P2, 'r')}
</div>
<div class="when upper">
  <div class="date">{T['date']}</div>
  <div class="time">{T['time']}</div>
  <div class="cta"><span>{T['cta']} <small>· {T['cta2']}</small></span></div>
</div>
{footer()}"""

for name, css, body in [('a', CSS_A, BODY_A), ('b', CSS_B, BODY_B), ('c', CSS_C, BODY_C), ('d', CSS_D, BODY_D)]:
    open(f'poster-{name}.html', 'w').write(page(f'Goenaga & Collado bij Poort Padel, variant {name.upper()}', css, body))
    print('poster-%s.html' % name)
