#!/usr/bin/env bash
# Agent Reach installer voor macOS / Linux
# Gebruik:  bash tools/agent-reach/install-mac.sh
set -euo pipefail

echo "=== Agent Reach installer (macOS/Linux) ==="

PY=""
for c in python3.12 python3.11 python3.10 python3; do
  if command -v "$c" >/dev/null 2>&1; then
    v=$("$c" -c 'import sys; print(sys.version_info.minor)')
    if [ "$v" -ge 10 ]; then PY="$c"; break; fi
  fi
done
if [ -z "$PY" ]; then
  echo "FOUT: Python 3.10+ niet gevonden. Installeer met: brew install python" >&2
  exit 1
fi
echo "Python: $PY"

VENV="$HOME/.agent-reach-venv"
[ -x "$VENV/bin/python" ] || "$PY" -m venv "$VENV"
"$VENV/bin/python" -m pip install --upgrade pip --quiet
"$VENV/bin/python" -m pip install --upgrade "https://github.com/Panniantong/agent-reach/archive/main.zip"

# Zet op PATH voor zsh (macOS standaard) en bash
for rc in "$HOME/.zshrc" "$HOME/.bashrc"; do
  if [ -f "$rc" ] && ! grep -q '.agent-reach-venv/bin' "$rc"; then
    echo 'export PATH="$HOME/.agent-reach-venv/bin:$PATH"' >> "$rc"
  fi
done
export PATH="$VENV/bin:$PATH"

agent-reach install --env=auto --system
agent-reach doctor

echo
echo "Klaar. Open een nieuw terminalvenster zodat 'agent-reach' overal werkt."
echo "Extra platforms: agent-reach install --env=auto --system --channels=opencli,reddit,facebook,instagram"
