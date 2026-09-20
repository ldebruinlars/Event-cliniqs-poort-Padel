# Flyer Padel Kids Kamp (voor scholen)

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
