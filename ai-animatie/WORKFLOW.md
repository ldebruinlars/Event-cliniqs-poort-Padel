# AI-animatie werkwijze (methode Tudor Morari)

Nagebouwd van [@tudormorari.ai](https://www.instagram.com/tudormorari.ai/) —
428k volgers, tagline "Make AI animations that don't look AI". Hij draait een
30-dagen challenge waarin hij per video zijn volledige workflow laat zien.

Geanalyseerd op 22-09-2026 uit twee van zijn reels: day 12 (jungle hunter) en
day 16 (painterly knight).

## Zijn recept in vier stappen

Alles gebeurt binnen higgsfield.ai. Hij claimt onder de 20 minuten per animatie.

### Stap 1 — het personage

Model: **GPT Image 2** (of Nano Banana Pro).
Zijn eigen foto in referentieslot 1.

> Turn me into a painted jungle hunter: fur collar, war paint, an axe, crouched
> in the green. **Same face, same beard.** Painterly concept art, teal and green light.

Twee dingen doen het werk: `same face, same beard` zet je identiteit vast, en de
stijlregel achteraan bepaalt de look.

### Stap 2 — het tweede element

Zelfde model.

> **Same painted style.** A huge tiger stalking low through the jungle, eyes on
> the viewer, teal shadows, wet ground.

`Same painted style` is de lijm tussen de beelden.

### Stap 3 — de omgeving

Zelfde model.

> **Same painted style.** An ancient jungle: giant mossy trees, hanging vines, a
> still pool reflecting green light. **Empty, no characters.**

Leeg genereren is essentieel: de personages komen er in stap 4 pas in.

### Stap 4 — de animatie

Model: **Seedance 2.5**. Alle drie de beelden in de referentieslots 1, 2 en 3.
En dan de truc:

> **@[hunter]** waits in **@[forest]**, an axe in his hand. **@[tiger]** steps out
> of the trees, low and slow. The camera drops with the tiger, both of them still.
> Painterly, **one continuous shot.**

Hij verwijst met **@-mentions** naar de genummerde referentiebeelden. Zo vertel je
het videomodel wie waar staat en wie beweegt, zonder dat het zelf iets hoeft te
verzinnen. `One continuous shot` voorkomt dat het model gaat knippen.

## Waarom dit werkt

| Probleem | Zijn oplossing |
|---|---|
| Gezicht verandert | `Same face, same beard` plus je foto als referentie |
| Beelden passen niet bij elkaar | `Same painted style` in elke prompt |
| Model propt alles in één beeld | Elementen los genereren, pas in de video samenvoegen |
| Video wordt een rommelige montage | `One continuous shot` |
| Camerawerk is willekeurig | Camera expliciet beschrijven: "the camera drops with the tiger" |

## Onze padel-variant

Zelfde vier stappen, andere inhoud. Kleuren afgestemd op Poort Padel
(lime `#CDFD50`, donkergroen `#355B52`).

**1. Het personage** — GPT Image 2, met Lars' foto als referentie:

> Turn me into a painted padel champion: navy blue kit with lime green accents,
> a padel racket gripped in his right hand, standing mid-court and focused,
> shoulders squared to the viewer, sweat on the brow. Same face, same beard,
> same hair, same build. Painterly concept art, thick visible brush strokes,
> deep teal-green shadows and lime green rim light.

**2. De bal** — met beeld 1 als stijlreferentie:

> Same painted style. A padel ball streaking through the air toward the viewer,
> lime green glow, long motion trail, droplets of light catching the glow.
> Deep teal-green background. Empty, no characters.

**3. De baan** — met beeld 1 als stijlreferentie:

> Same painted style. An empty indoor padel court at night: glass walls, dark
> blue floor, black steel frame, stadium lights cutting through haze. Deep
> teal-green and lime green light. Empty, no characters.

**4. De animatie** — Seedance 2.5, alle drie als referentie:

> @[1] stands ready on @[3], racket up, breathing hard. @[2] streaks toward him
> and he swings through a smash. The camera pushes in low and slow. Painterly,
> one continuous shot.

## Wat het kost

| Stap | Model | Credits |
|---|---|---|
| Beeld 1, 2 en 3 | GPT Image 2, 2k, high | 2 per stuk |
| Animatie | Seedance 2.5 | zie onder |

Beelden zijn spotgoedkoop, dus experimenteer daar vrij mee. De video is de
grote post. Reken de kosten altijd eerst voor met `get_cost: true` voordat je
een video wegzet.

## Praktische notities

- **Het uploadvenster van Higgsfield werkt niet in Claude Code.** Gebruik
  `media_upload` voor een presigned URL, stuur de bytes met `curl -X PUT`, en
  bevestig daarna met `media_confirm`.
- **Verticaal 9:16** voor Reels en TikTok.
- **Referentiefoto**: kies er een waarop het gezicht groot en scherp in beeld is.
  Een actiefoto van veraf geeft een slechtere gelijkenis.
- Je kunt een gegenereerd beeld als referentie voor het volgende gebruiken door
  het **job-id** door te geven in plaats van een media-id.

## Resultaten

### Beeld 1 — het personage

`assets/01-champion.png` (1520x2688), gemaakt van `assets/00-bronfoto-lars.jpg`.

Wat er goed ging, en beter dan verwacht: het shirt draagt **leesbaar**
"POORT PADEL" met het Academy-logo ernaast, ook op de broek en op het racket.
GPT Image 2 is sterk in typografie, en met de bronfoto als referentie neemt hij
bestaande logo's over.

Dat is een belangrijke nuance op de regel "AI kan geen tekst": **logo's
overnemen van een referentiefoto lukt wel, tekst die het model zelf moet
verzinnen niet.** Een datum op een poster blijft dus handwerk.

Gelijkenis is goed: haar, baard en glimlach kloppen.

### Volgende beelden

Beeld 2 (de bal) en beeld 3 (de baan) gebruiken beeld 1 als stijlreferentie via
het job-id, niet de oorspronkelijke foto. Dat houdt de schilderstijl consistent,
wat sterker werkt dan Tudor's aanpak waarbij hij zijn eigen foto in het slot
laat staan.

## Wachttijden

Higgsfield kan traag zijn. Beeld 1 stond ruim een kwartier op `queued` voor 2
credits. Dat is geen fout aan de prompt — gewoon hun wachtrij. Niet opnieuw
indienen, gewoon wachten.

### Beeld 2 en 3

`assets/02-bal.png` en `assets/03-baan.png`. Stijl is consistent met beeld 1:
zelfde penseelstreek, zelfde palet, zelfde licht. Het model zette ongevraagd
het Poort Padel-logo op de bal, overgenomen uit beeld 1.

### De animatie

`assets/04-animatie-mini.mp4` — 8 seconden, 720x1280, **Seedance 2.0 Mini,
8 credits**.

De @-verwijzingstechniek werkt ook via de API zonder de `@[naam]`-syntax uit de
webinterface. "The player from the first reference... the ball from the second
reference... the court from the third reference" is genoeg; de referenties gaan
in volgorde mee als `image_references`.

Wat de animatie doet: wijd begin met Lars op de lege baan, de gloeiende bal
komt met een spoor naar beneden, hij rent en springt in de smash, camera duwt
door naar een close-up van zijn gezicht. Eén doorlopende shot, geen knip.

**Wat minder goed ging:** de tekst op het shirt brokkelt af tijdens beweging
("POORT" wordt "POOR"), en het gezicht wordt in de laatste close-up jonger en
gladder dan het origineel.

## Volledige kostenoverzicht

| Onderdeel | Model | Credits |
|---|---|---|
| Beeld 1, 2, 3 | GPT Image 2, 2k high | 6 |
| Animatie testversie | Seedance 2.0 Mini, 8s 720p | 8 |
| Animatie eindversie | Seedance 2.5, 8s 720p | 56 |

Totaal voor een geslaagde animatie: **14 credits om te testen**, en pas daarna
de 56 voor de mooie versie. Tudor draait meteen op 2.5; testen op Mini scheelt
een hoop als de compositie nog niet klopt.

## Versie 2: de fouten eruit

Drie problemen uit versie 1 aangepakt met één langere prompt
(`prompt-v2-animatie.txt`, 377 woorden tegenover 68).

**Wat er veranderde:**

| Probleem | Oplossing |
|---|---|
| Raakmoment niet zichtbaar | Eigen blok `SECONDS 4-5. THE CONTACT` met racketmidden, indrukkende bal, verfexplosie, en de regel "must be clearly visible and unmistakable" |
| Geen tegenstander | Vijfde beeld `05-tegenstander.png` als vierde referentie |
| Gezicht verjongt | Eigen `IDENTITY`-blok, expliciet "do not smooth, youthen or slim", en het einde verplaatst van extreme close-up naar medium shot |
| Tekst brokkelt af | "keep the POORT PADEL wordmark sharp, stable and readable in every frame" |

**Resultaat** (`assets/06-animatie-v2-mini.mp4`): alle vier opgelost.

De grote les is de **structuur**, niet de lengte. Een prompt als tijdlijn met
genummerde secondeblokken wordt aanzienlijk beter gevolgd dan dezelfde
informatie in een lopende zin.

### Let op bij het controleren

Het raakmoment duurt ongeveer 0,2 seconde. Bij frames trekken op 2 per seconde
mis je het en concludeer je ten onrechte dat het ontbreekt. Trek rond het
verwachte moment frames op **12 per seconde**:

```bash
ffmpeg -ss 2.0 -t 2.5 -i video.mp4 -vf "fps=12,scale=250:-1" frames/i_%02d.jpg
```

### Preset-waarschuwing

Higgsfield stelde bij deze prompt de preset "IN THE DARK" voor, een
survival-horror laadscherm. Dat gebeurt op losse woorden zoals "dark" en negeert
je referenties volledig. Afwijzen met `declined_preset_id` en letterlijk
genereren.
