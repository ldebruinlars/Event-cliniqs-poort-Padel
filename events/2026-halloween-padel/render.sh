#!/bin/sh
# Rendert poster.html op 2x naar feed (2160x2700), story (2160x3840) en print (2160x2892 -> pdf A3-verhouding 3:4).
# Gebruik: ./render.sh [bg]   bg=1 pompoenspeler (standaard), bg=0 pompoenbal op de baan
cd "$(dirname "$0")"
BG=${1:-1}
CHROME=${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}
for F in feed:1350 story:1920 print:1446; do
  N=${F%%:*}; H=${F##*:}
  "$CHROME" --headless=new --no-sandbox --hide-scrollbars --window-size=1080,$((H+100)) --force-device-scale-factor=2 --virtual-time-budget=6000 --screenshot=build/_$N.png "file://$PWD/poster.html?bg=$BG#$N" 2>/dev/null
done
python3 -P - "$BG" <<'PY'
import sys; from PIL import Image
bg=sys.argv[1]; tag='' if bg=='1' else '-baan'
for n,h in (('feed',1350),('story',1920),('print',1446)):
    im=Image.open(f'build/_{n}.png').convert('RGB').crop((0,0,2160,h*2))
    out={'feed':f'halloween-padel{tag}-ig-feed-4x5.jpg','story':f'halloween-padel{tag}-ig-story-9x16.jpg','print':f'halloween-padel{tag}-poster.jpg'}[n]
    im.save(out,quality=94); print(out, im.size)
    if n=='print': im.save(out.replace('.jpg','-30x40cm.pdf'),resolution=im.width/(30/2.54))
PY
rm -f build/_*.png
