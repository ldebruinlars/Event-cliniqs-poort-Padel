# Scrapers voor websites, Instagram en Facebook (GitHub, gevonden 18 september 2026)

Vraag: één tool die websites, Instagram, Facebook en meer kan uitlezen. Er is niet één repo die alles doet; dit zijn de beste per doel, gesorteerd op sterren.

| Repo | Sterren | Wat het doet | Wanneer gebruiken |
|---|---|---|---|
| [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | 83.800 | Open-source webcrawler die pagina's omzet naar schone markdown voor AI. Ook als MCP-server (coleam00/mcp-crawl4ai-rag). | Websites van bedrijven, scholen en Poort Padel uitlezen. Instagram/Facebook niet (login-muur). |
| [mikf/gallery-dl](https://github.com/mikf/gallery-dl) | 19.700 | Commandline-downloader voor foto's en video's van 300+ sites, waaronder Instagram, Twitter/X, TikTok, Pinterest, Flickr. Facebook beperkt. | Alle foto's en reels van @poortpadel in één keer binnenhalen: `gallery-dl https://www.instagram.com/poortpadel/` (met eigen cookies-bestand). |
| [instaloader/instaloader](https://github.com/instaloader/instaloader) | 13.400 | Python-tool voor Instagram: posts, stories, reels, captions, metadata, profielen. | Instagram specifiek, inclusief bijschriften en hashtags: `instaloader --login jouwaccount poortpadel`. |
| [harismuneer/Ultimate-Social-Scrapers](https://github.com/harismuneer/Ultimate-Social-Scrapers) | 3.200 | Verzameling scrapers voor Facebook, Instagram en Twitter/X: posts, likes, reacties, foto's, volgers, contactgegevens, events. | Facebook-pagina's van bedrijven en events uitlezen. |
| [postaddictme/instagram-php-scraper](https://github.com/postaddictme/instagram-php-scraper) | 3.300 | PHP-library voor Instagram-accounts, foto's, stories, comments. | Alleen als je in PHP werkt. |
| yt-dlp (github.com/yt-dlp/yt-dlp) | 100.000+ | Video's van YouTube, Instagram reels, TikTok, Facebook en 1.000+ sites. | Reels en video's van Poort Padel downloaden. |

Combinatie die alles dekt: **crawl4ai** (websites) + **gallery-dl of instaloader** (Instagram) + **yt-dlp** (video) + **Ultimate-Social-Scrapers** (Facebook). Alle vier draaien lokaal met Python; Instagram vereist inloggen met je eigen account en respecteert rate limits (ongeveer 100 posts per uur).

## Zonder installatie

- **imginn.com/poortpadel/** toont de openbare Instagram-posts, stories en reels van @poortpadel zonder login, met downloadknoppen. Dit is gebruikt om de echte foto's van Poort Padel in de posters te verwerken.
- Firecrawl (via de ChatCut-connector) leest websites, maar Instagram en Facebook worden geweigerd.
- Metricool (verbonden voor All Court Academy) kan Instagram-concurrenten volgen; @poortpadel toevoegen als "competitor" geeft hun posts en statistieken in het dashboard.

## Foto's van Poort Padel die al beschikbaar zijn

- Google Drive van Lars: map met de professionele fotoshoot `ACA_PoortPadel_29mei-*.jpg` (66 foto's, juni 2026). Dit is de beste bron voor posters; de website van Poort Padel gebruikt dezelfde serie.
- poortpadel.nl: Grand Café, evenementenruimte met discobal, hal, banen (1600 px, zie `events/posters/README.md`).
- Instagram @poortpadel (via imginn): Almere Zaken-release in de hal, Grand Café-gerechten, kleedkamers, wintercompetitie, Kids Camp van All Court Academy.
