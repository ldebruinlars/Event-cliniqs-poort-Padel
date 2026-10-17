---
name: aca-ai-animatie
description: Werkwijze voor korte AI-animaties (Reels, TikTok, Shorts) voor All Court Academy en Poort Padel met Higgsfield (Nano Banana Pro, GPT Image, Seedance) en eventueel Blender. Gebruik bij elke vraag om een animatie, korte video, character sheet, personage, omgeving of storyboard te maken, ook als Lars het casual vraagt ("maak een filmpje", "meer characters", "storyboard", "character sheet", "animatie voor de post"). Voorbeeld: Halloween-short oktober 2026.
---

# AI-animatie (ACA × Poort Padel)

Lees eerst `ai-animatie/WORKFLOW.md` (eerste experimenten, kosten) en het voorbeeld `events/2026-halloween-padel/video/characters/README.md`. Gebaseerd op eigen ervaring plus de technieken uit de MIT-repo's alew3/skills (higgsfield-seedance-video-suite) en elementsix/elementsix-skills (seedance-storyboard), in eigen woorden.

## Volgorde

1. **Brief**: lengte (standaard 15 s, 9:16), toon, wie er meespeelt, wat de kijker moet doen (boeken). Inspiratie: Pinterest-keuzebord (zie CLAUDE.md, Make-tool Pinterest) en Lars laat per groep kiezen.
2. **Identiteitsblok per personage**: 30 tot 50 woorden, vaste volgorde (silhouet en hoofd, ogen, kleuren, bouw, kenmerk, kleding, prop). Elke prompt begint met dit blok, woord voor woord; daarna `// SCENE:` met alleen pose, expressie en camera. Eén woord anders = ander personage.
3. **Master per personage**: één vooraanzicht, neutraal, plat licht, lichtgrijze achtergrond, 3:4. Pas na akkoord de sheets, altijd met de master als referentie (job-id in `medias`).
4. **Character sheet**: Higgsfield-workflow `character-sheet` (laden met `get_workflow_instructions`). Opbouw die Lars koos: bovenaan een rij koppen met expressies, daaronder de hele figuur van voor, 3/4, zij en achter. Een sheet die te veel wil (turnaround + expressies + kleurvakken in één beeld) verprutst de onderste rij: liever twee beelden. Mislukt paneel: alleen dat paneel opnieuw vanaf de master, "change only X, keep everything else identical".
5. **Omgeving**: eerst een lege brede master met een vaste "location bible" (indeling, materialen, schaal, lichtrichting en kleurtemperatuur). Daarna aanzichten A tot F met dezelfde bible en "no people, geometry identical". Lichtrichting nooit omdraaien.
6. **Storyboard**: 15 s = 5 of 6 panelen. Per paneel: tijd, shotgrootte, één camerabeweging, onderwerp plus één werkwoord, geluid, links/rechts-posities. Ter keuze één 16:9-overzicht met bijschriften; voor productie elk paneel apart (9:16) met masters als referentie, zodat het een startbeeld voor video kan zijn. Maak meerdere varianten en laat Lars kiezen.
7. **Video**: Seedance omni-reference (max 9 beelden, `mode: "omni_reference"`), elke referentie één taak ("first reference = Pompie, character reference"). Prompt: kopregel (stijl, duur, formaat, sfeer), dan tijdblokken "0-3s: camera, scène, actie, licht", dan geluid. Eén camerabeweging per shot, zeg ook wat de camera niet doet. Vermijd het woord "fast" (geeft rommel), schrijf "quick but smooth". Negatief: benoem het concrete artefact (morphing, face drift, flicker, extra fingers) en koppel aan een positieve regel. Testen op Seedance 2.0 Mini 480p, pas daarna 2.5.
8. **Eindkaart en tekst** erover in de Higgsfield-sandbox (ffmpeg), nooit tekst laten genereren.

## Echte (foto-realistische) personages

- Seedance weigert (status `nsfw`, credits terug) zodra er meerdere foto-echte gezichten als referentie meegaan. Eén startbeeld met een gezicht werkt wel.
- Daarom shot voor shot: per shot een 9:16-startbeeld met het personage in de echte omgeving vanuit de gekozen camerahoek (Nano Banana Pro met master + omgevingsmaster als referentie), dan image-to-video per shot (Seedance 2.0 Mini 4 s = 2 credits) en monteren met ffmpeg. Camerahoeken en gezichten liggen zo vast.
- Per personage: master, hoofdsheet (5 hoeken + expressies), lijf-turnaround; plus prop-sheet (rackets merkloos!) en omgevingssheet met de camerahoeken van de shotlijst.
- Vermijd lage hoeken van achteren op mensen in korte sportkleding (filter).
- Voorbeeld: `events/2026-halloween-padel/video/echt/README.md`.

## Blender

- `/use-blender` (Higgsfield) werkt alleen in Claude Code op Lars' eigen computer.
- In de cloud: Higgsfield 3D Jutsu (`scene_builder_3d_*`, gehoste bpy, alleen catalogusmodellen) of `pip install bpy==5.0.1` in een Python 3.11-venv (container of Higgsfield-sandbox). Goed voor camerapaden, blocking en een vaste ruimte; personages zelf animeren in Blender wordt stijf, dus figuren via Seedance.

## Taal

- Alle prompts naar Higgsfield, Seedance, Blender en andere AI-tools in het Engels: die modellen volgen Engels het best. Namen van personages mogen Nederlands blijven.
- Alles wat Lars of klanten zien (bijschriften, eindkaart, captions, uitleg) in het Nederlands, en altijd zelf erover zetten, nooit door het model laten schrijven.

## Praktisch

- Higgsfield-bestanden zijn niet te downloaden vanuit de container. Bekijken en samenvoegen in de Higgsfield-sandbox (`sandbox_exec` met `image_paths`), uploaden met `media_upload` + PUT + `media_confirm`.
- Nano Banana Pro 2k kost 2 credits per beeld; batch met `generate_image_batch`, wachten met `jobs_wait`.
- Het model zet soms Engelse labels onder sheet-plaatjes. Controleer de spelling of plak eigen labels erover.
