# Outreach – bedrijven en scholen in Almere mailen

## Stap 1: leads verzamelen (lijst met bedrijven en scholen)

Er is geen kant-en-klare lijst van "alle bedrijven in Almere" in deze repo. Je bouwt die zelf met een open-source scraper of via publieke bronnen. Twee GitHub-tools die dit goed doen:

| Tool | Wat | Link |
|---|---|---|
| gosom/google-maps-scraper | Open-source CLI + web UI. Zoekt op Google Maps ("bouwbedrijf Almere") en levert naam, adres, telefoon, website en waar mogelijk e-mail als CSV. Werkt goed samen met Claude Code: beschrijf de leads die je wilt en laat de agent de zoekopdrachten draaien. | https://github.com/gosom/google-maps-scraper |
| ozhehkovski/geoleadscraper | Gratis Chrome-extensie zonder account of API-key. Exporteert Google Maps-resultaten naar CSV/XLSX. Handig als je geen terminal wilt gebruiken. | https://github.com/ozhehkovski/geoleadscraper |

Aanbevolen zoekopdrachten (per keer max. ~120 resultaten in Google Maps, dus splits per wijk en branche):

Bedrijven: `kantoor Almere Poort`, `bedrijf Almere Stad`, `accountant Almere`, `advocaat Almere`, `makelaar Almere`, `bouwbedrijf Almere`, `installatiebedrijf Almere`, `IT bedrijf Almere`, `marketingbureau Almere`, `autobedrijf Almere`, `zorginstelling Almere`, `gemeente Almere afdeling`, `bedrijventerrein De Vaart Almere`, `bedrijventerrein Gooisekant Almere`, `Stichtsekant Almere`, `Sallandsekant Almere`.

Scholen: `basisschool Almere`, `middelbare school Almere`, `mbo Almere`, `Windesheim Almere`, `Aeres Almere`, `kinderopvang Almere`, `BSO Almere`. Voor scholen is scholenopdekaart.nl (publieke database van alle NL-scholen met contactgegevens) de meest complete bron: filter op gemeente Almere.

Zet het resultaat in `outreach/leads.csv` met de kolommen `segment,bedrijf,voornaam,email,plaats,sector,opt_out,notitie`. Gebruik bij voorkeur een algemeen adres (info@, directie@, hr@) of de naam van de HR-/officemanager als je die kent.

## Stap 2: templates checken

- `email/template-bedrijven.md` – bedrijfsuitje, teambuilding, klantevent.
- `email/template-scholen.md` – gymles op locatie, schoolclinic, sportdag, naschools programma.
- `email/followup.md` – opvolgmail na 7 dagen zonder reactie.

Placeholders: `{{aanhef}}` (automatisch "Hey Kim" of "Hey team van Bedrijf"), `{{bedrijf}}`, `{{voornaam}}`, `{{plaats}}`, `{{sector}}`. De prijzen in de templates komen uit `pricing/aca-event-prijslijst.md`. Pas ze aan als je de marge of inputs in de calculator wijzigt.

## Stap 3: versturen

```bash
# 1. dry-run: laat zien wat er zou gaan, verstuurt niets
python3 outreach/send_campaign.py

# 2. Gmail app-wachtwoord instellen (Google-account > Beveiliging > 2-staps > App-wachtwoorden)
export ACA_SMTP_USER="info@allcourtacademy.com"
export ACA_SMTP_PASS="xxxx xxxx xxxx xxxx"

# 3. echt versturen, in batches
python3 outreach/send_campaign.py --send --segment scholen --limit 40
python3 outreach/send_campaign.py --send --segment bedrijven --limit 40
```

Het script slaat automatisch over: opt-outs, ongeldige adressen, voorbeeldregels en adressen die al in `outreach/sent_log.csv` staan. Standaard 20 seconden pauze tussen mails en max. 50 per run. Hou het bij een Gmail-account onder ongeveer 100 externe mails per dag om niet als spam gemarkeerd te worden. Bij grotere volumes: Google Workspace-account of een tool als Brevo/Mailchimp met eigen domeinverificatie (SPF/DKIM).

Alternatief zonder script: Claude kan met de Gmail-connector per lead een concept in je Gmail-map "Concepten" klaarzetten, zodat je elke mail zelf nog even nakijkt en verstuurt.

## Spelregels (Telecommunicatiewet en AVG)

- Ongevraagde commerciële e-mail aan **bedrijven en instellingen** (rechtspersonen, algemene adressen zoals info@) is in Nederland toegestaan zolang het aanbod relevant is voor de ontvanger en er een duidelijke afmeldmogelijkheid in staat. De templates bevatten daarom een afmeldregel.
- Aan **persoonlijke adressen van natuurlijke personen** (voornaam@gmail.com, eenmanszaken) mag je niet zomaar mailen zonder toestemming. Filter die eruit.
- Verwerk een afmelding direct: zet `opt_out` op `1` in `leads.csv`.
- Bewaar niet meer gegevens dan nodig (naam, functie, zakelijk e-mailadres). Noem in je privacyverklaring dat je zakelijke contactgegevens gebruikt voor acquisitie.

## Vervolg

Reacties komen binnen op je eigen mailbox. Antwoord met de `allcourtacademy-emails` skill (concept in jouw stijl) en maak de offerte met `pricing/prijscalculator.xlsx` (tabblad Offerte).
