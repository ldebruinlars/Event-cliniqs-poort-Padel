"""Bouwt events/padel-quiz-scorebord.xlsx: Mexicano-ranglijst, quiz-scorebord, vouchers, regels.
Draaien vanuit de repo-root: python3 events/build_padel_quiz_scorebord.py"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import CellIsRule
from openpyxl.utils import get_column_letter

OUT = "events/padel-quiz-scorebord.xlsx"
FONT = "Calibri"
BOLD = Font(name=FONT, bold=True)
H1 = Font(name=FONT, bold=True, size=14)
BLUE = Font(name=FONT, color="0000FF")
NOTE = Font(name=FONT, italic=True, color="666666")
GREY = PatternFill("solid", fgColor="EDEDED")
YEL = PatternFill("solid", fgColor="FFF2CC")
GREEN = PatternFill("solid", fgColor="D9EAD3")
thin = Side(style="thin", color="BBBBBB")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
CENTER = Alignment(horizontal="center")

wb = Workbook()

# ------------------------------------------------------------------ Mexicano
ws = wb.active
ws.title = "Mexicano"
ws["A1"] = "Padel & Quiz – Mexicano-ranglijst (rallypunten per ronde, individueel)"; ws["A1"].font = H1
ws["A2"] = "Blauw = invullen. Vul per speler de rallypunten van ronde 1 t/m 6 in (of laat de app het doen en neem het totaal over). Rang, dames- en herenrang en de prijzen rekenen zichzelf uit."; ws["A2"].font = NOTE
heads = ["Nr", "Naam", "M/V", "Team (inschrijving)", "R1", "R2", "R3", "R4", "R5", "R6", "Totaal", "Laatste ronde", "Rang", "Rang M/V", "Prijs"]
for c, h in enumerate(heads, 1):
    cell = ws.cell(row=4, column=c, value=h); cell.font = BOLD; cell.fill = GREY; cell.border = BOX; cell.alignment = CENTER
N = 40
first, last = 5, 4 + N
for i in range(N):
    r = first + i
    ws.cell(row=r, column=1, value=i + 1).border = BOX
    for c in (2, 3, 4):
        cell = ws.cell(row=r, column=c); cell.font = BLUE; cell.border = BOX
    for c in range(5, 11):
        cell = ws.cell(row=r, column=c); cell.font = BLUE; cell.border = BOX; cell.fill = YEL
    ws.cell(row=r, column=11, value=f'=IF(B{r}="","",SUM(E{r}:J{r}))').border = BOX
    ws.cell(row=r, column=12, value=f'=IF(B{r}="","",J{r})').border = BOX
    # rang: totaal, dan laatste ronde als tiebreak (via 1/1000 opslag)
    ws.cell(row=r, column=13, value=f'=IF(B{r}="","",1+COUNTIFS($B${first}:$B${last},"<>",$K${first}:$K${last},">"&K{r})+COUNTIFS($B${first}:$B${last},"<>",$K${first}:$K${last},K{r},$L${first}:$L${last},">"&L{r}))').border = BOX
    ws.cell(row=r, column=14, value=f'=IF(B{r}="","",1+COUNTIFS($C${first}:$C${last},C{r},$K${first}:$K${last},">"&K{r})+COUNTIFS($C${first}:$C${last},C{r},$K${first}:$K${last},K{r},$L${first}:$L${last},">"&L{r}))').border = BOX
    ws.cell(row=r, column=15, value=(
        f'=IF(B{r}="","",IF(AND(N{r}=1,C{r}="V"),"Padelkoningin",IF(AND(N{r}=1,C{r}="M"),"Padelkoning",'
        f'IF(M{r}-COUNTIFS($N${first}:$N${last},1,$M${first}:$M${last},"<"&M{r})<=2,"Nummer "&(M{r}-COUNTIFS($N${first}:$N${last},1,$M${first}:$M${last},"<"&M{r})+1)&" padel",""))))'
    )).border = BOX
ws.conditional_formatting.add(f"O{first}:O{last}", CellIsRule(operator="notEqual", formula=['""'], fill=GREEN))
r = last + 2
ws.cell(row=r, column=1, value="Regels").font = BOLD
for t in [
    "Rallypunten: elke gewonnen rally is 1 punt voor beide spelers van het koppel. 13 minuten of 24 punten per ronde.",
    "Rang: totaal punten; gelijk = meeste punten in de laatste ronde (kolom L); nog gelijk = één beslissende rally, pas dan handmatig aan.",
    "Padelkoning/-koningin = rang 1 bij M en bij V. Nummer 2 en 3 padel = de eerstvolgende twee van de totale lijst zonder de koning en koningin (kolom O rekent dit uit).",
    "Sportiviteitsprijs: kies zelf, noteer hieronder.",
]:
    r += 1; ws.cell(row=r, column=1, value=t).font = NOTE
r += 2; ws.cell(row=r, column=1, value="Sportiviteitsprijs:").font = BOLD; ws.cell(row=r, column=2).font = BLUE; ws.cell(row=r, column=2).fill = YEL
widths = [5, 22, 5, 20, 6, 6, 6, 6, 6, 6, 8, 12, 6, 9, 18]
for c, w in enumerate(widths, 1):
    ws.column_dimensions[get_column_letter(c)].width = w
ws.freeze_panes = "C5"

# ---------------------------------------------------------------------- Quiz
wq = wb.create_sheet("Quiz")
wq["A1"] = "Padel & Quiz – scorebord quiz (6 rondes, joker, wipeout, jackpot, tiebreak)"; wq["A1"].font = H1
wq["A2"] = "Blauw = invullen. Joker = rondenummer 1 t/m 5 (die ronde telt dubbel). R6 = wipeout: vul het aantal goede antwoorden in, en 'Fout in R6' = 1 als er minstens één fout antwoord bij zat (dan telt R6 als 0). 8 goed zonder fout = 8 + 4 bonus."; wq["A2"].font = NOTE
qh = ["Tafel", "Teamnaam", "Joker (1-5)", "R1", "R2 beeld", "R3 muziek", "R4", "R5 (max 10)", "R6 goed", "Fout in R6", "R6 score", "Totaal", "Tiebreak schatting", "Afstand tot antwoord", "Jackpot goed (1/0)", "Rang", "Prijs", "Volgorde inleveren R2", "Volgorde inleveren R3"]
for c, h in enumerate(qh, 1):
    cell = wq.cell(row=4, column=c, value=h); cell.font = BOLD; cell.fill = GREY; cell.border = BOX; cell.alignment = Alignment(horizontal="center", wrap_text=True)
wq.row_dimensions[4].height = 32
T = 12
qf, ql = 5, 4 + T
wq["U3"] = "Tiebreak-antwoord:"; wq["U3"].font = BOLD; wq["V3"] = 343121; wq["V3"].font = BLUE; wq["V3"].fill = YEL
wq["U4"] = "Jackpot-uren nu:"; wq["U4"].font = BOLD; wq["V4"] = 2; wq["V4"].font = BLUE; wq["V4"].fill = YEL
for i in range(T):
    r = qf + i
    wq.cell(row=r, column=1, value=i + 1).border = BOX
    for c in [2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 18, 19]:
        cell = wq.cell(row=r, column=c); cell.font = BLUE; cell.border = BOX; cell.fill = YEL if c in (4, 5, 6, 7, 8, 9, 10) else PatternFill()
    wq.cell(row=r, column=11, value=f'=IF(B{r}="","",IF(J{r}=1,0,IF(I{r}=8,12,I{r})))').border = BOX
    wq.cell(row=r, column=12, value=(
        f'=IF(B{r}="","",SUM(D{r}:H{r})+K{r}+IF(C{r}=1,D{r},IF(C{r}=2,E{r},IF(C{r}=3,F{r},IF(C{r}=4,G{r},IF(C{r}=5,H{r},0))))))'
    )).border = BOX
    wq.cell(row=r, column=14, value=f'=IF(M{r}="","",ABS(M{r}-$V$3))').border = BOX
    wq.cell(row=r, column=16, value=f'=IF(B{r}="","",1+COUNTIFS($B${qf}:$B${ql},"<>",$L${qf}:$L${ql},">"&L{r})+COUNTIFS($B${qf}:$B${ql},"<>",$L${qf}:$L${ql},L{r},$N${qf}:$N${ql},"<"&N{r}))').border = BOX
    wq.cell(row=r, column=17, value=(
        f'=IF(B{r}="","",IF(P{r}=1,"Kampioenen",IF(P{r}=2,"Nummer 2",IF(P{r}=3,"Nummer 3",IF(P{r}=COUNTIF($B${qf}:$B${ql},"<>"),"Poedelprijs","")))))'
        f'&IF(AND(B{r}<>"",K{r}=12)," + wipeout-bonus","")'
        f'&IF(AND(B{r}<>"",O{r}=1,COUNTIF($O${qf}:$O${ql},1)=1)," + JACKPOT","")'
        f'&IF(AND(B{r}<>"",O{r}=1,COUNTIF($O${qf}:$O${ql},1)>1,W{r}=MIN($W${qf}:$W${ql}))," + JACKPOT (tiebreak)","")'
    )).border = BOX
    # helper columns (W: afstand als jackpot goed, X/Y: sleutel score en inlevervolgorde voor de rondeprijzen)
    wq.cell(row=r, column=23, value=f'=IF(AND(B{r}<>"",O{r}=1,N{r}<>""),N{r},999999999)').font = NOTE
    wq.cell(row=r, column=24, value=f'=IF(AND(B{r}<>"",E{r}<>""),E{r}*1000-IF(R{r}="",999,R{r}),-1)').font = NOTE
    wq.cell(row=r, column=25, value=f'=IF(AND(B{r}<>"",F{r}<>""),F{r}*1000-IF(S{r}="",999,S{r}),-1)').font = NOTE
wq.conditional_formatting.add(f"Q{qf}:Q{ql}", CellIsRule(operator="notEqual", formula=['""'], fill=GREEN))
r = ql + 2
wq.cell(row=r, column=1, value="Rondeprijzen").font = BOLD
r += 1
wq.cell(row=r, column=1, value="Beeldronde (R2): hoogste score, gelijk = eerst ingeleverd")
wq.cell(row=r, column=8, value=f'=IF(COUNT(E{qf}:E{ql})=0,"",INDEX(B{qf}:B{ql},MATCH(MAX(X{qf}:X{ql}),X{qf}:X{ql},0)))').font = BOLD
r += 1
wq.cell(row=r, column=1, value="Muziekronde (R3): hoogste score, gelijk = eerst ingeleverd")
wq.cell(row=r, column=8, value=f'=IF(COUNT(F{qf}:F{ql})=0,"",INDEX(B{qf}:B{ql},MATCH(MAX(Y{qf}:Y{ql}),Y{qf}:Y{ql},0)))').font = BOLD
r += 1
wq.cell(row=r, column=1, value="Jackpot: als geen enkel team 1 heeft bij 'Jackpot goed', rollover: volgende editie +1 uur (cel V4 aanpassen).").font = NOTE
r += 1
wq.cell(row=r, column=1, value="Snelste tafel en beste teamnaam worden live bepaald (briefjes, applaus) en hier alleen genoteerd:").font = NOTE
r += 1; wq.cell(row=r, column=1, value="Snelste tafel:").font = BOLD; wq.cell(row=r, column=3).font = BLUE; wq.cell(row=r, column=3).fill = YEL
r += 1; wq.cell(row=r, column=1, value="Beste teamnaam:").font = BOLD; wq.cell(row=r, column=3).font = BLUE; wq.cell(row=r, column=3).fill = YEL
qw = [6, 24, 8, 6, 8, 9, 6, 9, 8, 8, 8, 8, 12, 12, 10, 6, 30, 10, 10, 3, 18, 10, 9, 9, 9]
for c, h in ((23, "hulp jackpot"), (24, "hulp R2"), (25, "hulp R3")):
    wq.cell(row=4, column=c, value=h).font = NOTE
for c, w in enumerate(qw, 1):
    wq.column_dimensions[get_column_letter(c)].width = w
wq.freeze_panes = "C5"

# ------------------------------------------------------------------ Vouchers
wv = wb.create_sheet("Vouchers")
wv["A1"] = "Vouchers en prijzen – uitgifte en inwisseling (lijst voor de bar van Poort Padel)"; wv["A1"].font = H1
vh = ["Nr", "Prijs", "Wat", "Winnaar (naam)", "Team", "Uitgegeven op", "Geldig tot", "Ingewisseld op", "Paraaf bar"]
for c, h in enumerate(vh, 1):
    cell = wv.cell(row=3, column=c, value=h); cell.font = BOLD; cell.fill = GREY; cell.border = BOX
prijzen = [
    ("Quizkampioenen", "Baanuur 1 van 2 (team)"), ("Quizkampioenen", "Baanuur 2 van 2 (team)"), ("Quizkampioenen", "Teamschotel 25 st"), ("Quizkampioenen", "Rondje van 4"),
    ("Nummer 2 quiz", "Baanuur (team)"), ("Nummer 2 quiz", "Rondje van 4"),
    ("Nummer 3 quiz", "Rondje van 4"), ("Nummer 3 quiz", "Bitterballen 8 st"),
    ("Padelkoning", "Baanuur"), ("Padelkoning", "Blik ballen"), ("Padelkoningin", "Baanuur"), ("Padelkoningin", "Blik ballen"),
    ("Nummer 2 padel", "Blik ballen + set grips"), ("Nummer 3 padel", "Blik ballen + set grips"),
    ("Rondewinnaar beeld", "Rondje van 4"), ("Rondewinnaar muziek", "Rondje van 4"), ("Snelste tafel", "Rondje van 4"),
    ("Wipeout-bonus", "Bitterballen 8 st per team"), ("Jackpot", "2 uur baan (team)"), ("Beste teamnaam", "4 koffie/thee/fris"),
    ("Poedelprijs", "Pollepel, drop, water, losse les ACA"), ("Sportiviteit", "1 drankje"),
]
for i, (p, w) in enumerate(prijzen, 1):
    r = 3 + i
    wv.cell(row=r, column=1, value=i).border = BOX
    wv.cell(row=r, column=2, value=p).border = BOX
    wv.cell(row=r, column=3, value=w).border = BOX
    for c in (4, 5, 6, 8, 9):
        cell = wv.cell(row=r, column=c); cell.font = BLUE; cell.border = BOX
    wv.cell(row=r, column=7, value=f'=IF(F{r}="","",EDATE(F{r},3))').border = BOX
    wv.cell(row=r, column=7).number_format = "DD-MM-YYYY"
    wv.cell(row=r, column=6).number_format = "DD-MM-YYYY"
wv.cell(row=3 + len(prijzen) + 2, column=1, value="Voorwaarden baanvoucher: 1 uur dubbelbaan voor 4 spelers, boeken via de bar, geldig ma t/m vr 07:00–17:00 of za/zo na 14:00, 3 maanden geldig, niet inwisselbaar voor geld, één voucher per boeking.").font = NOTE
for c, w in enumerate([5, 20, 32, 22, 18, 14, 12, 14, 10], 1):
    wv.column_dimensions[get_column_letter(c)].width = w

# ------------------------------------------------------------------- Regels
wr = wb.create_sheet("Regels kort")
regels = [
    "Teams van 4, maximaal 5. Teamnaam op de teamkaart.",
    "6 rondes van 8 vragen. 1 punt per goed antwoord, halve punten alleen bij muziek.",
    "Joker: één ronde uit 1 t/m 5 telt dubbel. Vooraf inleveren. Niet op de wipeout.",
    "Ronde 6 wipeout: openlaten mag, één fout is nul, 8 goed is 8 + 4 bonus.",
    "Vellen ophalen vóór de antwoorden. Buurtafel kijkt na, Lars telt.",
    "Telefoons op tafel, scherm naar beneden. Opzoeken is die ronde nul.",
    "Snelste tafel na de pauze: briefje, eerste goede wint, fout is af.",
    "Jackpot na ronde 6: goed wint, meerdere goed = tiebreak, niemand = rollover.",
    "Gelijke stand: schattingsvraag beslist, nooit loting.",
    "De quizmaster heeft altijd gelijk.",
    "Mexicano: rallypunten, individueel, 13 min of 24 punten, blokken van 4 op stand vanaf ronde 2.",
]
wr["A1"] = "Regels in het kort"; wr["A1"].font = H1
for i, t in enumerate(regels, 1):
    wr.cell(row=2 + i, column=1, value=f"{i}. {t}")
wr.column_dimensions["A"].width = 110

wb.save(OUT)
print("saved", OUT)
