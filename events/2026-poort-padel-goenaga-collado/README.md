# Enrique Goenaga & Guille Collado @ Poort Padel

Briefing voor de aankondigingsposter. Verzameld op 22-09-2026 via Instagram en
padelfip.com.

## Het event

| | |
|---|---|
| Wat | Twee Spaanse profs trainen bij Poort Padel, publiek mag komen kijken |
| Wanneer | **Zondag 27 september 2026, 18:30 – 20:00** |
| Waar | Poort Padel, Almere Poort |
| Programma | Training en wedstrijd, vrij toegankelijk om te bekijken |

## Spelers

### Enrique Goenaga

| | |
|---|---|
| Instagram | [@enri_goenaga](https://www.instagram.com/enri_goenaga/) |
| Volgers | 4.644 (180 posts), geen blauw vinkje |
| FIP-ranking | **57** — 1153 punten, peildatum 24-08-2026 |
| Land | Spanje (Madrid / Salamanca) |
| Sponsor | HEAD Padel, Grupo Bafer Hispanesa |
| Partner | Manu Castaño ([@manucastanoo](https://www.instagram.com/manucastanoo/)) |

> 🏆 x2 Campeón de España · 📊 Matemáticas · 🎾 @head_padel · 📍 Madrid ↔ Salamanca

Wiskundestudent naast zijn padelcarrière. Recent hoogtepunt: met Manu Castaño
de nummer 6-geplaatsten verslagen op de Pretoria Premier Padel P1.

### Guille Collado

| | |
|---|---|
| Instagram | [@guilleecollado__](https://www.instagram.com/guilleecollado__/) |
| Volgers | 11.300 (251 posts), blauw vinkje |
| FIP-ranking | **37** — 1831 punten, peildatum 31-08-2026 |
| Land | Spanje |
| Sponsor | Dropshot, Zumub |
| Speelt met | Pol Hernández ([@polhernaandeez](https://www.instagram.com/polhernaandeez/)) |

> 🏆 World Champion U-18 (2023) · 🏆 World National Champion ('19 '23)
> 🏆 National Champion ('19 '22 '23) · 🤝 @dropshot

De jongste van de twee en het hoogst geklasseerd. Speelde dit seizoen onder meer
de London Premier Padel P1 en Roland-Garros.

### Let op bij de rankings

De briefing noemde #53 en #39. padelfip.com toont nu **57** (Goenaga) en **37**
(Collado). FIP-rankings schuiven wekelijks, dus check de actuele stand vlak voor
publicatie. Veilig alternatief op de poster: "top 60 van de wereld" en
"top 40 van de wereld", of helemaal geen nummer.

## Huisstijl Poort Padel

Afgeleid van [@poortpadel](https://www.instagram.com/poortpadel/) op 22-09-2026.

### Kleuren

| Rol | Hex | RGB |
|---|---|---|
| Lime (accent, vlakken, koppen) | `#CDFD50` | 205, 253, 80 |
| Donkergroen (achtergrond) | `#355B52` | 53, 91, 82 |
| Wit (koptekst) | `#FFFFFF` | 255, 255, 255 |

### Vormtaal

- **Diagonale scheiding** tussen lime en donkergroen is hét signatuurelement.
  Een schuine rand die van linksonder naar rechtsboven loopt.
- **Patroon**: het "P"-logo subtiel herhaald als textuur op de donkergroene vlakken.
- **Logo**: limegroene padelbal met donkergroene "P" erin.
- **Wordmark**: "POORT" in zware schuine kapitalen, daaronder "PADEL" met ruime
  letterafstand.
- **Typografie**: vet, schuin, kapitalen. Ondertitels met veel spatiëring.
- **Call to action**: klein limegroen schuin bannertje met donkere tekst
  (zoals "SCHRIJF JE SNEL IN!" bij de wintercompetitie).
- **Tagline**: MEET • SMASH • RELAX

### Hoe ze een event aankondigen

Kijk naar de wintercompetitie-post: foto van de locatie als achtergrond, daaroverheen
een koptekst waarvan de eerste regel wit is en de tweede lime. Daaronder kleine
witte regels met de details, en onderin het schuine limebalkje met de actie.

## Poster maken

Een kant-en-klare prompt staat in [`POSTER-PROMPT.md`](POSTER-PROMPT.md). Die is zelfstandig: plak het blok in een nieuwe chat en voeg de foto's uit `assets/` toe.

## Beeldmateriaal

Alles in [`assets/`](assets/).

**Sterkste voor een poster:**

| Bestand | Waarom |
|---|---|
| `goenaga-profile.jpg` | Actie, donkere achtergrond, kijkt omhoog naar de bal |
| `goenaga-post-06.jpg` | Volley in volle actie, bal in beeld |
| `goenaga-post-05.jpg` | Rustig portret, wit shirt, schone achtergrond |
| `collado-post-06.jpg` | Gezicht goed in beeld, felblauw shirt |
| `collado-profile.jpg` | Zijprofiel, groene achtergrond, veel lucht eromheen |
| `collado-post-04.jpg` | Zwart-wit, sfeervol, met racket |
| `poortpadel-logo.jpg` | Het balllogo |
| `poortpadel-style-01..03.jpg` | Huisstijlreferentie: logo, wordmark, diagonaal |

**Minder geschikt:** `goenaga-post-01` (reclamebeeld zonder hoofd),
`goenaga-post-02` (vakantiefoto op een boot), `collado-post-05` (detail van een sok).

Let op: het donkergroen van Poort Padel vloekt licht met het felblauw van
Collado's Dropshot-shirt. De zwart-witfoto (`collado-post-04`) of een
duotone-behandeling lost dat op.

## Rechten

Beeldmateriaal komt van de Instagram-accounts van de spelers zelf en van
Premier Padel / FIP. Voor een aankondiging van hun eigen bezoek is dat in de
praktijk zelden een probleem, maar stem het even af met de spelers of hun
management voordat het publiek gaat.

## Poster, versie 1 (22 september 2026)

Gebouwd als HTML/CSS op exact 1080 × 1350, zonder AI-beeldgeneratie. Bestanden:

| Bestand | Wat |
|---|---|
| `poster-1080x1350.png` | Instagram-post 4:5, direct bruikbaar |
| `poster-2160x2700.png` | dezelfde poster op 2×, voor scherm bij Poort Padel of print |
| `poster.html` | de bron: tekst, kleuren en maten |
| `render.sh` | maakt beide PNG's opnieuw uit `poster.html` (Chromium headless) |
| `build/` | de foto's in duotone (donkergroen naar lime) en het witte Poort Padel-logo |
| `fonts/` | Poppins (OFL-licentie), het lettertype van de Poort Padel-huisstijl |

Keuzes in deze versie:

- **Foto's**: Collado links met `collado-profile.jpg`, Goenaga rechts met `goenaga-profile.jpg`. De blauwe shirts botsten met het groen, daarom staan beide foto's in dezelfde duotone (donkergroen, lime in de hoge lichten). `collado-post-06.jpg` (racket boven het hoofd) is ook geprobeerd en staat klaar als `build/collado-duotone.jpg`, maar daar viel zijn gezicht onder de naam.
- **Ranking** als "Top 40 van de wereld" en "Top 60 van de wereld", geen exacte nummers.
- **Tekst**: kop in twee regels (wit, lime), namen groot, datum en tijd als grootste blok, lime CTA-balk "Gratis toegang · kom kijken", adres en site in de voet.

Aanpassen zonder opnieuw ontwerpen:

1. Tekst: open `poster.html`, zoek de blokken met `<!-- TEKST: ... -->` en pas de woorden aan.
2. Maten en kleuren: bovenin `poster.html` staan variabelen (`--headline`, `--name`, `--date`, `--time`, `--photo-top`, `--photo-height`, `--lime`, `--green`).
3. Andere foto: zet een nieuwe duotone in `build/` (het duotone-recept staat in `build_duotone.py`) en wijzig de `src` van de `<img>` in het fotoblok. De uitsnede stuur je met `object-position`.
4. Daarna `./render.sh` draaien; die rendert eerst 1080 × 1450 en snijdt bij naar 1350, omdat Chromium headless anders de onderste 90 px niet schildert.

Nog te doen voor publicatie: toestemming van de spelers of hun management voor de foto's (zie "Rechten" hierboven) en de eventtekst laten checken door Poort Padel.
