# Character sheet korte animatie (cute maar griezelig)

Stand 17 oktober 2026. Nieuwe stijl voor de Halloween-short: schattige 3D-figuren (clay-toy, animatiefilm-look) in plaats van de comic-halftone uit `../script-v2.txt`. Kleding en kleuren zijn van de oude pompoenspeler en het oude spook overgenomen, zodat het bij de poster blijft.

Gemaakt met de Higgsfield-workflow `character-sheet` (preset `3d-stylized`), model Nano Banana Pro, 2k, 16:9, 2 credits per beeld.

## Cast (namen zijn voorstellen)

- **Pompie**: pompoenkop met ribbels en krulsteeltje, gloeit van binnen oranje; in spookmodus ogen en grijns lime met een lime vlammetje. Zwart shirt met lime randje en pompoen-logo, zwarte short met lime streep, lime polsbanden, gescheurde oranje-zwarte cape, zwart racket met lime stippen.
- **Boo**: klein wit lakenspookje met zwevend staartje, grote zwarte ovale ogen, roze wangetjes, paarse hoofdband en polsbanden, wit racket met paarse stippen. Ongeveer twee derde van Pompie's hoogte.
- **Spookbal**: lime padelbal met spookgezichtje en lime gloed; plat bij de klap met oranje-lime vonken.

## Higgsfield jobs

| Wat | Job |
|---|---|
| Pompie, turnaround (onderste rij mislukt, niet gebruiken) | `90744dbe-ec14-459d-a00a-978d25245ed4` |
| Pompie, zes gezichten en vier poses | `61c959ab-56b5-403a-866e-69ac28291a63` |
| Boo, turnaround, gezichten en poses | `eff639d4-6efd-42da-b19c-6629a8c2d8f6` |
| Cast met hoogte, spookbal, rackets, lantaarn, vleermuis | `021db00b-1c2f-4c25-98dd-9d95d73e926c` |
| Alles samen op één sheet (4040 × 2682, media) | `d6888bf0-52ba-415a-8d66-4d8b94695153` |

Complete sheet: https://d2ol7oe51mr4n9.cloudfront.net/user_3DTi6Z7G6lm7S5aYIwHXC1iM486/d6888bf0-52ba-415a-8d66-4d8b94695153.jpg

## Lessen

- Een volle sheet (turnaround plus expressies plus swatches) in één beeld: de onderste rij gaat mis (vage gezichten, donkere rand). Beter: turnaround en expressies als aparte beelden, met de turnaround als referentie (job-id) voor de rest.
- Voor een gesneden pompoengezicht expliciet "clearly carved face, candle glow from inside the cut-outs" en per expressie de vorm van de uitsnijding beschrijven.
- Het model zet soms toch Engelse labels onder de plaatjes, ook met "no text". Die waren hier correct gespeld.
- Samenvoegen gebeurt in de Higgsfield-sandbox (ImageMagick, Montserrat), daarna `media_upload` en `media_confirm`. Higgsfield-bestanden zijn vanuit de cloudcontainer niet te downloaden.

## Blender

- De Higgsfield-opdracht `/use-blender` werkt alleen op Lars' eigen computer (Claude Code lokaal), niet in deze cloudomgeving.
- Wel mogelijk: Higgsfield 3D Jutsu (gehoste Blender, `scene_builder_3d_*`), en Blender als Python-module (`pip install bpy==5.0.1` in een Python 3.11-venv) in de container of in de Higgsfield-sandbox. 3D Jutsu kan alleen catalogusmodellen importeren, geen eigen GLB.

## Pinterest-referenties

Keuzebord met 30 referenties (A stijl, B opbouw sheet, C sfeer, D animatie-look), gekozen uit 161 pins van openbare Pinterest-pagina's (ideeën: 3D ghost, cute ghost 3D model, 3D Halloween animation, pumpkin head drawing cute; borden met model sheets en 3D-animatieshorts). Media `07b8bff6-640b-4079-9c4d-1180eb5d2d1b`:
https://d2ol7oe51mr4n9.cloudfront.net/user_3DTi6Z7G6lm7S5aYIwHXC1iM486/07b8bff6-640b-4079-9c4d-1180eb5d2d1b.jpg

Alleen als inspiratie voor stijl en opbouw; niets letterlijk overnemen.

## Versie 2 van de cast (keuze Lars: stijl A2, opbouw B2, meer en engere personages, grotere omgeving)

Stijl: matte kleifiguurtjes, expressief (A2). Sheets: bovenaan zeven koppen met expressies, daaronder vijf hele aanzichten (B2). Eerst een master per personage, daarna de sheet met de master als referentie.

**Character bible (alles op één beeld):** https://d2ol7oe51mr4n9.cloudfront.net/user_3DTi6Z7G6lm7S5aYIwHXC1iM486/836766cf-2319-4858-ae8d-2a54b3d12197.jpg

| Personage | Master | Sheet |
|---|---|---|
| Pompie (Team Schattig) | `a9bb1579-a259-4bcd-936e-13d1778da55e` | `a1f793ee-bc04-4d7c-919d-6d3d780aebc7` |
| Boo (Team Schattig) | `720f025a-39a9-434b-b093-e582de4153cf` | `5d970daf-a0c8-4f2b-b2f6-922b10214bc6` |
| Knekel, skelet (Team Griezel) | `494b82e4-65f3-4912-ab4b-0585eb569dbe` | `5b148927-aefb-442d-8d31-49916a8b918e` |
| Graaf Vlad, vampier (Team Griezel) | `903ad8e7-a9b4-478c-aac6-0a92dd91a257` | `b2e1a1ee-635a-4325-9ef8-96218229d3b0` |
| Mummie, scheidsrechter | `88eeea45-c4a3-4663-b26c-789e37713f77` | `b55a7438-c218-4c8a-96bc-a81ef161059a` |
| Cast-lineup met hoogtes | | `201b80f7-d870-45a4-83a8-9b0f82c7a3aa` |
| Spookpark, lege master | `86326559-f5ca-40f8-a243-b89e40fd1695` | zes aanzichten `7fbe5599-439a-451b-986a-fc5c38ff8213` |

### Identiteitsblokken (woord voor woord hergebruiken)

- **Pompie**: Pompie, a small chibi pumpkin-head padel player toy: big round matte orange pumpkin head with deep ribs and a curly green stem with one leaf, carved triangle eyes and a jagged grin with two square teeth glowing warm candlelight from inside, short round body, stubby limbs, black gloves. Wearing black sports shirt with neon lime collar and small orange pumpkin emblem, black shorts with lime stripe, lime wristbands, tattered orange-black cape, black shoes with lime soles, black padel racket with lime dots.
- **Boo**: Boo, a small round white bedsheet ghost toy, soft matte cloth with gentle folds, wavy hem tapering into a floating tail, no legs, two stubby cloth arms, big glossy black oval eyes, small mouth, rosy pink cheeks, faint inner glow. Deep purple headband and wristbands, white padel racket with purple dots.
- **Knekel**: Knekel, a lanky cartoon skeleton padel player toy, oversized round skull with a cracked crown, deep eye sockets with tiny glowing neon lime pupils, wide toothy grin with one missing tooth, thin bone arms and legs, slightly hunched. Wearing a torn faded black-and-bone-white striped sports shirt hanging loose on the ribcage, black shorts, mismatched socks, worn black shoes, a cracked bone-white padel racket held together with tape.
- **Graaf Vlad**: Graaf Vlad, a tall thin cartoon vampire padel player toy, pale grey-green skin, sharp widow's peak of slick black hair, pointed ears, narrow glowing red eyes, two small white fangs in a sly smile, long thin fingers. Wearing a high-collared black cape with blood-red lining over a deep burgundy sports shirt, black shorts, black socks, pointed black shoes, black padel racket with blood-red dots.
- **Mummie**: Mummie, a chubby cartoon mummy umpire toy, wrapped head to toe in loose dusty cream bandages with a few trailing ends, one big glowing amber eye peeking through a gap, the other covered, round belly, short legs. Wearing a referee whistle on a black cord and a tiny black umpire cap, holding a small blank scorecard.
- **Stijl**: stylized 3D render of a matte clay figurine, soft sculpted forms with subtle clay texture, expressive face, Pixar-style appeal, cute but a little creepy.

## Storyboards (drie versies, Lars kiest)

| Versie | Verhaal | Paneel-job | Bord met bijschriften |
|---|---|---|---|
| 1 De Spookwedstrijd | Team Schattig tegen Team Griezel, smash als climax | `cbbf48a9-5473-41d6-abb9-e29f9abdefc2` | https://d2ol7oe51mr4n9.cloudfront.net/user_3DTi6Z7G6lm7S5aYIwHXC1iM486/e214804e-5e2b-41eb-aa08-38fd71fe039e.jpg |
| 2 Wie durft? | begint als horror, eindigt schattig | `1f8a507c-4cca-4d4c-8039-637e346692f1` | https://d2ol7oe51mr4n9.cloudfront.net/user_3DTi6Z7G6lm7S5aYIwHXC1iM486/ad79a0ad-eba1-485c-b45b-d5d1e80e3df1.jpg |
| 3 De Kostuumkeuring | verkleed = goedgekeurd = korting | `2438c6bd-d21d-42b2-bc62-343c532d9bcf` | https://d2ol7oe51mr4n9.cloudfront.net/user_3DTi6Z7G6lm7S5aYIwHXC1iM486/9c7f8637-690b-4a85-8a5a-cc8ec1bde133.jpg |

Bijschriften staan in `board.py`-stijl in de Higgsfield-sandbox gemaakt (PIL, Montserrat); de panelen zelf hebben geen AI-tekst. Eindkaart voor alle versies: ZA 31 OKTOBER · KOM VERKLEED = 50% KORTING · LINK IN BIO.

## Test: versie 3 met de smash uit versie 1 (Seedance 2.0 Mini, 480p, 15 s, 7,5 credits)

- Job `f27f7ed2-3d7f-4882-9282-11a3aa1fc77f`. Referenties: de vijf masters plus de spookpark-master. Preset-suggestie "CLAY FIGURINE" afgewezen (`declined_preset_id`), anders worden de referenties genegeerd. `genre: comedy`.
- Met eindkaart (`../eindkaart-v2.html`, opgeschaald naar 1080 × 1920, eindkaart vanaf 12,4 s met fade): media `5b90462b-1d1d-46ab-9e23-ebc24aef99cd`, https://d2ol7oe51mr4n9.cloudfront.net/user_3DTi6Z7G6lm7S5aYIwHXC1iM486/5b90462b-1d1d-46ab-9e23-ebc24aef99cd.mp4
- Beoordeling: alle zes beats komen in beeld, personages blijven herkenbaar, smash met vonken voor de maan zit er duidelijk in. Kleine punten: het model zet een woordje op de scorekaart, Knekel houdt de pompoen vast in plaats van hem op te zetten.
- Eindversie kost (15 s, 9:16): Seedance 2.5 720p 105, Seedance 2.0 1080p 180, Seedance 2.5 1080p 240 credits.

## Test: versie 1 De Spookwedstrijd, meer actie (Seedance 2.0 Mini, 480p, 15 s, 7,5 credits)

Lars koos de wedstrijd ("veel meer actie en leuker om te zien"). Prompts altijd in het Engels.

- Job `5e0b7840-fce3-4c3c-9545-61d461c193d9`, `genre: action`, zelfde zes referenties, preset afgewezen. Extra in de prompt: blok COURT GEOMETRY (Team Schattig links, Team Griezel rechts, nooit dezelfde kant op kijken), drone-duik, rally met kaak eraf en bal glas-op-glas, lob naar de maan, slowmotion smash met 180 graden orbit.
- Met eindkaart vanaf 12,6 s: media `926aa301-3bc6-4ec4-a21d-76e1cc1265bf`, https://d2ol7oe51mr4n9.cloudfront.net/user_3DTi6Z7G6lm7S5aYIwHXC1iM486/926aa301-3bc6-4ec4-a21d-76e1cc1265bf.mp4
- Goed: bliksem-haakje, drone-duik over het park, rally, smash met grote vonkenexplosie, Vlads cape over zijn hoofd, groepsviering voor het clubhuis.
- Verbeteren in de eindversie: de openingsclose-up van Mummie heeft de grijze studio-achtergrond van de master overgenomen. Toevoegen: "the opening close-up is set outside at night against a dark stormy sky, never a grey studio background".
