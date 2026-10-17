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
