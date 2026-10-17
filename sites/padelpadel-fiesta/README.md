# halloween-poort-padel: Halloween Padel Special (za 31 oktober 2026, 16:00 tot 23:00)

Netlify-project: https://app.netlify.com/projects/halloween-poort-padel (voorheen padelpadel-fiesta, site-id `d1b410c7-af4c-4e1e-8111-5469aabc82ee`).
Live adres: https://halloween-poort-padel.netlify.app. Statische site, geen build nodig (`netlify.toml`: publish = ".").

De vorige site (Papapadel's Verjaardags-Mexicano, 10 oktober) staat bewaard in `sites/archief/papapadel-verjaardags-mexicano/`.

## Wat de site doet

Boekingsmodule voor de Halloween-actie: wie echt verkleed of geschminkt komt, krijgt 50% korting op zijn of haar deel van de baan.

| Regel | Waarde in de code (`index.html`, onderaan in het script) |
|---|---|
| Baanprijs weekend, dubbelbaan | `PRIJS_PER_UUR = 3750` (centen) |
| Spelers per baan | `SPELERS = 4` |
| Tijden za 31 oktober | `OPEN = 16:00`, `DICHT = 23:00`, begintijden per 30 minuten |
| Duur | 1, 1,5 (standaard) of 2 uur |

Rekenvoorbeeld 1,5 uur: baan €56,25, gedeeld door 4 = €14,06 p.p. Verkleed betaal je €7,03. Alle vier verkleed: €28,13 voor de baan in plaats van €56,25.

Totaal = baanprijs × (8 − aantal verkleed) / 8, afgerond op centen. Alle bedragen:

| Verkleed | 1 uur | 1,5 uur | 2 uur |
|---|---|---|---|
| 0 | €37,50 | €56,25 | €75,00 |
| 1 | €32,81 | €49,22 | €65,63 |
| 2 | €28,13 | €42,19 | €56,25 |
| 3 | €23,44 | €35,16 | €46,88 |
| 4 | €18,75 | €28,13 | €37,50 |

De bezoeker kiest de duur, tikt op de baan aan welke spelers verkleed komen, kiest een begintijd en vult naam, e-mail en telefoon in. Verplicht vinkje: korting alleen bij echt verkleed of geschminkt; wie dat aan de balie niet is, betaalt het verschil bij.

## Betalen: direct via Mollie (Make-scenario "halloween betaling")

Klanten betalen vooraf, direct bij het boeken, met iDEAL. Een vaste betaallink werkt niet, omdat het bedrag per boeking verschilt (15 mogelijke bedragen). Daarom maakt Make per boeking een Mollie-betaling met precies het juiste bedrag, net als bij de Mexicano (scenario "papapadel 2").

Flow: site → Netlify Forms (overzicht) → Make-webhook → Mollie createPayment → Make stuurt de iDEAL-link terug → klant betaalt → Mollie stuurt terug naar `/bedankt.html` → Lars boekt de baan bij Poort Padel → tweede mail "baan geboekt".

### Status (17 oktober 2026)

Gebouwd en aangezet: Make-scenario **"halloween betaling"** (id 8011622) met webhook "Halloween boeking" (`https://hook.eu1.make.com/uo8p28ou79eewpoqfpjk3vgy5mmfhi3t`, staat in `index.html` bij `BETAAL_WEBHOOK`). Webhook → filter "geldige boeking" (verkleed 0 t/m 4, uren 1 t/m 2) → Mollie Create a Payment (connectie All Court Academy B.V., bedrag door Make berekend, metadata met alle spelers) → antwoord met de iDEAL-link. Getest met 1,5 uur en 3 verkleed: iDEAL-pagina toont €35,16 aan All Court Academy B.V. Die testbetaling (omschrijving begint met TEST) is niet betaald en vervalt vanzelf.

Betaalde boekingen → Google Sheet: Make-scenario **"halloween betaald naar sheet en Moneybird"** (id 8011858, webhook "Halloween Mollie betaald"). Mollie roept het aan bij elke statuswijziging; het haalt de betaling op en zet alleen betalingen die in het afgelopen halfuur op "paid" zijn gesprongen als één regel in [Halloween Padel 31 oktober · boekingen en check-in](https://docs.google.com/spreadsheets/d/1JDcYpc3hiMmV3yYleYBBustmHQm1-N7fkt4-fqkBr_w/edit) (tab Boekingen). Een latere terugbetaling geeft zo geen dubbele regel. Daarna gaat elke echte (live) betaling naar **Moneybird**, net als bij de Mexicano: contact opzoeken op e-mail (of aanmaken), factuur maken (workflow "Kidscamp", 9% btw, grootboek Omzet, referentie "Mollie tr_…", regel "Baanhuur Halloween Padel Special · zaterdag 31 oktober · start tot eind · naam"), factuur op handmatig verstuurd zetten en de Mollie-betaling erop boeken, zodat hij meteen als betaald staat.

**Terugbetalingen.** Een terugbetaling in Mollie roept hetzelfde scenario aan (status blijft "paid", `amountRefunded` stijgt). De route voor nieuwe betalingen slaat die over, want die eist `amountRefunded` = 0 en betaald in het afgelopen halfuur. De terugbetalingsroute zoekt de boeking op in de sheet (kolom Mollie-id), vergelijkt het teruggestorte bedrag met kolom O "Terugbetaald (€)" en maakt alleen voor het verschil een **creditfactuur** in Moneybird: negatief bedrag, regel "Terugbetaling baanhuur Halloween Padel Special …", referentie "Mollie tr_… terugbetaling", zelfde contact. Die creditfactuur wordt op verstuurd gezet en met de terugbetaling verrekend. Daarna zet Make het nieuwe totaal in kolom O. Een tweede gedeeltelijke terugbetaling op dezelfde boeking geeft zo alleen een credit voor het nieuwe deel. Volledig terugbetaalde boekingen verdwijnen van de Printlijst; de tellers bovenaan tellen alleen boekingen die niet volledig zijn terugbetaald en "Netto betaald" is betaald min terugbetaald. Tab Printlijst sorteert alles op starttijd en is bedoeld om te printen voor de bar (Bestand → Afdrukken → liggend, aanpassen aan breedte). Lars vult het baannummer in tab Boekingen, kolom Baan (geel). Getest: een geannuleerde testbetaling komt niet in de sheet. Een echte betaalde boeking is nog niet getest.

De bedankpagina zegt "Bedankt!" en niet "Betaald!", omdat Mollie ook na een afgebroken betaling naar die pagina terugstuurt.

### Zo zet je het op in Make (handmatige beschrijving van hetzelfde scenario)

1. Make → Scenarios → "papapadel 2" → ⋯ → **Clone**. Noem de kopie `halloween betaling`.
2. **Webhook (module 1):** klik erop → **Add** → nieuwe webhook `Halloween boeking`. Kopieer het adres (Copy address).
3. **Google Sheets "getCell" (module 4) en de router:** haal deze weg, of laat de vol-check staan als je een cel bijhoudt met vrije banen. Zonder vol-check: verbind de webhook direct met Mollie.
4. **Mollie "Create a Payment" (module 2):**
   - Amount: `{{formatNumber(round(37.5 * 1.uren * (8 - 1.verkleed) / 8 * 100) / 100; 2; "."; "")}}`. Make rekent het bedrag zelf uit op basis van uren en verkleed, dus niemand kan een lager bedrag doorsturen.
   - Description: `{{1.omschrijving}} - {{1.naam}}`
   - Redirect URL: `https://halloween-poort-padel.netlify.app/bedankt.html`
   - Metadata (alles wat de check-in nodig heeft): `{"naam":"{{1.naam}}","s2":"{{1.speler_2}}","s3":"{{1.speler_3}}","s4":"{{1.speler_4}}","vps":"{{1.verkleed_per_speler}}","telefoon":"{{1.telefoon}}","email":"{{1.email}}","start":"{{1.starttijd}}","eind":"{{1.eindtijd}}","uren":"{{1.uren}}"}`
   - Webhook URL: leeg laten, of een kopie van "betaling gelukt" voor Halloween (zie stap 7).
5. **Filter** op de lijn naar Mollie (moersleutel → Set up a filter), naam "geldige boeking": `1.verkleed` ≥ 0 én ≤ 4, en `1.uren` ≥ 1 én ≤ 2.
6. **Webhook response (module 3):** body `{{2.checkoutLink}}`, status 200, header `Access-Control-Allow-Origin: *` (staat er al).
7. Zet het scenario **aan** en plak het webhook-adres in `index.html` bij `const BETAAL_WEBHOOK = '...'`. Daarna opnieuw publiceren.
8. **Check-inlijst automatisch vullen.** Zet `events/2026-halloween-padel/checkin/halloween-checkin-lijst.xlsx` in Google Drive en open hem als Google Sheet. Clone "betaling gelukt" naar `halloween betaling gelukt`: Mollie "Get a payment" → filter status = paid → JSON "Parse JSON" op de metadata → **4× Google Sheets "Add a row"** in tabblad Check-in, één per speler:
   - Starttijd `start`, Eindtijd `eind`, Boeker `naam`, Telefoon boeker `telefoon`, Duur `uren`, Mollie-betaling `{{id}}`
   - Speler: rij 1 `naam`, rij 2 `s2`, rij 3 `s3`, rij 4 `s4`
   - Korting betaald: `{{get(split(vps; ","); 1)}}` voor rij 1, `2` voor rij 2, enzovoort
   - Baan, Aanwezig, Echt verkleed? en Bijbetaald via laat je leeg (die vul jij en de check-in in).
   Zet het webhook-adres van dit scenario in stap 4 bij Webhook URL.

Test: boek zelf 1 uur met 4 verkleed (€18,75), betaal, en storneer via Mollie → Betalingen → Terugbetalen.

### Check-in op de dag

Wie controleert: één persoon bij een Halloween check-in tafel bij de balie van Poort Padel, van 15:50 tot ongeveer 21:45 (laatste begintijd 21:30). Lars zelf, een trainer van de Academy, of iemand van Poort Padel. Twee diensten van drie uur is prettig.

Die persoon heeft de check-inlijst open op telefoon of tablet (Google Sheet) en een Tikkie-QR of pinautomaat voor bijbetalen. Per speler: Aanwezig = ja, Echt verkleed? = ja/nee. Kolom Groep compleet toont "compleet" als alle vier er zijn; pas dan krijgt de groep het baannummer. Wordt de cel oranje, dan betaalt die speler het verschil bij (1 uur €4,69, 1,5 uur €7,03, 2 uur €9,38). Uitleg staat in het tabblad "Uitleg check-in".

### Na een betaling

1. Boek de baan in Playtomic/bij Poort Padel en zet het baannummer in kolom Baan van de check-inlijst.
2. Stuur de tweede bevestiging (mail of WhatsApp), zonder baannummer: de spelers horen hun baan pas bij de check-in. Tekst: zie `events/2026-halloween-padel/checkin/bevestiging-whatsapp.txt`.
3. Tijd vol? Bel of mail voor een andere tijd. Past niets: terugbetalen via Mollie.

Netlify Forms (formulier `halloween-boeking`) bewaart ook elke boeking, ook als iemand de betaling afbreekt. Vergelijk met Mollie: alleen wat in Mollie op "betaald" staat, boek je.

Zolang `BETAAL_WEBHOOK` leeg is, slaat de site de boeking alleen op en ziet de klant "we sturen een betaallink".

## Publiceren

Vanuit de Claude-cloudomgeving lukte publiceren niet: na het toestaan van `api.netlify.com` en `netlify-mcp.netlify.app` werd de upload naar `netlify-mcp.netlify.app` steeds na ongeveer 11 seconden afgebroken (fetch failed). Twee manieren:

1. **Zelf slepen (1 minuut):** Netlify → padelpadel-fiesta → Deploys → sleep de map `sites/padelpadel-fiesta` (of de uitgepakte zip) in het vak onderaan.
2. **Laten doen:** voeg in de instellingen van de cloudomgeving (Network access) `api.netlify.com` en `netlify-mcp.netlify.app` toe aan de toegestane domeinen; dan kan Claude publiceren met de Netlify-koppeling.

## Bestanden

| Bestand | Wat |
|---|---|
| `index.html` | de site, alle tekst en de rekenregels staan hierin |
| `bedankt.html` | pagina na betalen: betaling binnen, tweede bevestiging volgt als de baan geboekt is |
| `assets/hero.jpg` | achtergrond, versie 12 van de Halloween-poster |
| `assets/og.jpg` | deelplaatje voor WhatsApp en social |
| `assets/fonts/` | Creepster en Poppins (OFL), zelf gehost |
