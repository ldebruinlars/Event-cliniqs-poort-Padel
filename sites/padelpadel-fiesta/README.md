# padelpadel-fiesta: Halloween Padel Special (za 31 oktober 2026)

Netlify-project: https://app.netlify.com/projects/halloween-poort-padel (voorheen padelpadel-fiesta, site-id `d1b410c7-af4c-4e1e-8111-5469aabc82ee`).
Live adres: https://halloween-poort-padel.netlify.app. Statische site, geen build nodig (`netlify.toml`: publish = ".").

De vorige site (Papapadel's Verjaardags-Mexicano, 10 oktober) staat bewaard in `sites/archief/papapadel-verjaardags-mexicano/`.

## Wat de site doet

Boekingsmodule voor de Halloween-actie: wie echt verkleed of geschminkt komt, krijgt 50% korting op zijn of haar deel van de baan.

| Regel | Waarde in de code (`index.html`, onderaan in het script) |
|---|---|
| Baanprijs weekend, dubbelbaan | `PRIJS_PER_UUR = 3750` (centen) |
| Spelers per baan | `SPELERS = 4` |
| Openingstijden za | `OPEN = 08:00`, `DICHT = 23:00`, begintijden per 30 minuten |
| Duur | 1, 1,5 (standaard) of 2 uur |

Rekenvoorbeeld 1,5 uur: baan €56,25, gedeeld door 4 = €14,06 p.p. Verkleed betaal je €7,03. Alle vier verkleed: €28,12 voor de baan in plaats van €56,25.

De bezoeker kiest de duur, tikt op de baan aan welke spelers verkleed komen, kiest een begintijd en vult naam, e-mail en telefoon in. Verplicht vinkje: korting alleen bij echt verkleed of geschminkt; wie dat aan de balie niet is, betaalt het verschil bij.

## Waar de aanvragen binnenkomen

**Netlify Forms**, formulier `halloween-boeking` (staat aan voor dit project). In Netlify: Forms → halloween-boeking. Per aanvraag: naam, e-mail, telefoon, opmerking, datum, duur, starttijd, eindtijd, aantal verkleed, per speler verkleed of niet, baanprijs, korting, totaal te betalen, bedrag per speler. Stel in Netlify een e-mailmelding in (Forms → Form notifications) zodat je elke aanvraag direct in je mail krijgt.

Werkwijze nu: aanvraag binnen → baan bij Poort Padel vastzetten → bevestiging met betaallink sturen (Tikkie of Mollie).

**Later automatisch betalen:** zet in `index.html` het adres van een Make-webhook in `BETAAL_WEBHOOK`. De site stuurt dan alle velden (incl. `totaal_te_betalen`) naar Make; als Make een betaallink (https://…) teruggeeft, gaat de bezoeker direct door naar betalen, net als bij de Mexicano. Laat Mollie terugsturen naar `/bedankt.html`.

Let op: de site weet niet welke banen bij Poort Padel nog vrij zijn (dat staat in Playtomic). Het is daarom een aanvraag, geen directe reservering.

## Publiceren

Vanuit de Claude-cloudomgeving lukte publiceren niet: na het toestaan van `api.netlify.com` en `netlify-mcp.netlify.app` werd de upload naar `netlify-mcp.netlify.app` steeds na ongeveer 11 seconden afgebroken (fetch failed). Twee manieren:

1. **Zelf slepen (1 minuut):** Netlify → padelpadel-fiesta → Deploys → sleep de map `sites/padelpadel-fiesta` (of de uitgepakte zip) in het vak onderaan.
2. **Laten doen:** voeg in de instellingen van de cloudomgeving (Network access) `api.netlify.com` en `netlify-mcp.netlify.app` toe aan de toegestane domeinen; dan kan Claude publiceren met de Netlify-koppeling.

## Bestanden

| Bestand | Wat |
|---|---|
| `index.html` | de site, alle tekst en de rekenregels staan hierin |
| `bedankt.html` | pagina na betalen (voor later, als Mollie via Make terugstuurt) |
| `assets/hero.jpg` | achtergrond, versie 12 van de Halloween-poster |
| `assets/og.jpg` | deelplaatje voor WhatsApp en social |
| `assets/fonts/` | Creepster en Poppins (OFL), zelf gehost |
