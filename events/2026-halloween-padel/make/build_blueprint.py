"""Bouwt de volledige Make-blauwdruk van scenario 8011858 "halloween betaald naar sheet en Moneybird".

Make's scenarios_update vervangt altijd het hele scenario, dus wijzig hier en stuur blueprint.json in z'n geheel mee.
De bevestigingsmail komt uit events/2026-halloween-padel/mail/bevestigingsmail-make.html (eerst build_mail.py draaien).
Gebruik: python3 build_blueprint.py  ->  blueprint.json naast dit script.
"""
import json, re
from pathlib import Path
HIER = Path(__file__).parent
html = re.sub(r'\n\s*', '', (HIER / '../mail/bevestigingsmail-make.html').read_text())
assert 'ref.' not in html
SHEET = "1JDcYpc3hiMmV3yYleYBBustmHQm1-N7fkt4-fqkBr_w"
DS = 222335
def conn(c, label, cid):
    return {"__IMTCONN__": {"data": {"scoped": "true", "connection": c}, "label": label}}, {"__IMTCONN__": cid}
MB_R, MB_P = conn("moneybird", "Moneybird All Court Academy", 7012271)
GS_R, GS_P = conn("google", "Lessenreeks connection (l.debruin@allcourtacademy.com)", 6966521)
def d(x, y): return {"x": x, "y": y}
def ds_meta(x, y): return {"restore": {"parameters": {"datastore": {"label": "halloween terugbetaald"}}}, "designer": d(x, y)}
INV_EXPECT = {"currency": {"mode": "chose", "label": "EUR - Euro"}, "contactId": {"mode": "edit"}, "workflowId": {"mode": "chose", "label": "Kidscamp"}, "pricesAreInclTax": {"mode": "chose"}, "detailsAttributes": {"mode": "chose", "items": [{"tax_rate_id": {"mode": "chose", "label": "9% btw"}, "ledger_account_id": {"mode": "chose", "label": "Omzet"}}]}}
def invoice(mid, contact, ref, price, desc, x, y, flt=None):
    m = {"id": mid, "module": "moneybird:createAnInvoice", "version": 1, "parameters": MB_P,
         "mapper": {"currency": "EUR", "contactId": contact, "reference": ref, "workflowId": "493446260745831581", "customFields": {}, "pricesAreInclTax": True,
                    "detailsAttributes": [{"price": price, "amount": "1", "description": desc, "tax_rate_id": "485681099381409517", "ledger_account_id": "485681098151429439"}]},
         "metadata": {"restore": {"expect": INV_EXPECT, "parameters": MB_R}, "designer": d(x, y)}}
    if flt: m["filter"] = flt
    return m
def send(mid, inv, x, y):
    return {"id": mid, "module": "moneybird:universal", "version": 1, "parameters": MB_P,
            "mapper": {"url": "/v2/485681097863070897/sales_invoices/{{%d.id}}/send_invoice.json" % inv, "body": "{\"sales_invoice_sending\":{\"delivery_method\":\"Manual\"}}", "types": "text", "method": "PATCH", "headers": [{"key": "Content-Type", "value": "application/json"}], "dataEnter": "manual"},
            "metadata": {"restore": {"expect": {"types": {"mode": "chose"}, "method": {"mode": "chose"}, "headers": {"mode": "chose", "items": [None]}, "dataEnter": {"mode": "chose"}}, "parameters": MB_R}, "designer": d(x, y)}}
def pay(mid, inv, price, tid, x, y):
    return {"id": mid, "module": "moneybird:ActionCreateSalesInvoicePayment", "version": 1, "parameters": MB_P,
            "mapper": {"price": price, "invoice_id": "{{%d.id}}" % inv, "payment_date": "{{formatDate(now; \"YYYY-MM-DD\"; \"Europe/Amsterdam\")}}", "transaction_identifier": tid},
            "metadata": {"restore": {"expect": {"invoice_id": {"mode": "edit"}}, "parameters": MB_R}, "designer": d(x, y)}}
def contacts(mid, q, x, y, flt):
    return {"id": mid, "module": "moneybird:listContacts", "version": 1, "parameters": MB_P, "filter": flt,
            "mapper": {"limit": "1", "query": q}, "metadata": {"restore": {"parameters": MB_R}, "designer": d(x, y)}}
DESC = "Baanhuur Halloween Padel Special · zaterdag 31 oktober · {{3.start}} tot {{3.eind}} · {{3.naam}}"
vps = lambda i: '{{if(get(split(3.vps; ","); %d) = "ja"; " (V)"; "")}}' % i
SHEET_EXPECT = {"from": {"label": "My Drive"}, "mode": {"label": "Search by path"}, "sheetId": {"label": "Boekingen"}, "spreadsheetId": {"path": ["Halloween Padel 31 oktober · boekingen en check-in"]}, "includesHeaders": {"label": "Yes"}, "useColumnHeaders": {"label": "No"}, "valueInputOption": {"mode": "chose", "label": "User entered"}}

routeA = [
    {"id": 3, "module": "json:ParseJSON", "version": 1, "parameters": {}, "mapper": {"json": "{{2.metadata}}"}, "metadata": {"designer": d(900, -300)},
     "filter": {"name": "nieuwe betaling", "conditions": [[{"a": "{{2.status}}", "b": "paid", "o": "text:equal"}, {"a": "{{2.metadata}}", "b": "{", "o": "text:contain"}, {"a": "{{2.paidAt}}", "b": "{{addMinutes(now; -30)}}", "o": "date:greater"}, {"a": "{{ifempty(2.amountRefunded; 0)}}", "b": "0", "o": "number:equal"}]]}},
    {"id": 4, "module": "google-sheets:addRow", "version": 2, "parameters": GS_P,
     "mapper": {"from": "drive", "mode": "select", "values": {"0": "{{3.start}}", "1": "{{3.eind}}", "3": "{{3.naam}}", "4": "'{{3.telefoon}}", "5": "{{3.naam}}" + vps(1), "6": "{{3.s2}}" + vps(2), "7": "{{3.s3}}" + vps(3), "8": "{{3.s4}}" + vps(4),
                "9": '{{(length(3.vps) - length(replace(3.vps; "ja"; ""))) / 2}}', "10": '{{formatNumber(2.amount; 2; ","; "")}}', "11": '{{replace(3.uren; "."; ",")}}', "12": "{{2.id}}", "13": '{{formatDate(2.paidAt; "DD-MM-YYYY HH:mm"; "Europe/Amsterdam")}}'},
                "sheetId": "Boekingen", "spreadsheetId": "/" + SHEET, "includesHeaders": True, "insertDataOption": "OVERWRITE", "useColumnHeaders": False, "valueInputOption": "USER_ENTERED", "insertUnformatted": False},
     "metadata": {"restore": {"expect": dict(SHEET_EXPECT, insertDataOption={"mode": "chose", "label": "Overwrite"}, insertUnformatted={"mode": "chose"}), "parameters": GS_R}, "designer": d(1200, -300)}},
    {"id": 17, "module": "datastore:AddRecord", "version": 1, "parameters": {"datastore": DS},
     "mapper": {"key": "{{2.id}}", "overwrite": True, "data": {"terugbetaald": 0}}, "metadata": ds_meta(1500, -300),
     "onerror": [{"id": 18, "module": "builtin:Resume", "version": 1, "mapper": {}, "parameters": {}, "metadata": {"designer": d(1500, -150)}}]},
    {"id": 15, "module": "google-email:sendAnEmail", "version": 4, "parameters": {"__IMTCONN__": 6999678},
     "mapper": {"to": ["{{3.email}}"], "subject": "🎃 Je baan staat vast: Halloween Padel, za 31 okt {{3.start}}", "bodyType": "rawHtml", "content": html},
     "onerror": [{"id": 16, "module": "builtin:Resume", "version": 1, "mapper": {}, "parameters": {}, "metadata": {"designer": d(1800, -600)}}],
     "metadata": {"restore": {"expect": {"cc": {"mode": "chose"}, "to": {"mode": "chose", "items": [None]}, "bcc": {"mode": "chose"}, "from": {"mode": "chose"}, "bodyType": {"label": "Raw HTML"}, "attachments": {"mode": "chose"}, "emailHeaders": {"mode": "chose"}},
                              "parameters": {"__IMTCONN__": {"data": {"scoped": "true", "connection": "google-email"}, "label": "My Gmail connection (l.debruin@allcourtacademy.com)"}}}, "designer": d(1800, -450)}},
    contacts(5, "{{3.email}}", 2100, -300, {"name": "alleen echte betalingen naar Moneybird", "conditions": [[{"a": "{{2.mode}}", "b": "live", "o": "text:equal"}]]}),
    {"id": 6, "module": "builtin:BasicRouter", "version": 1, "mapper": None, "metadata": {"designer": d(2400, -300)}, "routes": [
        {"flow": [
            {"id": 7, "module": "moneybird:createAContact", "version": 1, "parameters": MB_P,
             "filter": {"name": "nieuw contact", "conditions": [[{"a": "{{5.`__IMTLENGTH__`}}", "b": "0", "o": "number:equal"}]]},
             "mapper": {"phone": "{{3.telefoon}}", "firstname": "{{3.naam}}", "customFields": {}, "sendInvoicesToEmail": ["{{3.email}}"]},
             "metadata": {"restore": {"expect": {"sendInvoicesToEmail": {"mode": "chose", "items": [None]}}, "parameters": MB_R}, "advanced": True, "designer": d(2700, -450)}},
            invoice(8, "{{7.id}}", "Mollie {{2.id}}", "{{2.amount}}", DESC, 3000, -450),
            send(10, 8, 3300, -450),
            pay(11, 8, "{{2.amount}}", "{{2.id}}", 3600, -450)]},
        {"flow": [
            invoice(12, "{{5.id}}", "Mollie {{2.id}}", "{{2.amount}}", DESC, 2700, -150, {"name": "bestaat al", "conditions": [[{"a": "{{5.`__IMTLENGTH__`}}", "b": "1", "o": "number:greaterorequal"}]]}),
            send(13, 12, 3000, -150),
            pay(14, 12, "{{2.amount}}", "{{2.id}}", 3300, -150)]}]}]

CREDIT = "{{round((ifempty(21.terugbetaald; 0) - 2.amountRefunded) * 100) / 100}}"
routeB = [
    {"id": 20, "module": "json:ParseJSON", "version": 1, "parameters": {}, "mapper": {"json": "{{2.metadata}}"}, "metadata": {"designer": d(900, 300)},
     "filter": {"name": "terugbetaling", "conditions": [[{"a": "{{ifempty(2.amountRefunded; 0)}}", "b": "0", "o": "number:greater"}, {"a": "{{2.metadata}}", "b": "{", "o": "text:contain"}]]}},
    {"id": 31, "module": "builtin:BasicRouter", "version": 1, "mapper": None, "metadata": {"designer": d(1200, 300)}, "routes": [
        {"flow": [
            {"id": 21, "module": "datastore:GetRecord", "version": 1, "parameters": {"datastore": DS}, "mapper": {"key": "{{2.id}}", "returnWrapped": False}, "metadata": ds_meta(1500, 150)},
            contacts(22, "{{20.email}}", 1800, 150, {"name": "nieuw terug te betalen bedrag, echte betaling", "conditions": [[{"a": "{{2.mode}}", "b": "live", "o": "text:equal"}, {"a": "{{2.amountRefunded - ifempty(21.terugbetaald; 0)}}", "b": "0.004", "o": "number:greater"}]]}),
            invoice(23, "{{22.id}}", "Mollie {{2.id}} terugbetaling", CREDIT, "Terugbetaling baanhuur Halloween Padel Special · zaterdag 31 oktober · {{20.start}} tot {{20.eind}} · {{20.naam}}", 2100, 150,
                    {"name": "contact gevonden", "conditions": [[{"a": "{{22.`__IMTLENGTH__`}}", "b": "1", "o": "number:greaterorequal"}]]}),
            send(24, 23, 2400, 150),
            pay(25, 23, CREDIT, "{{2.id}} terugbetaling", 2700, 150),
            {"id": 26, "module": "datastore:AddRecord", "version": 1, "parameters": {"datastore": DS},
             "mapper": {"key": "{{2.id}}", "overwrite": True, "data": {"terugbetaald": "{{2.amountRefunded}}"}}, "metadata": ds_meta(3000, 150)}]},
        {"flow": [
            {"id": 27, "module": "google-sheets:filterRows", "version": 2, "parameters": GS_P,
             "mapper": {"from": "drive", "limit": 1, "filter": [[{"a": "M", "b": "{{2.id}}", "o": "text:equal"}]], "sheetId": "Boekingen", "sortOrder": "asc", "spreadsheetId": SHEET, "tableFirstRow": "A1:CZ1", "includesHeaders": True, "valueRenderOption": "UNFORMATTED_VALUE", "dateTimeRenderOption": "FORMATTED_STRING"},
             "metadata": {"restore": {"expect": {"from": {"label": "Select from My Drive"}, "orderBy": {"mode": "chose", "label": "Empty"}, "sheetId": {"mode": "chose", "label": "Boekingen"}, "sortOrder": {"mode": "chose", "label": "Ascending"}, "spreadsheetId": {"mode": "chose", "label": "Halloween Padel 31 oktober · boekingen en check-in"}, "tableFirstRow": {"label": "A-CZ"}, "includesHeaders": {"mode": "chose", "label": "Yes"}, "valueRenderOption": {"mode": "chose", "label": "Unformatted value"}, "dateTimeRenderOption": {"mode": "chose", "label": "Formatted string"}}, "parameters": GS_R}, "designer": d(1500, 450)},
             "onerror": [{"id": 28, "module": "builtin:Ignore", "version": 1, "mapper": {}, "parameters": {}, "metadata": {"designer": d(1500, 600)}}]},
            {"id": 29, "module": "google-sheets:updateRow", "version": 2, "parameters": GS_P,
             "filter": {"name": "boeking staat in de sheet", "conditions": [[{"a": "{{27.`__ROW_NUMBER__`}}", "o": "exist"}]]},
             "mapper": {"from": "drive", "mode": "select", "values": {"14": '{{formatNumber(2.amountRefunded; 2; ","; "")}}'}, "sheetId": "Boekingen", "rowNumber": "{{27.`__ROW_NUMBER__`}}", "spreadsheetId": "/" + SHEET, "includesHeaders": True, "useColumnHeaders": False, "valueInputOption": "USER_ENTERED"},
             "metadata": {"restore": {"expect": SHEET_EXPECT, "parameters": GS_R}, "designer": d(1800, 450)},
             "onerror": [{"id": 32, "module": "builtin:Ignore", "version": 1, "mapper": {}, "parameters": {}, "metadata": {"designer": d(1800, 600)}}]}]}]}]

bp = {"name": "halloween betaald naar sheet en Moneybird",
      "metadata": {"instant": True, "version": 1, "designer": {"orphans": []}, "scenario": {"dlq": False, "dataloss": False, "maxErrors": 3, "autoCommit": True, "roundtrips": 1, "sequential": False, "confidential": False, "freshVariables": False, "autoCommitTriggerLast": True}},
      "flow": [
          {"id": 1, "module": "gateway:CustomWebHook", "version": 1, "mapper": {}, "parameters": {"hook": 3921655, "maxResults": 1},
           "metadata": {"restore": {"parameters": {"hook": {"data": {"editable": "true"}, "label": "Halloween Mollie betaald"}}}, "designer": d(0, 0), "interface": [{"name": "id", "type": "text"}]}},
          {"id": 2, "module": "mollie:getPayment", "version": 1, "mapper": {"id": "{{1.id}}"}, "parameters": {"__IMTCONN__": 10761452},
           "onerror": [{"id": 9, "module": "builtin:Ignore", "version": 1, "mapper": {}, "parameters": {}, "metadata": {"designer": d(300, 300)}}],
           "metadata": {"restore": {"expect": {"id": {"mode": "edit"}, "embed": {"mode": "chose"}, "include": {"mode": "chose"}}, "parameters": {"__IMTCONN__": {"data": {"scoped": "true", "connection": "mollie"}, "label": "Lars's Mollie connection (All Court Academy B.V.)"}}}, "designer": d(300, 0)}},
          {"id": 30, "module": "builtin:BasicRouter", "version": 1, "mapper": None, "metadata": {"designer": d(600, 0)}, "routes": [{"flow": routeA}, {"flow": routeB}]}]}
ids = []
def walk(f):
    for m in f:
        ids.append(m["id"]); [ids.append(e["id"]) for e in m.get("onerror", [])]
        for r in m.get("routes", []): walk(r["flow"])
walk(bp["flow"]); assert len(ids) == len(set(ids)), ids
out = HIER / 'blueprint.json'
open(out, 'w').write(json.dumps(bp, ensure_ascii=False, separators=(',', ':')))
print(len(json.dumps(bp, ensure_ascii=False)), sorted(ids))
