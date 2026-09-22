#!/bin/sh
# Rendert poster.html naar PNG op exact 1080 x 1350 (Instagram 4:5) en een 2x-versie (2160 x 2700).
# Chromium headless snijdt onderaan ~90 px af van de window-size, daarom hoger renderen en daarna bijsnijden.
cd "$(dirname "$0")"
CHROME=${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}
SRC=${1:-poster.html}
OUT=${2:-poster}
"$CHROME" --headless=new --no-sandbox --hide-scrollbars --window-size=1080,1450 --force-device-scale-factor=1 --screenshot=build/_r1.png "file://$PWD/$SRC" 2>/dev/null
"$CHROME" --headless=new --no-sandbox --hide-scrollbars --window-size=1080,1450 --force-device-scale-factor=2 --screenshot=build/_r2.png "file://$PWD/$SRC" 2>/dev/null
python3 - "$OUT" <<'PY'
import sys; from PIL import Image
out=sys.argv[1]
Image.open('build/_r1.png').crop((0,0,1080,1350)).save(f'{out}-1080x1350.png')
Image.open('build/_r2.png').crop((0,0,2160,2700)).save(f'{out}-2160x2700.png')
for f in [f'{out}-1080x1350.png',f'{out}-2160x2700.png']: print(f, Image.open(f).size)
PY
rm -f build/_r1.png build/_r2.png
