#!/usr/bin/env python3
"""Mail-merge voor de All Court Academy eventcampagne.

Leest outreach/leads.csv, vult een template uit email/ in en verstuurt via Gmail SMTP.
Standaard DRY-RUN: er wordt niets verstuurd, je ziet alleen wat er zou gaan.

Gebruik:
    python3 outreach/send_campaign.py                       # dry-run, alle leads
    python3 outreach/send_campaign.py --segment scholen     # alleen scholen
    python3 outreach/send_campaign.py --send --limit 40     # echt versturen, max 40

Vereist voor --send (Gmail met 2FA + app-wachtwoord):
    export ACA_SMTP_USER="info@allcourtacademy.com"
    export ACA_SMTP_PASS="xxxx xxxx xxxx xxxx"     # Google app-wachtwoord
Optioneel:
    export ACA_SMTP_HOST="smtp.gmail.com"  ACA_SMTP_PORT="587"
    export ACA_FROM_NAME="Lars de Bruin | All Court Academy"

Kolommen in leads.csv (kop verplicht):
    segment,bedrijf,voornaam,email,plaats,sector,opt_out,notitie
    segment  = bedrijven | scholen
    voornaam = mag leeg; dan wordt de aanhef "Hey team van {bedrijf}"
    opt_out  = 1 om over te slaan
Verzonden adressen worden gelogd in outreach/sent_log.csv en niet nogmaals gemaild.
"""
import argparse
import csv
import os
import re
import smtplib
import sys
import time
from datetime import datetime
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEADS = ROOT / "outreach" / "leads.csv"
LOG = ROOT / "outreach" / "sent_log.csv"
TEMPLATES = {
    "bedrijven": ROOT / "email" / "template-bedrijven.md",
    "scholen": ROOT / "email" / "template-scholen.md",
}
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$", re.I)


def load_template(path: Path):
    """Template = eerste regel 'Onderwerp: ...', lege regel, daarna de body."""
    text = path.read_text(encoding="utf-8")
    first, _, body = text.partition("\n")
    if not first.lower().startswith("onderwerp:"):
        sys.exit(f"{path}: eerste regel moet beginnen met 'Onderwerp:'")
    return first.split(":", 1)[1].strip(), body.strip() + "\n"


def render(text: str, lead: dict) -> str:
    voornaam = (lead.get("voornaam") or "").strip()
    bedrijf = (lead.get("bedrijf") or "").strip()
    aanhef = f"Hey {voornaam}" if voornaam else f"Hey team van {bedrijf}"
    values = {**lead, "aanhef": aanhef}
    def sub(m):
        key = m.group(1)
        return str(values.get(key, "")).strip()
    return re.sub(r"\{\{\s*(\w+)\s*\}\}", sub, text)


def already_sent() -> set:
    if not LOG.exists():
        return set()
    with LOG.open(encoding="utf-8") as f:
        return {row["email"].lower() for row in csv.DictReader(f)}


def log_sent(lead: dict, subject: str):
    new = not LOG.exists()
    with LOG.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["timestamp", "segment", "bedrijf", "email", "onderwerp"])
        w.writerow([datetime.now().isoformat(timespec="seconds"), lead["segment"], lead["bedrijf"], lead["email"], subject])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--send", action="store_true", help="echt versturen (anders dry-run)")
    ap.add_argument("--segment", choices=list(TEMPLATES), help="alleen dit segment")
    ap.add_argument("--limit", type=int, default=50, help="max aantal mails per run (Gmail: hou het onder ~100/dag)")
    ap.add_argument("--pause", type=float, default=20.0, help="seconden tussen mails")
    ap.add_argument("--leads", default=str(LEADS))
    args = ap.parse_args()

    templates = {k: load_template(v) for k, v in TEMPLATES.items()}
    sent = already_sent()

    with open(args.leads, encoding="utf-8") as f:
        leads = list(csv.DictReader(f))

    todo = []
    for lead in leads:
        seg = (lead.get("segment") or "").strip().lower()
        email = (lead.get("email") or "").strip().lower()
        if args.segment and seg != args.segment:
            continue
        if seg not in templates:
            print(f"SKIP onbekend segment '{seg}': {lead.get('bedrijf')}")
            continue
        if (lead.get("opt_out") or "").strip() in ("1", "ja", "true"):
            print(f"SKIP opt-out: {email}")
            continue
        if not EMAIL_RE.match(email):
            print(f"SKIP ongeldig e-mailadres: '{email}' ({lead.get('bedrijf')})")
            continue
        if email in sent:
            print(f"SKIP al verstuurd: {email}")
            continue
        if lead.get("bedrijf", "").upper().startswith("VOORBEELD"):
            print(f"SKIP voorbeeldregel: {lead.get('bedrijf')}")
            continue
        lead["segment"] = seg
        lead["email"] = email
        todo.append(lead)

    todo = todo[: args.limit]
    print(f"{len(todo)} mails klaar om te {'versturen' if args.send else 'tonen (dry-run)'}\n")

    server = None
    if args.send:
        user = os.environ.get("ACA_SMTP_USER")
        pw = os.environ.get("ACA_SMTP_PASS")
        if not user or not pw:
            sys.exit("Zet ACA_SMTP_USER en ACA_SMTP_PASS (Google app-wachtwoord) als omgevingsvariabelen.")
        host = os.environ.get("ACA_SMTP_HOST", "smtp.gmail.com")
        port = int(os.environ.get("ACA_SMTP_PORT", "587"))
        server = smtplib.SMTP(host, port, timeout=30)
        server.starttls()
        server.login(user, pw)
        from_name = os.environ.get("ACA_FROM_NAME", "Lars de Bruin | All Court Academy")
        sender = formataddr((from_name, user))

    for i, lead in enumerate(todo, 1):
        subject_t, body_t = templates[lead["segment"]]
        subject = render(subject_t, lead)
        body = render(body_t, lead)
        print(f"--- [{i}/{len(todo)}] {lead['segment']} → {lead['bedrijf']} <{lead['email']}>")
        print(f"Onderwerp: {subject}")
        if not args.send:
            print(body)
            continue
        msg = EmailMessage()
        msg["From"] = sender
        msg["To"] = lead["email"]
        msg["Subject"] = subject
        msg["Reply-To"] = os.environ.get("ACA_SMTP_USER")
        msg.set_content(body)
        server.send_message(msg)
        log_sent(lead, subject)
        print("verstuurd")
        if i < len(todo):
            time.sleep(args.pause)

    if server:
        server.quit()


if __name__ == "__main__":
    main()
