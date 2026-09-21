# Event- en clinicaanbod All Court Academy bij Poort Padel

Doel: het event- en zalenaanbod van Poort Padel (Almere) in kaart brengen, daar een eigen prijslijst van All Court Academy met 20% winstmarge op bouwen, en bedrijven en scholen in Almere per e-mail benaderen.

| Map | Inhoud |
|---|---|
| `research/poort-padel-aanbod.md` | Volledig overzicht van Poort Padel: 13 banen, 6 vergaderzalen, 2 skyboxen, congreszaal, evenementenruimte, eventvormen, baanprijzen (Playtomic), horecakaart en wat alleen op aanvraag is. Met bronnen. |
| `pricing/prijscalculator.xlsx` | Werkboek met alle inkoopprijzen als inputs en formules voor verkoopprijs = kostprijs × (1 + marge). Tabbladen: Inputs, Arrangementen, Add-ons, Scholen, Offerte, Legenda. |
| `pricing/build_prijscalculator.py` | Script dat het werkboek genereert. Aanpassen en opnieuw draaien als je het model wilt uitbreiden. |
| `pricing/aca-event-prijslijst.md` | Leesbare prijslijst voor bedrijven en scholen, inclusief kostprijsonderbouwing. |
| `email/template-bedrijven.md` | Eerste mail aan bedrijven (mail-merge template). |
| `email/template-scholen.md` | Eerste mail aan scholen. |
| `email/followup.md` | Opvolgmail na een week. |
| `outreach/leads.csv` | Leadlijst met 415 leads: 77 scholen (alle schoolbesturen in Almere) en 338 bedrijven (leden Vereniging Bedrijfskring Almere), verzameld 14 september 2026. |
| `outreach/send_campaign.py` | Mail-merge script via Gmail SMTP. Dry-run standaard, logt verzonden adressen, respecteert opt-outs. |
| `outreach/README.md` | Hoe je de leadlijst bouwt (GitHub-scrapers), verstuurt en binnen de spamregels blijft. |

## Snel starten

```bash
pip install openpyxl
python3 pricing/build_prijscalculator.py      # werkboek (opnieuw) genereren
python3 outreach/send_campaign.py             # dry-run van de mailing
```

## Belangrijkste aannames

- Baanhuur is geverifieerd op Playtomic: daluren €30, piek €44, weekend €37,50 per uur (dubbelbaan).
- Zaalhuur is uitgelezen uit de reserveringswizard van Poort Padel (kantoor €225, skybox €250, congreszaal €550, evenementenruimte €450 per dagdeel, excl. btw). Event- en cateringarrangementen zijn bij Poort Padel alleen op offerte; het coachtarief en de horeca-arrangementen staan daarom als gele aannames in de calculator.
- Alle prijzen excl. btw. Minimum 16 personen per zakelijk event (eis Poort Padel).

## Agent Reach skill

`.claude/skills/agent-reach/` en `tools/agent-reach/` zijn overgenomen uit `ldebruinlars/animation-padel` (21 september 2026). De skill werkt op je eigen computer met Claude Code in VS Code, na `bash tools/agent-reach/install-mac.sh` of het Windows-script. In de cloudsessie van Claude Code (deze omgeving) staat het netwerk de backends niet toe (Exa, Jina, YouTube, Reddit, Instagram zijn geblokkeerd), dus daar doet de skill niets; onderzoek loopt daar via de ingebouwde zoek- en browsertools.
