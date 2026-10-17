# CLAUDE.md

Werkgeheugen voor Claude in deze repo. Kort houden; details staan in de README's waarnaar verwezen wordt.

## Wie en wat

- Lars de Bruin, eigenaar All Court Academy (ACA), padelschool bij Poort Padel, Neonweg 62, Almere Poort. Schrijft snel getypt Nederlands; interpreteer de bedoeling.
- Deze repo: events, clinics, posters, sites en social voor ACA × Poort Padel. Overzicht van alle mappen: `README.md`.
- Werkbranch: `claude/poort-padel-all-court-h6n4c9`. Repo is publiek, dus geen geheimen of webhook-adressen van privézaken in nieuwe bestanden.

## Stijl van Lars (altijd)

- Teksten namens Lars: "Hoi/Hey [naam]", geen ondertekening, eindigen met "Tot snel op de baan!", geen gedachtestreepjes (komma gebruiken), concept tussen `---` en afsluiten met "Klaar voor versturen?". De skill `allcourtacademy-emails` heeft alle regels.
- Social: kort en hype, geen uitleg in de post (die staat op de site). Eerste zin pakt (bijv. "Over 2 weken ..."), dan sfeer, één voordeel, urgentie, boekoproep. Maximaal 5 hashtags. Instagram: "link in bio", @poortpadel als collaborator en getagd. Facebook: volledige link in de tekst. Plan in Metricool pas na akkoord van Lars ("plan maar in" of een expliciete tijd). Afspraken en planning: `events/social-posts.md`.
- Laat Lars eerst een voorbeeld zien (render/preview) voordat iets live gaat.

## Halloween Padel Special (za 31 oktober 2026, 16:00 tot 23:00)

Stand 17 oktober 2026: alles live en getest met een echte betaling. Details: `sites/padelpadel-fiesta/README.md`, poster en mail: `events/2026-halloween-padel/`.

- Prijs: €37,50 per uur dubbelbaan, gedeeld door 4; wie echt verkleed komt betaalt de helft van zijn deel. Totaal = round(37,5 × uren × (8 − verkleed) / 8, centen). Niet verkleed op de dag: geen bijbetaling. Betaald = bevestigd.
- Site: https://halloween-poort-padel.netlify.app (Netlify site id `d1b410c7-af4c-4e1e-8111-5469aabc82ee`, map `sites/padelpadel-fiesta/`). Volgorde op de site: wie verkleed → duur → tijd → namen → "Betaal €…". Publiceren: zip van die map, Lars sleept hem in Netlify → Deploys (upload vanuit de cloudomgeving lukt niet).
- Make (team 1563554): scenario 8011622 "halloween betaling" (webhook → Mollie-betaling, bedrag door Make berekend) en 8011858 "halloween betaald naar sheet en Moneybird" (sheet-regel, bevestigingsmail via Gmail, Moneybird-factuur; terugbetaling → creditfactuur, bijgehouden in data store 222335 "halloween terugbetaald", plus bedrag in kolom O van de sheet). Blauwdruk wijzigen: `events/2026-halloween-padel/make/build_blueprint.py` genereert de volledige JSON (scenarios_update vervangt altijd het hele scenario).
- Google Sheet `1JDcYpc3hiMmV3yYleYBBustmHQm1-N7fkt4-fqkBr_w`: tab Boekingen (Make schrijft, Lars vult kolom Baan) en tab Printlijst (voor de bar, leest hele kolommen). Locale nl_NL: formules met `;`.
- Moneybird: facturen nu op workflow "Kidscamp", die een "bedankt voor je betaling"-mail stuurt. Open punt: Lars maakt workflow "Halloween Padel" zonder betaalbevestiging, daarna `workflowId` in de blauwdruk vervangen (workflows ophalen met Make RPC `listWorkflows`).
- Social: post Instagram (collab @poortpadel) + Facebook ingepland in Metricool (brand 6979019) op za 17 okt 17:00. Story nog niet ingepland.

## Werkwijze in deze omgeving

- Renderen: Chromium op `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`, Playwright via `NODE_PATH=/opt/node22/lib/node_modules node`. Lokaal testen: `python3 -m http.server` in de sitemap.
- Netwerk: netlify.app en hook.eu1.make.com zijn vanuit de container geblokkeerd; gebruik de Netlify- en Make-koppelingen. Niet om blokkades heen werken, melden.
- Afbeeldingen voor Metricool: publieke raw-URL van GitHub (repo is publiek) werkt.
- Higgsfield: bestanden (cloudfront) niet te downloaden vanuit de container; controleren en samenvoegen in de Higgsfield-sandbox (`sandbox_exec`, `image_paths` om zelf te kijken). Character sheets: workflow `character-sheet`. Blender: `/use-blender` alleen lokaal; in de cloud 3D Jutsu of `pip install bpy==5.0.1` (Python 3.11-venv). Stand animatie: `events/2026-halloween-padel/video/characters/README.md`.
- Herbruikbaar stappenplan voor een nieuw betaald event: skill `aca-event-launch` (`.claude/skills/aca-event-launch/SKILL.md`).
