# De Spookbaan v2: shotplan 20 s (9:16)

Feedback Lars op v1: shots niet goed, personages komen niet tot leven, moest 20 s zijn. Aanpak v2:

- Skill `filmmaker` (dylantarre/animation-principles, via find-skills/skills.sh) geïnstalleerd in `.claude/skills/filmmaker`: anticipatie, follow-through, secondary action, staging, exaggeration, 180-gradenregel, cut on action.
- Seedance 2.5 met **startbeeld én eindbeeld** per acteershot: het model moet van pose A naar pose B, dus echte beweging en acting in plaats van zweven.
- Echte camerahoeken per shot, geen vlakke middentotalen meer. Team ACA (Mila, coach) altijd links in beeld en kijkt naar rechts; monsters rechts en kijken naar links.
- Knippen op actie (impact, landing, blik), niet op vaste tijden.

| # | Tijd | Shot en camera | Acting / actie (start → eind) | Geluid | Cut |
|---|---|---|---|---|---|
| 1 | 0,0-1,5 | ECU, vast: inktdruppel op papier (v1-clip) | druppel → spat | diepe drup-echo | op de spat |
| 2 | 1,5-3,5 | worm's-eye in het bos, tilt omhoog mee met lantaarn | lantaarn drijft over | wind, uil | als lantaarn uit beeld is |
| 3 | 3,5-5,5 | strakke OTS achter Mila, langzame push-in | ze stapt, krullen veren na, ze stopt bij het hek | voetstappen grind | op haar stop |
| 4 | 5,5-7,0 | ECU gezicht Mila, frontaal | kalm → ogen wijd, hap naar adem (pompoen in haar ogen) | adem, hartslag | op de gasp |
| 5 | 7,0-9,5 | heel laag op de baan, onder het net door | pompoentop in inktplas → Pompoenman rijst op, gezicht ontbrandt | inkt-gorgel, vuur | als gezicht oplicht |
| 6 | 9,5-11,0 | Dutch angle breed, crane omhoog | heks, weerwolf, bruid gebukt → schaterlach, huil, sluier open | huil, kakellach | op de huil |
| 7 | 11,0-12,5 | MCU coach, ooghoogte | grijns, fluitje, wangen bol, gooit bal op | fluit | op de fluit |
| 8 | 12,5-15,0 | laag zijaanzicht, maan erachter | opgerold → sprong-smash, slowmo bij impact, oranje inktstreep | donder, klap | op de impact |
| 9 | 15,0-16,5 | laag breed, Mila duikt; dan Pompoenman | duik en return → bal tegen pompoenkop, kop draait scheef | bonk, 'boing' | op de draai |
| 10 | 16,5-20,0 | medium-breed aan het net | iedereen lacht, high-five over het net; eindkaart vanaf 17,3 s | lachen, racketklak | einde |

Prompts: Engels, stijlblok "Japanese sumi-e ink wash animation on crumpled cream rice paper", per shot één camerabeweging, acting in tijdblokken, concrete negatieven (no morphing, no face drift, no extra limbs).

## Resultaat v2 (Seedance 2.5, 720p, 4 s per shot)

- Start + eindbeeld samen (`start_image` + `end_image`) faalde bij Seedance 2.5 drie keer zonder foutmelding. Werkt wel: `start_image` plus het eindbeeld als `image_references` en in de prompt "the reference image shows the final pose to reach". Het model springt rond 2,4 s naar die pose; daar knippen.
- Preset "IN THE DARK" afgewezen met `declined_preset_id`.

| # | Video-job | Knip (start / lengte) | Tijd in film |
|---|---|---|---|
| 1 inktdruppel (v1, Mini) | `e3c86538-8b72-40a3-ac35-80a4a91afccc` | 0,3 / 1,2 | 0,0-1,2 |
| 2 lantaarn worm's-eye | `282ec339-924d-455b-a8e3-246ee7b8d577` | 0,2 / 1,8 | 1,2-3,0 |
| 3 OTS Mila naar het hek | `c00c9871-c58d-4483-a5a1-2d41ddb8c3f4` | 0,3 / 1,8 | 3,0-4,8 |
| 4 ECU Mila, knipper → gasp | `e6cf61a0-94fd-4b5c-9336-2ed794df9de6` | 1,5 / 2,0 | 4,8-6,8 |
| 5 Pompoenman rijst uit inkt | `6a1bee7f-6b26-4701-bd04-5c3d88c835ba` | 0,8 / 2,6 | 6,8-9,4 |
| 6 heks, weerwolf, bruid | `5650eb7c-3f5a-4117-af3a-552bc3cae390` | 0,6 / 1,6 | 9,4-11,0 |
| 7 coach, fluitje | `400f3155-d118-4c1f-96ea-67b949332bae` | 0,8 / 1,2 | 11,0-12,2 |
| 8 smash voor de maan | `2ac9d8fb-e4ca-4179-91c4-489eedeb3073` | 1,0 / 2,6 | 12,2-14,8 |
| 9 Mila duikt | `f2afd913-6cb2-426e-825e-d4d406da3432` | 0,2 / 1,4 | 14,8-16,2 |
| 10 pompoenkop draait | `282e53e9-5cf9-456a-bcaf-8d854438a537` | 0,2 / 1,2 | 16,2-17,4 |
| 11 samen lachen, high-five | `28e1b0de-8ae9-4d1a-ba2e-b42a73645312` | 0,5 / 2,6 | 17,4-20,0 |

Eindkaart v2 vanaf 17,9 s met fade, audio fade-out vanaf 19,2 s. Media `9f39d367-8e2c-480e-ad5c-035c8a276aa5`, bestand `spookbaan-v2-20s.mp4`, https://d2ol7oe51mr4n9.cloudfront.net/user_3DTi6Z7G6lm7S5aYIwHXC1iM486/9f39d367-8e2c-480e-ad5c-035c8a276aa5.mp4

Kosten: 11 clips Seedance 2.5 720p en 14 key frames; saldo na afloop 2438 credits (begin van de dag 2823, inclusief keuzeset, startbeelden en test v1).

## v3: minder cuts, vloeiend (Seedance 2.0 Mini 480p)

Feedback Lars op v2: te veel cuts, voelt random; bos/lantaarn eruit. Nu 4 lange shots (5-6 s), elke cut met een reden (zij kijkt over het net → wat ze ziet). Per shot twee varianten, beste gekozen. 8 clips Mini ≈ 22 credits.

| Shot | Tijd | Inhoud | Gekozen job | Afgevallen |
|---|---|---|---|---|
| A | 0,0-4,8 | Mila en coach lopen de kerkhofbaan op, zij draait haar hoofd naar het net | `8149ff54-2512-4237-afe0-51b74cebc8d6` | `723a2694-…` (lopen naar camera) |
| B | 4,8-9,6 | Pompoenman rijst uit de inkt, heks, weerwolf, bruid erachter, gezicht ontbrandt | `43d5a973-8916-4a69-9a7e-a2313feb8110` | `baacefd0-…` |
| C | 9,6-15,3 | smash, bal over het net, Mila returnt, Pompoenman close | `9259c02a-0efc-4030-b4f1-8249f6a7a42d` | `4ec4735f-…` (springt naar leeg papier) |
| D | 15,3-20,0 | samen lachen, high-five; eindkaart vanaf 17,6 s | `5506438f-fddf-4f71-9ad5-7b41cbf1708d` | `28d52314-…` (zoomt te ver uit) |

Resultaat: media `a6465d87-f0d0-47fc-a437-763e6ee64d2e`, bestand `spookbaan-v3-20s-mini.mp4`, https://d2ol7oe51mr4n9.cloudfront.net/user_3DTi6Z7G6lm7S5aYIwHXC1iM486/a6465d87-f0d0-47fc-a437-763e6ee64d2e.mp4

Les: lange shots met referenties per personage (`image_references`) en één doorlopende camerabeweging geven een rustiger, logischer film dan veel korte clips. Mini doet 4-15 s per clip.

## v4: shot C als echte padelwedstrijd (Seedance 2.0 Mini 480p)

Feedback Lars op v3: de match moet met iedereen en de teams aan weerszijden van het net, als een echte padelwedstrijd.

- Startbeelden (Nano Banana, 3 × 2 credits) met alle personages als referentie: M1 `8788c55b-0dc3-49b1-866c-eb7dbc2f0c6d`, **M2 `1f6a6fd2-8dfd-41d5-90f4-7d55e301d30b` (gekozen)**, M3 `8576672f-cec8-4286-9eac-a23458543e79` (geen echte baan). Bestanden in `v3-match/`.
- Opstelling: tv-hoek hoog achter de baseline. Mila (achter) en coach (net) tegen Pompoenman (achter) en weerwolf (net); heks in de scheidsrechtersstoel, spookbruid kijkt door het zijglas.
- Rally op Mini, 6 s, 3 varianten: `08c97b84-381b-4c22-8232-65bb0c82c8d4`, **`070c24c8-5115-41b8-bb9b-d43eadeb6c0a` (gekozen: service, volleys, sprong-smash, iedereen blijft aan zijn kant)**, `a03b6ac2-3017-4014-a5e1-1ebdc3b96dd8`.
- Montage gelijk aan v3, alleen C vervangen (9,6-15,3 s). Media `0b76a885-c742-48ad-9132-e5923b38b6a1`, bestand `spookbaan-v4-20s-mini.mp4`, https://d2ol7oe51mr4n9.cloudfront.net/user_3DTi6Z7G6lm7S5aYIwHXC1iM486/0b76a885-c742-48ad-9132-e5923b38b6a1.mp4
- Prompt-les: "each team stays on its own side of the net, nobody crosses the net, no characters swap sides" plus een startbeeld met de juiste opstelling houdt de teams op hun helft.
