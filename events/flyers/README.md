# Flyer Padel Kids Kamp (voor scholen)

## Gekozen versie: Higgsfield-illustratie, voor- en achterkant (definitief 20 september 2026)

Lars koos de Higgsfield-voorkant (job `c255ca17-4b23-430c-8bc9-24bcacf34c4f`) en de Higgsfield-achterkant (job `135677f6-a10c-411f-96e2-9d61ad94db17`). Beide zijn daarna lokaal afgewerkt op basis van de afbeeldingen die Lars in de chat plakte (1328 × 2000 px):

- **Kortingstekst herschreven.** "10% korting vanaf het 2e kind" was dubbelzinnig. Voorkant nu: "€195 all-in · 2 of meer kinderen: 10% korting" (zelfde navy pill, Fredoka Bold in dezelfde geelgroene kleur). Achterkant nu: "Broertje of zusje mee? Dan krijg je 10% korting" (Barlow Semi Condensed, zelfde kleur en grootte als de andere regels).
- **Achterkant korter.** De drie "Dag 1/2/3"-kaartjes zijn verwijderd (het dagprogramma staat al in het navy blok); het blok "Goed om te weten" met de QR is omhoog geschoven en het vrijgekomen vlak is gevuld met de originele papiertextuur.
- **Echte QR-code** in het witte vlak op beide zijden, machinaal gecontroleerd (decodeert op voor- en achterkant).
- Opgeschaald naar 2× en met de papierkleur aangevuld tot A5-verhouding.

| Bestand | Wat |
|---|---|
| `kidskamp-flyer-illustratie-a5.pdf` | drukbestand, 2 pagina's A5 |
| `kidskamp-flyer-voorkant-illustratie.png`, `kidskamp-flyer-achterkant-illustratie.png` | beide zijden, 2819 × 4000 px, ook bruikbaar als post of in de ouderapp |
| `kidskamp-flyer-illustratie-a5.html` | bron van de PDF (beide zijden als ingebedde afbeelding) |
| `kidskamp-qr.png` | de QR-code los |

Let op: Lars noemde een eigen QR-code, maar er kwam geen afbeelding mee. De gebruikte code wijst naar `allcourtacademy.com/pages/kids-camp.html` met UTM-parameters (`utm_source=flyer`, `utm_medium=print`, `utm_campaign=kidskamp-herfst2026`). Een andere QR: vervang `kidskamp-qr.png` en draai de afwerking opnieuw, of plak de code in Canva over het witte vlak.

## Eerste versie (HTML, navy) blijft beschikbaar

Gemaakt op 20 september 2026. A5, dubbelzijdig, drukklaar.

| Bestand | Wat |
|---|---|
| `kidskamp-flyer-a5.pdf` | drukbestand, 2 pagina's A5 (148 × 210 mm), voorkant navy, achterkant crème |
| `kidskamp-flyer-voorkant.png`, `kidskamp-flyer-achterkant.png` | preview op 3× resolutie, ook bruikbaar als Instagram-post of WhatsApp-afbeelding |
| `kidskamp-flyer-a5.html` | bron; tekst aanpassen en opnieuw naar PDF printen met Chrome (Ctrl+P, A5, marges geen, achtergrondkleuren aan) |
| `kidskamp-qr.png` | de QR-code los, 1220 × 1220 px, voor gebruik in Canva of op andere posters |

## QR-code

De QR-code is echt gegenereerd (niet door een beeldmodel getekend, die zijn nooit scanbaar) en wijst naar:

`https://allcourtacademy.com/pages/kids-camp.html?utm_source=flyer&utm_medium=print&utm_campaign=kidskamp-herfst2026`

Door de UTM-parameters zie je in Google Analytics en in het inschrijfformulier ("Hoe heb je ons gevonden?") hoeveel inschrijvingen via de flyer komen. Foutcorrectie staat op niveau H, dus de code blijft scanbaar bij een logo in het midden of lichte drukvervuiling. Beide zijden zijn machinaal gecontroleerd: de QR decodeert op de gerenderde voorkant en achterkant.

Heeft Lars een eigen QR-code (bijvoorbeeld uit Canva of met een andere link)? Vervang dan `kidskamp-qr.png` en de base64-afbeelding in de HTML, of plak de nieuwe code in Canva over de bestaande.

## Opbouw en waarom

Voorkant (voor het kind én de ouder in één oogopslag): kop, één zin die het gevoel geeft ("Sla je eerste smash, maak nieuwe vrienden…"), de drie feiten die een ouder als eerste wil weten (wanneer, welke leeftijd, wat is geregeld), prijs met familiekorting, schaarste ("de zomereditie zat vol"), QR met "Scan & schrijf je in".

Achterkant (voor de ouder die twijfelt): wat het kind precies doet, het dagprogramma per uur, de opbouw van drie dagen, praktische zaken (rackets aanwezig, wat mee te nemen, vriendjes samen in een groep), nogmaals de QR en het mailadres.

Bewust weggelaten: tekst die niet op de site staat (geen losse dagen, geen vriendjeskorting), foto's van kinderen (die heb je op de site, maar voor een flyer op scholen is toestemming van ouders nodig; een illustratie is veiliger), en meer dan één call-to-action.

## Drukken en verspreiden

- Drukken: A5, dubbelzijdig, 170 of 250 grams mat. Bij 300 stuks kost dat bij een online drukker rond de €30 tot €45. Voor kleine oplages: printen op 160 grams bij de Poort Padel-balie.
- Bleed: het bestand heeft geen afloop van 3 mm; vraag de drukker om "schaalbaar zonder afloop" of laat de PDF opnieuw maken met afloop als de drukker dat eist.
- Verspreiden: de 77 scholen in `outreach/leads.csv` (bestuur staat in de notitie). Praktisch: 20 flyers per school voor het prikbord en de leerkrachten van groep 3 t/m 8, plus een korte mail met de PDF voor de nieuwsbrief. Pdf-versie mailen werkt vaak beter dan papier, omdat scholen de flyer dan digitaal in de ouderapp (Parro, Social Schools) kunnen zetten.

## Alternatieve ontwerpen (Higgsfield, met lege QR-plek)

Twee AI-varianten met dezelfde tekst en een leeg wit vlak waar de QR-code in Canva overheen kan: navy met de echte high-five-foto (job `90571c9a-8854-40f1-8164-e6b8359736c3`) en crème met illustratie (job `c255ca17-4b23-430c-8bc9-24bcacf34c4f`). Controleer bij die versies de spelling; de HTML/PDF-versie hierboven is tekstueel exact.
