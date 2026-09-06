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
| `outreach/leads.csv` | Leadlijst (kolommen vastgelegd, met voorbeeldregels). Hier komen de bedrijven en scholen in. |
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
- Poort Padel publiceert geen prijzen voor events, zalen of arrangementen. Zaalhuur en coachtarief staan als gele aannames in de calculator en moeten bevestigd worden.
- Alle prijzen excl. btw. Minimum 16 personen per zakelijk event (eis Poort Padel).
