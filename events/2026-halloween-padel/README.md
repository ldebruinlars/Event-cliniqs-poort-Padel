# Halloween Padel Special bij Poort Padel (zaterdag 31 oktober 2026)

Actie: wie verkleed komt, speelt op zaterdag 31 oktober met 50% korting op de baan bij Poort Padel.

## Bestanden

| Bestand | Wat |
|---|---|
| `halloween-padel-ig-feed-4x5.jpg` | Instagram-post 2160 × 2700, achtergrond pompoenspeler (voorkeur) |
| `halloween-padel-ig-story-9x16.jpg` | Instagram-story 2160 × 3840, tekst boven de onderste 210 px (ruimte voor de Instagram-balk) |
| `halloween-padel-poster.jpg` / `-30x40cm.pdf` | printposter 3:4, voor het raam of de balie bij Poort Padel |
| `halloween-padel-baan-*` | dezelfde drie, met de achtergrond "pompoenbal op de baan" |
| `artwork/` | de vier Higgsfield-achtergronden zonder tekst (pompoenspeler, pompoenbal op de baan, racket-stilleven, badge) |
| `poster.html` | de opmaak; `render.sh 1` maakt de pompoenspeler-versie, `render.sh 0` de baanversie |

De achtergronden zijn gemaakt met Higgsfield (GPT Image 2, 3:4, 2k) zonder tekst; alle tekst en het Poort Padel-logo staan er als HTML overheen, zodat er geen typefouten in kunnen sluipen. Lettertypen: Creepster (kop) en Poppins (Poort Padel-huisstijl), beide OFL.

Higgsfield jobs: pompoenbal op de baan `f9847947-0ab8-4fac-9aa4-4536aa3a25bd`, pompoenspeler `3e480fd0-4381-4b72-ad5d-419fe7c085a7`, racket-stilleven `b7a13bb9-72c9-4230-9074-a9ed3b1d9464`, badge `76a95be6-cf19-4bcb-90d8-68ee5bed8ec2`.

## Tekst op de poster

Poort Padel presenteert · HALLOWEEN PADEL SPECIAL · Zaterdag 31 oktober · Kom verkleed = 50% korting op je baan · Boek je baan via Playtomic en stap in kostuum de baan op · Korting per verklede speler, alleen op zaterdag 31 oktober. Masker of schmink telt ook. · Neonweg 62 · Almere Poort · poortpadel.nl

## Aannames om te checken met Poort Padel

- De korting geldt **per verklede speler** (zijn of haar deel van de baanhuur), de hele dag. Als het "hele baan half geld zodra iemand verkleed is" moet zijn, of alleen bepaalde uren: de regel `fine` in `poster.html` aanpassen.
- Wat telt als verkleed: nu "masker of schmink telt ook", zodat niemand afhaakt omdat een heel kostuum te veel moeite is.
- Hoe de bar het controleert: korting verrekenen bij de balie bij binnenkomst, met een foto voor Instagram als bonus.

## Captions

**Feed:**
Halloween op de baan 🎃 Kom zaterdag 31 oktober verkleed naar Poort Padel en speel voor de halve prijs. Boek je baan via Playtomic, trek je kostuum aan (een masker of schmink telt ook) en de korting regelen we aan de balie. Beste outfit van de dag komt op onze Instagram 👻
📍 Neonweg 62, Almere Poort

**Story:** Za 31 oktober: verkleed = 50% korting op je baan 🎃 Boek nu via Playtomic.

## Cartoonvideo (15 seconden, 9:16)

Werkwijze zoals in `ai-animatie/WORKFLOW.md`: eerst losse referenties maken, dan het script als tijdlijn, dan de video. De tekst komt er pas na de generatie overheen (eindkaart), zodat die foutloos is.

**Referenties (Nano Banana Pro, poster-achtergrond als stijlreferentie):**

| Wat | Higgsfield job |
|---|---|
| Pompoenspeler, character sheet vier aanzichten | `4489f928-0d30-4023-8d22-0ae01ded3917` |
| Spook-tegenstander, character sheet vier aanzichten | `72f92796-2758-4e26-a99e-369567c8c94c` |
| Spookbaan, rustig (versie 1) | `71665bae-96d3-4729-87cf-625bc016d7fa` |
| Spookbaan, levendig: bliksem, skeletpubliek, wervelende mist en bladeren (versie 2) | `8b9f7295-0231-444d-8a61-6c06c824dcf7` |
| Spookbal, ook ingedrukt bij de klap | `392a88f2-bc5b-4e8e-b058-c65b36ff45c7` |

**Versie 1** (`video/script-v1-seedance.txt`, één doorlopende shot): Seedance 2.5 omni-reference, eerst draft 480p (job `2e84088e-773f-440e-9ac1-f0a8e58b00fb`, 45 credits), daarna afgerond op 1080p (job `daf0d11f-149f-4766-a1b3-6bf60e028fc1`, 60 credits). Met eindkaart vanaf 12,4 s: https://d2ol7oe51mr4n9.cloudfront.net/user_3DTi6Z7G6lm7S5aYIwHXC1iM486/d227d709-1a08-4d55-b983-b6a8ed2753fb.mp4

Feedback Lars: te duur voor een test, omgeving mag dynamischer, script beter.

**Versie 2** (`video/script-v2.txt`): zes shots met harde cuts op de beat, overal bewegende camera, haakje in de eerste seconde (bliksem, ogen gaan aan), langere rally, bullet-time smash, levendige omgeving. Getest op **Seedance 2.0 Mini 480p (7,5 credits)** in plaats van een Seedance 2.5-draft (45).

**Eindkaart**: `video/eindkaart.html` en `video/eindkaart-1080x1920.png` (transparant), in de laatste 2,6 seconden ingefade met ffmpeg in de Higgsfield-sandbox.

### Kosten om te onthouden (15 seconden, 9:16)

| Model | Credits |
|---|---|
| Seedance 2.0 Mini, 480p | 7,5 |
| Seedance 2.0 fast, 480p | 15 |
| Seedance 2.5 draft 480p | 45 (+60 om af te ronden op 1080p) |
| Seedance 2.5, 720p | 105 |
| Seedance 2.5, 1080p | 180 |

Testen altijd op Mini; pas de goedgekeurde versie op 2.5.

### Praktisch

- Higgsfield-bestanden (cloudfront) zijn vanuit deze cloudomgeving niet te downloaden. De Higgsfield-sandbox (`sandbox_exec`) kan dat wel en heeft ffmpeg: frames trekken om te controleren, eindkaart erover, en het resultaat met `media_upload` terug in Higgsfield zetten.
- De preset-suggestie "IN THE DARK" afwijzen (`declined_preset_id`), anders worden de referenties genegeerd.

## Tien extra posterversies (feed 4:5)

Op basis van de goedgekeurde pompoenspeler (versie 1) tien nieuwe achtergronden, gemaakt met **Nano Banana Pro** met de pompoenspeler (job `3e480fd0-…`) als referentie, zodat het personage hetzelfde blijft. Kosten: 2 credits per beeld, 20 in totaal.

Alles staat in `varianten/`: `build.py` maakt de tien HTML-bestanden (de tekst staat bovenin onder TEKST en is voor alle versies gelijk), `render.sh` rendert naar `varianten/final/halloween-<naam>-ig-feed-4x5.jpg` (2160 × 2700) en maakt `varianten/final/overzicht-alle-versies.jpg`. De achtergronden zonder tekst staan in `artwork/varianten/`.

| # | Richting | Opmaak | Higgsfield job |
|---|---|---|---|
| 01 | Poort Padel | groene smash, lime Creepster-kop, schuine lime aanbiedingsbalk | `ecd0f39d-2b9b-4dfc-8141-9f88a2ef757d` |
| 02 | Poort Padel | heldenpose, strakke Anton-letters links, P-patroon, ronde lime sticker | `cc092eff-36f8-4a30-aaf0-9528b9871cf4` |
| 03 | Poort Padel | door de glaswand, schuine kop, lime lint over de hele breedte | `20aee626-a5ea-4e8d-a07b-c1544abb9a7e` |
| 04 | All Court Academy | kidsclinic met verklede kinderen, Bungee, navy + oranje blokken | `8e6266df-c908-412b-91fa-45865f4490b8` |
| 05 | All Court Academy | varsity/college-poster, Graduate, oranje vaantje | `0053c9d3-5b8f-45fe-bbfd-1900efe1515a` |
| 06 | All Court Academy | trainingssessie met kegels en ballenmachine, scorebord met drie vakken | `cc255d43-e3a2-4a38-99e2-ffa7404779cb` |
| 07 | Eng | horrorfilmposter, Cinzel, tagline "Wie verkleed komt, speelt voor de helft." | `133f3813-bf8d-4dee-bca3-407f939ca5d9` |
| 08 | Eng | verlaten baan bij het kerkhof, aanbieding op een grafsteen | `0d96c3bd-ee36-41fe-b2e1-dd0030c920f2` |
| 09 | Eng | jaren-80 VHS-horror, rode neon (Monoton), scanlines | `8ac7f4c1-5c13-441f-a552-858713cf2cc0` |
| 10 | Eng | gotische houtsnede, fraktur-kop, oranje stempel | `e7d24c5c-ecf4-48ba-bb80-c275742fc429` |

Extra lettertypen (allemaal OFL, uit google/fonts): Anton, Bungee, Graduate, Oswald, Cinzel, Eater, Nosifer, Monoton, UnifrakturMaguntia, IM Fell English. De gekozen versie kan daarna ook als story (9:16) en printposter worden gemaakt.

### Versies 11-14: eng, met kapot glas

Lars vond versie 7 (horrorfilm) het vetst, maar wilde de energie van 3 of 1 erin terug, met de enge sfeer erbij. Vier nieuwe achtergronden (Nano Banana Pro, 8 credits), gemaakt met versie 7 en 3/1/8 als referentie: mist, kapotte glazen wanden, een flikkerende lamp en lime licht. De opmaak is die van 3 (schuin, lime lint) of 1 (gecentreerd, lime balk), op een donkerdere blauwzwarte basis.

| # | Beeld | Opmaak | Higgsfield job |
|---|---|---|---|
| 11 | door de glaswand, donker en mistig | als 3 | `1f8d52d1-80e7-4f7c-9259-9346c976d0f2` |
| 12 | smash onder lime schijnwerpers, glazen wanden met gaten | als 1 | `37426461-c9c1-4292-a556-ba041c030f75` |
| 13 | kerkhofbaan, door de glaswand met reuzenbal | als 3 | `b4892e0a-804c-469c-b2c0-87aa5b9060c4` |
| 14 | filmisch zoals 7, duik terwijl het glas achter hem ontploft | als 1 | `d19b8616-69a4-4451-8a1d-ff549dc71e92` |
