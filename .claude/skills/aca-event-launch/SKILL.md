---
name: aca-event-launch
description: Stappenplan om een betaald event of clinic van All Court Academy bij Poort Padel online te zetten, van poster tot boekingssite, Mollie-betaling via Make, Google Sheet voor de bar, Moneybird-factuur en creditfactuur, bevestigingsmail en social posts in Metricool. Gebruik bij elk nieuw event, elke actie met online boeken en betalen, of als Lars vraagt "zet dit event online", "maak een boekingssite", "koppel Mollie/Moneybird", "maak een poster en post hem". De Halloween Padel Special (okt 2026) is het werkende voorbeeld.
---

# Event online zetten (ACA × Poort Padel)

Werkend voorbeeld van alle onderdelen: Halloween Padel Special. Kopieer de aanpak, niet de ID's. Lees eerst `CLAUDE.md` in de root.

## Volgorde

1. **Afspraken vastleggen**: datum, tijden, prijs en kortingsregel, wie controleert op de dag, of betalen vooraf gaat (standaard ja: betaald = bevestigd). Schrijf de rekenregel als formule op, die komt op drie plekken terug (site-JS, Make-bedrag, uitleg).
2. **Poster**: HTML met formaten via `#feed` (1080×1350), `#story` (1080×1920), `#print` (3:4 + pdf 30×40), renderen op 2x met headless Chromium. Voorbeeld: `events/2026-halloween-padel/definitief/` (`poster.html`, `render.sh`). Online versies: "link in bio". Print: webadres + QR (`pip install qrcode`, controleren met OpenCV `QRCodeDetector`). Artwork: Higgsfield `nano_banana_pro`.
3. **Boekingssite**: statische map met `index.html`, `bedankt.html`, zelf gehoste fonts, `netlify.toml`. Voorbeeld: `sites/padelpadel-fiesta/`. Volgorde in de module: keuzes die de prijs bepalen eerst, dan tijd, dan namen, pas onder het formulier de betaalknop. Geen "betalen"-knoppen eerder in de pagina; wel een "volgende stap"-knop. Alle velden verplicht met "Vul dit in.". Haal `" \ < >` uit namen (Make bouwt er JSON van). Testen met Playwright op 390 px en 1280 px, met nep-webhook (route intercept).
4. **Publiceren**: zip van de sitemap (zonder README en `.gitignore`); Lars sleept hem in Netlify → Deploys. Netlify Forms vangt elke inzending ook op.
5. **Betalen (Make scenario 1)**: webhook → filter op geldige invoer → Mollie Create Payment (bedrag door Make berekend met dezelfde formule, nooit het bedrag uit het formulier vertrouwen; metadata als JSON met alle namen) → Webhook response met `checkoutLink` en header `Access-Control-Allow-Origin: *`. redirectUrl naar `bedankt.html`, webhookUrl naar scenario 2.
6. **Na betaling (Make scenario 2)**: webhook → Mollie Get Payment → router.
   - Nieuwe betaling (status paid, betaald in laatste 30 min, `amountRefunded` = 0): Google Sheets Add a row met **insertDataOption OVERWRITE** (INSERT_ROWS neemt de opmaak van de kopregel over), data store-record met 0, Gmail bevestigingsmail (Resume bij fout), Moneybird alleen bij `mode = live`: contact zoeken of maken, factuur, op verstuurd (`delivery_method: Manual`), betaling registreren.
   - Terugbetaling (`amountRefunded` > 0): router met twee takken. Moneybird: data store ophalen, alleen het verschil crediteren (negatieve factuur + betaling), nieuw totaal opslaan. Sheet: rij zoeken op Mollie-id en kolom Terugbetaald vullen (Ignore bij fout).
   - Moneybird-workflow kiezen zonder automatische betaalbevestiging, anders krijgt de klant een extra mail.
7. **Sheet voor de bar**: tab met ruwe boekingen (Make schrijft) en een printtab met `SORT(FILTER(...))` over **hele kolommen** (`Boekingen!A:L` met `ROW()>1`), nooit `A2:L` (schuift mee bij invoegen). Locale nl_NL: `;` in formules, bedragen als "35,16".
8. **Bevestigingsmail**: tabel-layout met inline stijlen, kopplaat als gehoste afbeelding (fonts werken niet in mail), sjabloon met `[[velden]]` dat zowel een Make-versie als een voorbeeld met nepdata maakt. Voorbeeld: `events/2026-halloween-padel/mail/build_mail.py`. Laat Lars het voorbeeld als artifact zien.
9. **Social**: volg `events/social-posts.md` (kort en hype, max 5 hashtags, @poortpadel collab en tag, Facebook met link). Inplannen in Metricool pas na akkoord; afbeelding via publieke GitHub raw-URL.
10. **Poort Padel informeren**: WhatsApp via skill `allcourtacademy-emails`, met poster, versie met QR en wat er voor de bar klaarligt.

## Valkuilen die we al tegenkwamen

- `scenarios_update` vervangt het hele scenario: genereer de blauwdruk met een script (voorbeeld `events/2026-halloween-padel/make/build_blueprint.py`) en stuur die in z'n geheel.
- Data store "Get a record" met een sleutel die niet bestaat is niet getest; daarom maakt scenario 2 het record al aan bij de betaling, zodat het er bij een terugbetaling altijd is.
- Make kan een webhook niet laten reageren als een filter faalt: de site moet een niet-`http`-antwoord als fout tonen.
- netlify.app en hook.eu1.make.com zijn vanuit de cloudcontainer geblokkeerd: testen via de Make- en Netlify-koppelingen of laat Lars testen. Echte test = echte betaling van het kleinste bedrag, daarna terugbetalen in Mollie.
- Teksten zonder gedachtestreepjes; check het hele project met grep na een regelwijziging (oude zinnen blijven anders staan op site, bedankpagina, mail, sheet en README).
