"""Bevestigingsmail na betaling, Halloween Padel Special.

Eén sjabloon, twee uitvoeren:
  bevestigingsmail-make.html  met Make-velden, gaat in de Gmail-module van scenario "halloween betaald naar sheet en Moneybird"
  voorbeeld.html              met voorbeelddata, om te bekijken (render.sh maakt er een png van)

Make-velden: 2 = Mollie "Get a payment", 3 = Parse JSON van de metadata
(naam, s2, s3, s4, vps = "ja,ja,nee,ja", telefoon, email, start, eind, uren).
"""
from pathlib import Path

HIER = Path(__file__).parent
SITE = "https://halloween-poort-padel.netlify.app"

NIGHT, DEEP, GLASS, LINE = "#070d10", "#0d181b", "#132326", "#24393b"
FOG, BONE, LIME, PUMPKIN = "#8fa6a0", "#eef3ef", "#cdfd50", "#ff7a1a"
FONT = "Arial,Helvetica,sans-serif"


def speler(i):
    return f"""
              <tr>
                <td style="padding:9px 0;border-top:1px solid {LINE};font:600 15px/1.4 {FONT};color:{BONE}">[[speler{i}]]</td>
                <td align="right" style="padding:9px 0;border-top:1px solid {LINE}"><span style="display:inline-block;background:[[bg{i}]];color:[[fg{i}]];font:700 12px/1 {FONT};letter-spacing:.06em;text-transform:uppercase;padding:6px 10px;border-radius:6px">[[lbl{i}]]</span></td>
              </tr>"""


def stap(n, kop, tekst):
    return f"""
          <tr>
            <td width="44" valign="top" style="padding:0 0 16px"><div style="width:32px;height:32px;border-radius:16px;background:{LIME};color:{NIGHT};font:900 italic 16px/32px {FONT};text-align:center">{n}</div></td>
            <td valign="top" style="padding:0 0 16px;font:15px/1.55 {FONT};color:{FOG}"><b style="color:{BONE}">{kop}</b><br>{tekst}</td>
          </tr>"""


def rij(label, waarde):
    return f"""
              <tr>
                <td valign="top" style="padding:7px 0;font:13px/1.4 {FONT};color:{FOG};width:110px">{label}</td>
                <td valign="top" style="padding:7px 0;font:700 15px/1.4 {FONT};color:{BONE}">{waarde}</td>
              </tr>"""


SJABLOON = f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="dark">
<meta name="supported-color-schemes" content="dark">
<title>Je baan staat vast, Halloween Padel Special</title>
</head>
<body style="margin:0;padding:0;background:{NIGHT}">
<div style="display:none;max-height:0;overflow:hidden;color:{NIGHT}">Betaald en bevestigd: zaterdag 31 oktober, [[start]] tot [[eind]] bij Poort Padel. Kom verkleed!</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{NIGHT}" style="background:{NIGHT}">
  <tr><td align="center" style="padding:20px 12px 36px">
    <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;background:{DEEP};border:1px solid {LINE};border-radius:16px;overflow:hidden">

      <tr><td><a href="{SITE}"><img src="[[img]]/mail-header.jpg" width="600" alt="Halloween Padel: betaald en bevestigd" style="display:block;width:100%;height:auto;border:0"></a></td></tr>

      <tr><td style="padding:30px 32px 6px">
        <p style="margin:0 0 12px;font:900 italic 26px/1.2 {FONT};color:{BONE}">Hoi [[voornaam]], jullie baan staat vast!</p>
        <p style="margin:0;font:16px/1.6 {FONT};color:{FOG}">Je betaling is binnen, dus je boeking is bevestigd. Zet je kostuum vast klaar, want op zaterdag 31 oktober wordt het griezelen bij Poort Padel.</p>
      </td></tr>

      <tr><td style="padding:22px 32px 4px">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{GLASS};border:2px dashed {LIME};border-radius:14px">
          <tr><td style="padding:20px 22px 8px">
            <p style="margin:0 0 6px;font:800 italic 12px/1 {FONT};letter-spacing:.22em;text-transform:uppercase;color:{LIME}">Jouw boeking</p>
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rij("Datum", "Zaterdag 31 oktober 2026")}{rij("Tijd", "[[start]] tot [[eind]] <span style='color:" + FOG + ";font-weight:400'>([[duur]] uur)</span>")}{rij("Waar", "Poort Padel, Neonweg 62, Almere Poort")}{rij("Baan", "Dubbelbaan, het nummer hoor je bij de check-in")}
            </table>
          </td></tr>
          <tr><td style="padding:6px 22px 18px">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{NIGHT};border-radius:10px">
              <tr>
                <td style="padding:14px 16px;font:14px/1.4 {FONT};color:{FOG}">Betaald met iDEAL</td>
                <td align="right" style="padding:14px 16px;font:900 italic 28px/1 {FONT};color:{LIME};white-space:nowrap">€[[bedrag]]</td>
              </tr>
            </table>
          </td></tr>
        </table>
      </td></tr>

      <tr><td style="padding:26px 32px 4px">
        <p style="margin:0 0 4px;font:900 italic 20px/1.2 {FONT};color:{BONE}">Wie spelen er</p>
        <p style="margin:0 0 10px;font:14px/1.5 {FONT};color:{FOG}">[[nverkleed]] van de 4 spelers hebben de Halloween-korting. Doe je best, dus echt verkleed of geschminkt.</p>
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{speler(1)}{speler(2)}{speler(3)}{speler(4)}
        </table>
      </td></tr>

      <tr><td style="padding:28px 32px 6px">
        <p style="margin:0 0 16px;font:900 italic 20px/1.2 {FONT};color:{BONE}">Zo werkt het op de dag</p>
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{stap(1, "Kom 10 minuten van tevoren", "Met z'n vieren naar de bar van Poort Padel, dus uiterlijk 10 minuten voor [[start]].")}{stap(2, "Noem de naam van de boeker", "Wij hebben jullie namen op de lijst staan.")}{stap(3, "Kostuums laten zien en spelen", "Daarna hoor je op welke baan jullie staan. De baan is van jullie tot [[eind]].")}
        </table>
      </td></tr>

      <tr><td style="padding:4px 32px 8px">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
          <td style="border-left:4px solid {PUMPKIN};background:{GLASS};border-radius:0 10px 10px 0;padding:14px 16px;font:14px/1.55 {FONT};color:{FOG}"><b style="color:{PUMPKIN}">Tip:</b> kies een kostuum waarin je veilig kunt spelen. Je moet de bal goed kunnen zien en er mag niets op de baan vallen. Een cape is prima, een masker dat je zicht wegneemt niet. De mooiste outfits zetten we op Instagram.</td>
        </tr></table>
      </td></tr>

      <tr><td align="center" style="padding:26px 32px 8px">
        <table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
          <td bgcolor="{LIME}" style="border-radius:10px"><a href="https://calendar.google.com/calendar/render?action=TEMPLATE&amp;text=Halloween%20Padel%20Special&amp;dates=20261031T[[gstart]]00/20261031T[[geind]]00&amp;ctz=Europe/Amsterdam&amp;location=Poort%20Padel%2C%20Neonweg%2062%2C%20Almere&amp;details=Kom%2010%20minuten%20van%20tevoren%20verkleed%20naar%20de%20bar." style="display:inline-block;padding:14px 26px;font:900 italic 16px/1 {FONT};color:{NIGHT};text-decoration:none">Zet in je agenda</a></td>
        </tr></table>
        <p style="margin:14px 0 0;font:13px/1.5 {FONT}"><a href="https://maps.google.com/?q=Poort+Padel+Neonweg+62+Almere" style="color:{LIME}">Route naar Poort Padel</a> <span style="color:{LINE}">&nbsp;|&nbsp;</span> <a href="{SITE}/#echt-verkleed" style="color:{LIME}">Wat telt als verkleed?</a></p>
      </td></tr>

      <tr><td style="padding:26px 32px 30px">
        <p style="margin:0;font:900 italic 22px/1.2 {FONT};color:{LIME}">Tot snel op de baan!</p>
      </td></tr>

      <tr><td style="padding:22px 32px 26px;border-top:1px solid {LINE};background:{NIGHT}">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
          <td width="50%" valign="middle"><img src="[[img]]/logo-all-court-academy.png" width="150" alt="All Court Academy" style="display:block;border:0;width:150px;height:auto"></td>
          <td width="50%" valign="middle" align="right"><img src="[[img]]/logo-poort-padel.png" width="140" alt="Poort Padel" style="display:block;border:0;width:140px;height:auto;margin-left:auto"></td>
        </tr></table>
        <p style="margin:16px 0 0;font:12px/1.6 {FONT};color:{FOG}">Halloween Padel Special van All Court Academy bij Poort Padel. Vragen of iets wijzigen? Mail <a href="mailto:l.debruin@allcourtacademy.com" style="color:{LIME}">l.debruin@allcourtacademy.com</a> of app <a href="https://wa.me/31615855057" style="color:{LIME}">+31 6 15 85 50 57</a>.</p>
      </td></tr>

    </table>
  </td></tr>
</table>
</body>
</html>
"""

AAN = ("#ff7a1a", "#070d10", "verkleed -50%")
UIT = ("#24393b", "#eef3ef", "gewoon tarief")


def make_velden():
    v = {
        "img": SITE + "/assets",
        "voornaam": '{{first(split(3.naam; " "))}}',
        "start": "{{3.start}}",
        "eind": "{{3.eind}}",
        "duur": '{{replace(3.uren; "."; ",")}}',
        "gstart": '{{replace(3.start; ":"; "")}}',
        "geind": '{{replace(3.eind; ":"; "")}}',
        "bedrag": '{{formatNumber(2.amount; 2; ","; ".")}}',
        "nverkleed": '{{(length(3.vps) - length(replace(3.vps; "ja"; ""))) / 2}}',
    }
    for i, veld in enumerate(["3.naam", "3.s2", "3.s3", "3.s4"], 1):
        ja = f'get(split(3.vps; ","); {i}) = "ja"'
        v[f"speler{i}"] = "{{" + veld + "}}"
        for k, n in (("bg", 0), ("fg", 1), ("lbl", 2)):
            v[f"{k}{i}"] = "{{if(" + ja + '; "' + AAN[n] + '"; "' + UIT[n] + '")}}'
    return v


def voorbeeld_velden(img):
    spelers = [("Sanne de Vries", True), ("Mark Jansen", True), ("Priya Bakker", False), ("Tom Visser", True)]
    v = {"img": img, "voornaam": "Sanne", "start": "18:00", "eind": "19:30", "duur": "1,5",
         "gstart": "1800", "geind": "1930", "bedrag": "35,16", "nverkleed": "3"}
    for i, (naam, vk) in enumerate(spelers, 1):
        bron = AAN if vk else UIT
        v[f"speler{i}"], v[f"bg{i}"], v[f"fg{i}"], v[f"lbl{i}"] = naam, *bron
    return v


def vul(velden):
    s = SJABLOON
    for k, w in velden.items():
        s = s.replace(f"[[{k}]]", w)
    assert "[[" not in s, s[s.index("[["):][:40]
    return s


if __name__ == "__main__":
    (HIER / "bevestigingsmail-make.html").write_text(vul(make_velden()))
    lokaal = "../../../sites/padelpadel-fiesta/assets"
    (HIER / "voorbeeld.html").write_text(vul(voorbeeld_velden(lokaal)))
    print("ok")
