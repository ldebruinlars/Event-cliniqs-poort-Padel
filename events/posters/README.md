# Posters Padel Dating

Gemaakt op 18 september 2026 met Higgsfield (beeld) en Canva (bewerkbare poster). De afbeeldingen zelf staan niet in deze repo omdat de download vanuit de bouwomgeving geblokkeerd was; alles staat in Lars' Canva-account en Higgsfield-bibliotheek.

## Stijlronde 5: eigen karakters in de echte Poort Padel-ruimtes, in de 3 gekozen stijlen (nieuwste)

Lars koos drie voorbeelden als favoriet: (1) warm groen en koraal met een polaroid, (2) roze met hartjes, (3) donker cinematisch met een elegante serif in de eventruimte. Op 18 september 2026 zijn daarvoor eerst vier originele karakters gemaakt en daarna dating-foto's in de echte ruimtes van Poort Padel, en pas daarna de posters.

Zo is het gedaan met Higgsfield:

1. Karakters via de `character-sheet`-workflow (`get_workflow_instructions`): vier originele volwassenen, fotorealistisch en onbewerkt (zichtbare huidtextuur, geen modellenlook), neutrale studio-achtergrond, sportkleding in de clubkleuren. Model Nano Banana Pro.
2. Elk karakter opgeslagen als reusable Element (`show_reference_elements`, actie `create`), zodat dezelfde gezichten in meerdere foto's terugkomen. Elements werken met meerdere personen per beeld; Soul niet, daarom niet gebruikt.
3. Scènes met Nano Banana Pro: de echte Poort Padel-foto als `image_references` (evenementenruimte met discobal, baan, Grand Café) plus de Elements in de prompt. De ruimte blijft zoals op de foto, alleen de mensen zijn toegevoegd.
4. Posters met GPT Image 2 op basis van de scènefoto, in elk van de drie stijlen twee varianten.

| Karakter (Element) | Element-id | Higgsfield job |
|---|---|---|
| Sanne, 31, donkerblond, groene padeltop | `7ec95b49-4780-4e87-88f0-8e31b1f44e35` | `4674937e-fda1-4c55-afc0-8da37d0e954e` |
| Daan, 34, bruin haar, baard, zwarte polo | `3283939e-32d6-44cf-8d60-7f8389e76dbf` | `ce5520b2-e967-43dc-b9c4-171819cbe17e` |
| Naomi, 28, krullen in knot, wit cropped shirt | `9a9b417f-38a3-4f3d-a345-58b92b2a6998` | `77fc6b96-11b8-457d-b2fa-47d56bec200c` |
| Emre, 29, zwart haar, lime shirt | `9852a01f-6809-4f0d-9aae-52ecb56b2b7f` | `09c6556e-96dd-4107-8a86-e7ecca71cb0e` |

Dating-foto's (Canva Uploads, naam begint met `Padel Dating foto`):

| Scène | Ruimte | Canva asset | Higgsfield job |
|---|---|---|---|
| Sanne en Daan lachend aan een statafel, racket en drankje | evenementenruimte, discobal | MAHVjSgcvvc | `a26bdfa7-9577-4c73-98e5-f3d1bdd648d3` |
| Naomi en Emre op barkrukken, hij houdt het matchkaartje omhoog | evenementenruimte, discobal | MAHVjSHyOWA | `7d099c71-4ccf-457a-b97b-8fa6c892156c` |
| Sanne en Emre als mixed dubbel juichend aan het net | baan, avondlicht | MAHVjYjUBYA | `640a7e29-eb49-485e-bdb7-cbdcbd75dac8` |
| Naomi en Daan proosten met prosecco aan de bar, bitterballen | Grand Café | MAHVjY7BYQw | `fa1d6e3e-d170-4c62-bd9d-90dee4a1b959` |
| Twee koppels aan twee statafels, groepsbeeld | evenementenruimte, discobal | MAHVjTjLZLE | `33541431-69d5-46e2-9ce6-914a3aef44ca` |
| Naomi en Emre rug aan rug met rackets, filmposter-pose | evenementenruimte, discobal | MAHVjTrhp5g | `9202e2a5-de50-4168-87bf-b9c56b46e73d` |

Posters (Canva Uploads, naam begint met `Padel Dating poster - stijl`):

| Stijl | Variant | Foto | Canva asset | Higgsfield job |
|---|---|---|---|---|
| 1 warm en speels | A: diepgroen, polaroid met koraal tape, doodles | statafel-koppel | MAHVjdV7rfs | `46fb1925-208b-4424-9425-9da313a29c1e` |
| 1 warm en speels | B: crème, twee polaroids, "match!" | mixed dubbel op de baan | MAHVjQBe0rU | `c095aeb6-63e4-473a-8433-38bebd19bf5e` |
| 2 roze hartjes | A: blush naar hot pink, glossy hartjes, fotokaart | rug-aan-rug pose | MAHVjR0AV8M | `92472f55-a3b2-4c71-9c9d-953f43255d28` |
| 2 roze hartjes | B: donker berry voor de avond, foto bovenin | matchkaartje aan tafel | MAHVjUBFhZo | `4593f0f4-b6d4-406a-a313-dec5fda9dfde` |
| 3 donker cinematisch | A: full-bleed foto, crème serif, lime accentlijn | twee koppels onder de discobal | MAHVjbzYLSw | `42368360-1ed4-44cf-9c08-be6983ab2e1e` |
| 3 donker cinematisch | B: full-bleed foto, crème serif, koraal accentlijn | proosten aan de bar | MAHVjfui7Jo | `a5e138e2-d23b-47dc-82e3-753a4c98c7da` |

Tekst op alle zes posters: PADEL DATING, Love at first serve, Speel. Praat. Match., Vrijdag 24 oktober · 19:30 – 22:00, 6 rondes elke ronde een nieuwe partner, 12 min spelen 12 min praten met een drankje, €49,50 p.p. incl. welkomstdrankje & hapjes, Early bird €45, Meld je aan → allcourtacademy.com/events, All Court Academy × Poort Padel · Neonweg 62, Almere. Controleer de spelling voordat je plaatst; GPT Image 2 maakt soms typefouten in Nederlandse tekst (in ronde 3 stond er "All Courrt Academy"). Bij twijfel: de foto zonder tekst in Canva zetten en de tekst zelf typen.

Volgende stap na keuze: dezelfde Elements opnieuw gebruiken voor een Instagram-carrousel (drie foto's: baan, tafel, bar) en een 9:16 story, zodat de karakters herkenbaar blijven in de hele campagne.

### Versie 2 van de groepsfoto (feedback: bier én flessen tegelijk klopt niet)

Lars koos de groepsfoto met de twee koppels onder de discobal als beste, met als kritiek dat er bierglazen op tafel stonden terwijl er met flessen werd geproost. Vier verbeterde versies, elk met precies één drankje per persoon en zonder flessen:

| Variant | Aanpak | Canva asset | Higgsfield job |
|---|---|---|---|
| A gecorrigeerd | dezelfde foto, alleen de drankjes vervangen: links proosten met twee glazen prosecco, rechts één prosecco en één tulpglas bier | MAHVja1YjiA | `fdc00eae-323f-466b-8b01-22b63a801508` |
| B warmer | dezelfde foto, prosecco en roze cocktails, waxinelichtjes, warmer en donkerder licht, lime randlicht | MAHVjd3iSuI | `ac990fc8-aee6-405a-94e8-b63434e9e80d` |
| C nieuw | opnieuw gegenereerd met de Elements, tafels dichter bij de camera, één racket per tafel | MAHVja07wkw | `f60f13ef-4ec4-45b9-b92f-13d1a5a680e4` |
| D close-up | Sanne en Daan proosten op de voorgrond, Naomi en Emre onscherp achter | MAHVjTywgF8 | `40d80c7c-0032-4378-b65e-64c7e94f088e` |

Posters op variant A (Canva Uploads, naam begint met `Padel Dating poster v2`):

| Stijl | Canva asset | Higgsfield job |
|---|---|---|
| 3 donker cinematisch, lime accent | MAHVjUHSc5w | `ad0820f8-6cc1-42fd-837d-9db7165a569d` |
| 1 warm groen, polaroid | MAHVjWxhltQ | `06a8127b-91f5-4bce-8127-ab76407822f0` |
| 2 roze hartjes, donkere avondversie | MAHVjQ3NWdk | `6fa3ffec-4721-45b4-a78b-bbebb3f5221d` |

Tip voor het beeld-prompten: benoem het aantal drankjes per persoon en het soort glas expliciet, anders zet het model zowel flessen als glazen neer.

### Versie 3: minder AI-look (feedback: de karakters zien er te AI uit)

Wat Higgsfield hiervoor heeft: Soul 2.0 is hun eigen realisme-model (bedoeld voor UGC en "unaesthetic" echte mensen), Kling O1 en GPT Image 2.5 renderen huid anders dan Nano Banana, en een prompt met camera-onvolmaaktheden (flitser, ISO-ruis, bewegingsonscherpte, glimmende huid, losse haren, kreukels, scheve framing, geen retouche) haalt de glans eraf. Zeven varianten, allemaal in Canva Uploads onder `Padel Dating foto v3 realistisch`:

| Variant | Model en aanpak | Canva asset | Higgsfield job |
|---|---|---|---|
| Soul 2.0, twee koppels | re-shoot van de gecorrigeerde foto met eventfotograaf-look, flitser, ISO 1600 | MAHVjQTIt2A | `e3fe5c02-3ccb-4d43-a510-0d9bfa985b34` |
| Soul 2.0, koppel close-up | re-shoot van variant D (Sanne en Daan voorgrond) | MAHVjV-uL6o | `4664c741-95c6-41ed-85b7-2974ac8f8b39` |
| GPT Image 2.5 flare, high | documentaire re-render van de gecorrigeerde foto | MAHVjS_6Kqc | `d4a8e12d-f9c6-4f60-8eab-310fb7e729a9` |
| Kling O1 | fotorealistische re-render van de gecorrigeerde foto | MAHVjddaVY8 | `d30bd0d5-6e1a-4561-8290-e8efc0232bea` |
| Nano Banana Pro, flash-look | alleen fotokwaliteit aangepast: poriën, glans, ruis, aberratie, lichte bewegingsonscherpte | MAHVjVNho9I | `f981f06e-c43f-49c8-9f72-2f5cff689b63` |
| Nano Banana Pro, iPhone-snapshot | nieuw met de Elements, iPhone-flitser, scheve framing, ruis in schaduwen | MAHVjU24bvo | `b0b73273-d7b3-423a-b404-b171070e5c21` |
| 4K upscale | gecorrigeerde foto (versie 2A) naar 3311×4096 voor print | MAHVjZNLrnY | `b98ef900-4e6a-4ac0-b96c-5b7402256dce` |

Eerlijke inschatting: AI-mensen blijven op posterformaat herkenbaar voor wie erop let. De echte oplossing is een echte foto. Twee opties die geen extra tooling vragen:

1. De 66 professionele foto's van de ACA-shoot bij Poort Padel (Google Drive, `ACA_PoortPadel_29mei-*.jpg`). Daar staan echte spelers en de echte hal op; een lachend koppel aan het net werkt als posterfoto.
2. Een shoot van 30 minuten in de evenementenruimte met vier leden of vrienden, twee statafels, prosecco en de discobal aan. Dat is de compositie van versie 2A, maar dan echt. Met een telefoon en de zaalverlichting is dit in één avond gedaan en meteen bruikbaar voor Instagram.

De AI-versies blijven bruikbaar als moodboard, als tijdelijke poster tot de shoot en voor stories.

### Versie 4: drukkere achtergrond zonder dubbele personen

Lars koos versie 2A (gecorrigeerde drankjes) als beste, met twee wensen: meer mensen op de achtergrond, en geen dubbele personen (op de achtergrond stond een man die op Daan leek). Drie edits op precies die foto; de vier op de voorgrond blijven onveranderd, de achtergrond is vervangen door andere, onderling verschillende singles. In de prompt staat expliciet: geen zwarte polo, geen lime shirt, geen wit cropped shirt, geen groene tanktop op de achtergrond en geen herhaalde gezichten.

| Variant | Achtergrond | Canva asset | Higgsfield job |
|---|---|---|---|
| A | 8 tot 10 singles in groepjes van twee en drie aan statafels verder weg | MAHVjYKULjw | `9cd85955-b4c9-4951-b042-3d94a95817b7` |
| B | volle zaal: ongeveer 12 singles, host met klembord links, bartafel met prosecco rechts | MAHVjUIWEqA | `73dffc2a-679e-4cd5-a045-f3a0f7d684df` |
| C | 6 singles aan twee tafels plus een host die prosecco inschenkt, iets warmer en donkerder licht | MAHVjWzDxio | `aba1a436-a784-4ec0-8131-9a845fbf09f0` |

Ook toegevoegd: een tweede Soul 2.0-poging (`b4b033f7-76ff-44a1-8c3d-ecaac86ef1a9`, Canva MAHVjdjqJJQ). Let op: Soul 2.0 herschrijft de prompt automatisch en maakte er "model-like features" van, precies wat we niet wilden; het model laat die prompt-verbetering niet uitzetten. Daarom is Nano Banana Pro met een "flitser en ruis"-prompt hier de betere realisme-route.

### Versie 5: gekozen basis, koppels van twee op de achtergrond (definitieve richting)

Lars koos variant A van versie 4, met de wens: meer koppels van twee op de achtergrond, geen groepjes van drie. Twee foto's en daarop de drie posterstijlen.

| Wat | Higgsfield job | Opmerking |
|---|---|---|
| Foto A2: zes koppels van twee op de achtergrond, elk aan een eigen statafel | `a69d69f4-bf96-4cf5-bbd2-4d1d578c4fc1` | gekozen basis voor de posters |
| Foto A3: vijf koppels van twee, direct op versie 2A | `50a258ed-bb63-442a-93fc-d04777c6f94d` | alternatief |
| Foto A2 in 4K (3311×4096) voor print | `e7f4068f-824a-4665-9894-2d10ca8a0c12` | |
| Poster stijl 3 donker cinematisch, lime accent, 2K | `527579fc-b74f-46c6-8af4-5bc75c5cfa6c` | |
| Poster stijl 1 warm groen met polaroid, 2K | `64a75c9c-f653-4c48-86b7-010b2cb98c4e` | |
| Poster stijl 2 roze hartjes, donkere avondversie, 2K | `2faa504e-e57a-4412-ab95-d5439893df5b` | |

Deze versie staat nog niet in Canva: de Canva-koppeling verliep tijdens het uploaden en moet opnieuw geautoriseerd worden in de claude.ai connector-instellingen. Daarna kunnen de zes bestanden hierboven vanuit de Higgsfield-galerij alsnog in Canva Uploads gezet worden.

### Versie 6: de polaroid-poster (stijl 1) met een minder AI-ogende foto

Lars koos de polaroid-poster op foto A2 als beste, met als enige kritiek dat de foto nog te AI oogt. Wat op die foto verraadt dat het AI is: te gladde huid, te gelijkmatig licht zonder flitsschaduw, iedereen perfect geposeerd en lachend, alles even scherp. Zes realisme-passes op precies foto A2, allemaal met behoud van compositie, mensen en ruimte:

| Variant | Model en aanpak | Higgsfield job |
|---|---|---|
| R1 | Seedream 5.0 Pro, inpaint-edit: poriën, glans, flitsschaduw, gemengde witbalans, ISO-ruis, aberratie | `d6bf7b67-d020-4606-a148-71f2d2f6ef1f` |
| R2 | Seedream 4.5, high: Sony A7 IV met flitser-look | `db01737b-c8d8-44fe-a7d5-77f8611a54bd` |
| R3 | Nano Banana Pro, filmlook: Portra 800 pushed, korrel, halatie rond de discobal, harde flitsschaduw, 2 graden scheef | `88bb82bc-a1ee-4933-a11f-84f637cf8113` |
| R4 | Nano Banana Pro, candid-imperfecties: mond half open, ogen half dicht, iemand half gedraaid en onscherp, lager handheld standpunt | `383715df-0c43-49b2-8a1d-6f0cf8b84efc` |
| R5 | GPT Image 2.5 flare, high: Canon R6 met bounce-flitser | `5f091d1e-3074-4f6b-8b5f-a658d3b4ff5b` |
| R6 | Kling O1: fotorealistische re-render | `9b6aed39-328d-48f6-b59f-b39d276474fe` |

Polaroid-posters (stijl 1, 2K) op de twee meest gecontroleerde edits:

| Poster | Foto | Higgsfield job |
|---|---|---|
| Stijl 1 op R3 (filmlook) | `88bb82bc…` | `aad1e917-77a2-4992-b54d-05a1458b812e` |
| Stijl 1 op R4 (candid) | `383715df…` | `82e56ed4-b34b-47ce-9649-d7407e0bf7d9` |

Wat het meest helpt tegen de AI-look, in volgorde: (1) poses en gezichten onperfect maken (R4), (2) flitser met harde schaduw en gemengde witbalans, (3) korrel en lichte onscherpte (R3). Alleen "meer huidtextuur" vragen helpt weinig. De echte foto blijft de beste oplossing; de compositie van A2 is het draaiboek voor een shoot van 30 minuten in de evenementenruimte.

### Versie 7: dezelfde polaroid-poster, maar zonder AI-mensen

Lars' idee: dezelfde tekst en opmaak, maar de foto zonder mensen, of met iets gezelligs of een smash uit zijn eigen Drive. Vijf posters, allemaal stijl 1 (polaroid) met exact dezelfde tekst:

| Variant | Foto in de polaroid | Higgsfield job |
|---|---|---|
| Stilleven eventruimte | echte evenementenruimte met discobal; statafel met twee rackets in een V, twee glazen prosecco, nootjes, waxinelichtje, twee ballen als hartje, matchkaartje; niemand in beeld | `d2480410-1c56-4d32-ad61-9bd8e1622dd6` |
| Lege baan 's avonds | echte baan van Poort Padel, lampen aan, racket en drie ballen bij het net (twee als hartje), lichtsnoer langs het glas | `2b21026f-c21c-40a0-be97-243d33f82ca8` |
| Illustratie smash | vlakke illustratie in koraal, perzik, crème en lime: racket in een smash, bal met een spoor van hartjes, discobal | `38174558-1977-4930-8cf1-cf7b6d2f1d9a` |
| Echte foto: ACA-les op de baan | de echte shootfoto van poortpadel.nl, onbewerkt in de polaroid; echte mensen dus | `8ef974fd-c25c-4f78-a89e-9c11f493b7e9` |
| Echte foto: wintercompetitie | echte Instagram-foto van Poort Padel, onbewerkt in de polaroid | `cade218c-ffa7-43ed-a5ca-eb8c99d6f2b6` |

De 66 shootfoto's op Google Drive (`ACA_PoortPadel_29mei-*.jpg`) zijn vanuit deze omgeving niet in Higgsfield te krijgen: de bestanden zijn privé (alleen eigenaar), de Drive-koppeling kan geen openbare link maken, en de upload-host van Higgsfield is vanuit de bouwomgeving geblokkeerd. Werkwijze die wel werkt: Lars kiest de smash-foto in Drive en uploadt die zelf via het Higgsfield upload-widget (of Canva), waarna de polaroid-poster erop gezet wordt met dezelfde prompt.

### Versie 8: gekozen ontwerp, definitieve tekst (zaterdag, 4 rondes, baruur, geen early bird)

Lars koos de illustratie-poster (smash met hartjes, geen mensen) en gaf de definitieve opzet door: zaterdagavond, 19:30 tot 22:30, vier rondes en daarna het laatste uur samen in de bar, geen early bird, prijs €49,50 blijft. 24 oktober 2026 valt op een zaterdag, dus de datum kon blijven staan.

Tekst op de poster:

> PADEL DATING · Love at first serve
> Speel. Praat. Match.
> Zaterdag 24 oktober · 19:30 – 22:30
> 4 rondes, elke ronde een nieuwe partner
> 12 min spelen, 12 min praten met een drankje
> Daarna: het laatste uur samen in de bar
> €49,50 p.p. incl. welkomstdrankje & hapjes
> Meld je aan → allcourtacademy.com/events
> All Court Academy × Poort Padel · Neonweg 62, Almere

| Bestand | Formaat | Higgsfield job |
|---|---|---|
| Poster, edit van het gekozen ontwerp (alleen tekst gewijzigd) | 2:3, 2K, high | `21ccf058-d812-4264-ace5-c67a03abc0fd` |
| Poster, opnieuw opgebouwd in dezelfde stijl | 2:3, 2K, high | `c348ca9c-faca-491d-a229-844e7c9124a7` |
| Instagram feed | 3:4, 2K | `9df86052-0667-44c4-a8b8-55eca64bef00` |
| Instagram story | 9:16, 2K | `a9c4bcf4-0b0b-4747-818d-c0b7722dafa3` |

Controleer de tekst letter voor letter voordat je print; de edit-versie is meestal het trouwst aan het origineel. Canva staat nog los (koppeling opnieuw autoriseren), daarna kunnen deze vier als Uploads erin en is de tekst daar bewerkbaar.

## Stijlronde 4: donker, warm en professioneel (avondstijl)

Feedback van Lars op ronde 3: warm is goed, maar het moet professioneler en donkerder, want het event is 's avonds. Art direction ronde 4: premium avond-uitnodiging zoals bij een members club of boutique hotel. Echte foto van de avondsfeer bij Poort Padel als achtergrond met een cinematische warme grade (groen-zwarte schaduwen `#0F1F1C`, amber highlights), elegante serif in warm crème `#F5EBDD`, dunne cursieve serif als tagline ("Love at first serve"), kleine schone sans-serif voor details, één accentkleur (lime `#CCFF00` of koraal `#FF6F61`) alleen voor een dunne lijn en het label. Geen stickers, geen cartoonhartjes, veel rust.

Canva, poster (halfoto tijdens avondevent):

| Kandidaat | Link |
|---|---|
| 1 | https://www.canva.com/d/NCcJHd-oXSETji3 |
| 2 | https://www.canva.com/d/JbbcrsoSjnzkba3 |
| 3 | https://www.canva.com/d/HvzFkj_lGGXwxBw |
| 4 | https://www.canva.com/d/jCaLf1kzCzC5piF |

Canva, Instagram-post 4:5 (evenementenruimte met discobal):

| Kandidaat | Link |
|---|---|
| 1 | https://www.canva.com/d/j4s5Y0jgu0w_ZH5 |
| 2 | https://www.canva.com/d/pFGYpQdV31FGHwp |
| 3 | https://www.canva.com/d/vQdzyahmz5XV7uC |
| 4 | https://www.canva.com/d/kx5IqinCrrVxgUy |

Higgsfield-versies (Canva Uploads, naam begint met `Padel Dating avond`): poster op de Instagram-eventfoto (lime-accent), poster op de evenementenruimte (koraal-accent), Instagram-post op het Grand Café.

### Skills en agents die hierbij helpen

| Wat | Waar | Gebruik |
|---|---|---|
| Higgsfield workflow `brand-asset-creation` | Higgsfield-connector, `get_workflow_instructions` | Complete brand-agent: vergrendelt logo, palet en typografie en maakt posters, social graphics en mockups die consistent blijven. Regel uit de workflow: logo en exacte tekst nooit in het AI-beeld bakken, maar er als laag overheen leggen (daarom is de Canva-versie leidend voor tekst). |
| Canva-plugin (`canva-design-feedback`, `canva-implement-feedback`, `canva-edit-design`, `canva-brand-check`, `canva-resize-for-social-media`) | Claude plugin-catalogus | Designfeedback op een gekozen Canva-ontwerp, feedback direct doorvoeren, poster omzetten naar story en Facebook. |
| Design-plugin (`design:design-critique`) | Claude plugin-catalogus | Professionele kritiek op hiërarchie, typografie, kleur en leesbaarheid. |
| Marketing-plugin (`marketing:brand-review`, `marketing:campaign-plan`) | Claude plugin-catalogus | Merkconsistentie en een campagneplan voor de lancering. |

## Stijlronde 3: warm en speels (aanbevolen voor een dating-event)

De eerste twee rondes gebruikten de donkergroene clubstijl. Voor een dating-avond werkt een warmere, speelsere stijl beter. Onderzoek op 18 september 2026: de best scorende speed-dating-templates op Canva ("Pink & Orange Illustrative Speed Dating Night Flyer", "Red and Pink Modern Speed Dating Event", "Pink and Navy Illustrated Speed Dating Event") en echte padel-dating-events (Padel Social Club "Padel Play Dates" Londen, Padel Match, LÕK × Bumble) gebruiken allemaal: crème of lichte achtergrond, koraalrood en perzik, chunky ronde letters, geïllustreerde hartjes en stickers, een echte foto in een ronde of boogvormige lijst, en een korte knipoog als tagline ("Love at first serve", "Match op de baan?").

Toegepaste stijl: crème `#FFF6EC`, koraal `#FF5A5F`, perzik `#FFB4A2`, één lime-accent `#CCFF00` en diepgroen `#143934` voor kleine tekst, zodat het nog steeds bij All Court Academy en Poort Padel past. Hartje van twee padelballen als terugkerend icoon.

Canva, poster (echte foto van de baan in een boogvormige lijst):

| Kandidaat | Link |
|---|---|
| 1 | https://www.canva.com/d/rJfKgcTvJ0TcEPP |
| 2 | https://www.canva.com/d/UpB9Cqy9zpMDQdS |
| 3 | https://www.canva.com/d/cKrcM-d3eBGRLsk |
| 4 | https://www.canva.com/d/EKESobFgUBoOuaE |

Canva, Instagram-post 4:5 (Grand Café-foto in een lijst):

| Kandidaat | Link |
|---|---|
| 1 | https://www.canva.com/d/feQKVY9lyC3m0pG |
| 2 | https://www.canva.com/d/0jSVQxAWAlCwiXe |
| 3 | https://www.canva.com/d/ND-TY2tOuH9qGvQ |
| 4 | https://www.canva.com/d/qIGiE3BJFHSBMZW |

Higgsfield-versies in deze stijl (kant-en-klaar, in Canva Uploads):

| Bestand in Canva Uploads | Opzet |
|---|---|
| Padel Dating warm - creme met boogfoto baan | crème achtergrond, koraal/perzik vormen, echte baanfoto in boogvormige lijst, stickers |
| Padel Dating warm - groen met koraal blobs, polaroid event | diepgroen met koraal blobs, echte eventfoto als polaroid, "Love at first serve" |
| Padel Dating warm - Instagram creme, Grand Cafe | 3:4 Instagram, crème, Grand Café-foto in lijst |
| Padel Dating warm - koraal, foto baan (stijlref Canva template) | gemaakt met de Canva-template "Red and Pink Modern Speed Dating" als stijlreferentie |
| Padel Dating warm - roze en groen, foto event (stijlref Canva template) | gemaakt met de Canva-template "Pink and Navy Illustrated Speed Dating" als stijlreferentie |

Wil je zelf verder in Canva: zoek op "speed dating" in Canva-templates en vervang de foto door een van de Poort Padel-foto's in Uploads. Aanraders: "Pink & Orange Illustrative Speed Dating Night Flyer" (canva.com/templates/EAGdpYTYSFo), "Red and Pink Modern Speed Dating Event" (EAGw3wQzL_c), "Pink and Navy Illustrated Speed Dating Event" (EAGw31ctZNE).

## Canva (bewerkbaar: datum, prijs, link aanpassen)

Alles staat in het Canva-account dat op 18 september 2026 opnieuw is gekoppeld (eerdere links uit een verkeerd account zijn verwijderd). Open een kandidaat, kies "Bewerken" en pas de datum aan zodra die vaststaat.

Poster A3/A4 op echte foto's (baan als achtergrond, Grand Café als inzet):

| Kandidaat | Link |
|---|---|
| 1 | https://www.canva.com/d/qJQWHpwwdkxXBn2 |
| 2 | https://www.canva.com/d/77ImA7ECxpaNT3v |
| 3 | https://www.canva.com/d/L23R3Uxy5XcTRXH |
| 4 | https://www.canva.com/d/GaU6Np1Gk3kBTo5 |

Instagram-post 4:5 op de foto van de evenementenruimte:

| Kandidaat | Link |
|---|---|
| 1 | https://www.canva.com/d/_8rjid_MPulCHHm |
| 2 | https://www.canva.com/d/4TTr4fJ5FwUW6iq |
| 3 | https://www.canva.com/d/9OhWhjOSmegpXvF |
| 4 | https://www.canva.com/d/mPUSR34KUnZzCYw |

Canva Uploads in dit account: `All Court Academy logo` (MAHVjfwlfJI); echte foto's `Poort Padel foto - ACA les op de baan` (MAHVjd7xUSc), `Poort Padel foto - Grand Cafe met zicht op banen` (MAHVjdo7nRc), `Poort Padel foto - hal` (MAHVjSDNHGU), `Poort Padel foto - evenementenruimte discobal` (MAHVjYYe3pQ); kant-en-klare posters `Padel Dating poster - echte foto baan (ACA les)` (MAHVjb6vMvA), `- echte foto hal` (MAHVjSTs17g), `- echte foto Grand Cafe` (MAHVja0ojcs), `Padel Dating Instagram 4x5 - echte foto evenementenruimte` (MAHVjaseTz8), `- Instagram Almere Zaken event` (MAHVjXh8aAc), `- Instagram Grand Cafe` (MAHVjapcx3E); AI-versies `Padel Dating poster AI v1` (MAHVjVnMA_k) en `Padel Dating hero 1 (AI sfeerfoto)` (MAHVjRVcO0s).

## Higgsfield (kant-en-klare beelden)

Versies op echte foto's (18 september 2026, tweede ronde). De foto blijft onbewerkt, alleen een donkergroene gradient en de tekst zijn toegevoegd.

| Bestand in Canva Uploads | Achtergrondfoto | Bron |
|---|---|---|
| Padel Dating poster - echte foto baan (ACA les) | spelers op de baan, ACA-fotoshoot 29 mei | poortpadel.nl |
| Padel Dating poster - echte foto hal | de hal tijdens een event | poortpadel.nl |
| Padel Dating poster - echte foto Grand Cafe | Grand Café met zicht op de banen | poortpadel.nl |
| Padel Dating Instagram 4x5 - echte foto evenementenruimte | evenementenruimte met discobal | poortpadel.nl |
| Padel Dating poster - Instagram Almere Zaken event | release Almere Zaken in de hal | instagram.com/poortpadel |
| Padel Dating poster - Instagram Grand Cafe | gerechten in het Grand Café | instagram.com/poortpadel |

Eerste ronde (volledig AI, ter vergelijking):

| Bestand | Model | Inhoud |
|---|---|---|
| Padel Dating poster AI v1 | GPT Image 2, 1360×2048 | Complete poster met alle tekst |
| Padel Dating poster AI v2 | GPT Image 2, 1360×2048 | Complete poster, tweede variant |
| Padel Dating hero 1 | Soul 2.0, 1536×2048 | Sfeerfoto zonder tekst (koppel op de baan) |
| Padel Dating hero 2 | Soul 2.0, 1536×2048 | Sfeerfoto zonder tekst, tweede variant |

Controleer bij de AI-posters de spelling van de Nederlandse tekst voordat je ze plaatst; beeldmodellen maken daar soms fouten in. De Canva-versie is leidend voor tekst.

## Stijlregels (uit allcourtacademy.com en poortpadel.nl)

- Achtergrond diepgroen `#143934`, accent lime `#CCFF00`, tekst wit of off-white `#F2F2EE`.
- Kop in serif (Fraunces), details in Poppins of Inter Tight.
- Call-to-action als lime pill-knop met donkere tekst.
- Onderaan beide logo's: All Court Academy × Poort Padel.

## Meer echte foto's

- Google Drive van Lars: `ACA_PoortPadel_29mei-*.jpg` (66 professionele foto's van de shoot bij Poort Padel, juni 2026). Upload er een paar naar Canva en vervang de achtergrond; dit is de beste bron.
- Instagram @poortpadel: bekijk posts, reels en stories zonder login via imginn.com/poortpadel/ (Instagram zelf blokkeert scrapers). Reels laten de sfeer van de hal, het Grand Café en events zien: imginn.com/reels/poortpadel/.
- Zie `research/scrapers-social-media.md` voor tools die dit automatisch binnenhalen.

### Versie 9: definitieve datum 7 november, start 19:00, leeftijdsgroep

Lars koos op 20 september 2026 zaterdag 7 november 2026 (onderbouwing in `events/padel-dating-datum.md`) en vroeg om een leeftijdsadvies (`events/padel-dating-leeftijd.md`, advies: singles van 25 t/m 40 jaar). De poster is opnieuw bewerkt vanuit versie 8 (`21ccf058…`), alleen de tekstregels zijn gewijzigd.

Tekst op de poster (variant met leeftijd):

> PADEL DATING · Love at first serve
> Speel. Praat. Match.
> Zaterdag 7 november · 19:00 – 22:00
> Singles van 25 t/m 40 jaar
> 4 rondes, elke ronde een nieuwe partner
> 12 min spelen, 12 min praten met een drankje
> Daarna: het laatste uur samen in de bar
> €49,50 p.p. incl. welkomstdrankje & hapjes
> Meld je aan → allcourtacademy.com/events
> All Court Academy × Poort Padel · Neonweg 62, Almere

| Bestand | Formaat | Higgsfield job |
|---|---|---|
| Poster met leeftijdsregel "Singles van 25 t/m 40 jaar" | 2:3, 2K, high | `6b9674b3-6ede-4db4-9756-d243c7ffe07c` |
| Poster zonder leeftijdsregel (alleen datum gewijzigd) | 2:3, 2K, high | `a6883a8e-7bb5-4918-a499-e6650f14e1bf` |
| Instagram feed (3:4, met leeftijd) | 3:4, 2K | `f2b74b1b-7599-4179-b755-f177f8591377` |
| Instagram story (9:16, met leeftijd, link in bio) | 9:16, 2K | `f1f50087-2f38-4a33-b30f-31f2d4ab3059` |

Controleer de spelling van de datum en de leeftijdsregel voordat je plaatst. Versie 8 (24 oktober) niet meer gebruiken.
