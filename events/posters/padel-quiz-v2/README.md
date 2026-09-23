# Padel & Quiz, poster versie 2 (krijtbord met programma)

Gemaakt op 23 september 2026. Eerst een versie in Poort Padel-stijl (lime balken, P-patroon, tagline); Lars wilde de inhoud houden maar geen lime en alles in krijtstijl. Nu: wit krijt en het geel van de illustratie, getekende kaders om de tijden, gele prijsbanner, beide logo's onderin, geen "Meld je aan"-knop meer (alleen de site als krijtregel). Het programma met tijden staat op de poster.

| Bestand (in `../final/`) | Wat |
|---|---|
| `padel-quiz-v2-poster.jpg` | printposter 3:4, 3488 × 4672 (295 dpi op 30 × 40 cm) |
| `padel-quiz-v2-poster-30x40cm.pdf` | dezelfde als pdf |
| `padel-quiz-v2-ig-feed-4x5.jpg` | Instagram feed 2160 × 2700, bord op hoogte gepast met donkere wand links en rechts |
| `padel-quiz-v2-ig-story-9x16.jpg` | Instagram story 2160 × 3840 |

## Tekst op de poster

Zaterdag 16 januari (datumvoorstel, alternatieven 12 december 2026 en 23 januari 2027) · 18:00 – 22:00 · inloop 17:30. Programma: 17:30 inloop, welkomstdrankje en teamindeling; 18:00 Mexicano padel, 6 rondes, elke ronde een andere partner; 19:45 pubquiz in teams van 4, 6 rondes met jackpotvraag; 21:15 prijsuitreiking, €500 aan prijzen van Poort Padel. Chips: alleen of met je team; alle niveaus, rackets liggen klaar. €39,50 p.p. incl. welkomstdrankje & hapjes. allcourtacademy.com/events. Logo's All Court Academy × Poort Padel, adres Neonweg 62, Almere.

## Hoe het gebouwd is

1. `build_board.py` maakt `build/board.jpg`: de krijtbord-illustratie (variant 1 uit `../assets/artwork/`) verkleind naar 80% bovenin, met het lege bord doorgetrokken naar beneden zodat er ruimte is voor het programma. (Het script maakt ook nog een P-patroontegel; die wordt niet meer gebruikt.)
2. `poster.html` is de opmaak op 1744 × 2336 (de maat van het bord). Tekst staat in de blokken met `TEKST`, maten bovenin bij `:root`.
3. `render.sh` rendert op 2× met Chromium headless, legt daarna in Python het krijteffect over alles wat van het kale bord afwijkt (ruis in de dekking, de logostrook blijft strak) en schrijft poster, pdf, feed en story naar `../final/`.

Aanpassen: tekst of datum in `poster.html` wijzigen en `./render.sh` draaien. Andere krijtbord-variant: het pad bovenin `build_board.py` aanpassen en beide scripts draaien.

De eerdere versie (`../final/padel-quiz-poster.jpg` en varianten, gele krijttekst zonder Poort Padel-elementen) blijft staan.
