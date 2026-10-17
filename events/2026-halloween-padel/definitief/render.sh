#!/bin/sh
# Rendert poster.html op 2x naar feed (2160x2700, ook een versie met QR-code), story (2160x3840) en print (2160x2892 + pdf 30x40 cm).
cd "$(dirname "$0")"
CHROME=${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}
mkdir -p _tmp
for F in feed:1350 feed-qr:1350 story:1920 print:1446; do
  N=${F%%:*}; H=${F##*:}
  "$CHROME" --headless=new --no-sandbox --hide-scrollbars --window-size=1080,$((H+100)) --force-device-scale-factor=2 --virtual-time-budget=6000 --screenshot=_tmp/$N.png "file://$PWD/poster.html#$N" 2>/dev/null
done
python3 -P - <<'PY'
from PIL import Image
out={'feed':('halloween-padel-ig-feed-4x5.jpg',1350),'feed-qr':('halloween-padel-ig-feed-4x5-qr.jpg',1350),'story':('halloween-padel-ig-story-9x16.jpg',1920),'print':('halloween-padel-poster.jpg',1446)}
for n,(f,h) in out.items():
    im=Image.open(f'_tmp/{n}.png').convert('RGB').crop((0,0,2160,h*2)); im.save(f,quality=94); print(f,im.size)
    if n=='print': im.save('halloween-padel-poster-30x40cm.pdf',resolution=im.width/(30/2.54))
PY
rm -rf _tmp
