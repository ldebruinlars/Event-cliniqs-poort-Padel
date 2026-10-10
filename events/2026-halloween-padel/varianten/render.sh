#!/bin/sh
# Rendert alle varianten (of de opgegeven namen) op 2x naar final/halloween-<naam>-ig-feed-4x5.jpg (2160x2700)
# en maakt een overzicht final/overzicht-alle-versies.jpg.
# Gebruik: python3 -P build.py && ./render.sh [naam ...]
cd "$(dirname "$0")"
CHROME=${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}
mkdir -p final _tmp
NAMES=${*:-$(ls [0-9]*.html | sed 's/\.html$//')}
for N in $NAMES; do
  "$CHROME" --headless=new --no-sandbox --hide-scrollbars --window-size=1080,1450 --force-device-scale-factor=2 --virtual-time-budget=6000 --screenshot=_tmp/$N.png "file://$PWD/$N.html" 2>/dev/null
done
python3 -P - $NAMES <<'PY'
import sys, glob; from PIL import Image, ImageDraw
for n in sys.argv[1:]:
    im=Image.open(f'_tmp/{n}.png').convert('RGB').crop((0,0,2160,2700))
    im.save(f'final/halloween-{n}-ig-feed-4x5.jpg',quality=93); print(n)
fs=sorted(glob.glob('final/halloween-[0-9]*-ig-feed-4x5.jpg'))
tw,th=432,540; cols=5; rows=(len(fs)+cols-1)//cols
sheet=Image.new('RGB',(cols*tw+(cols+1)*16,rows*th+(rows+1)*16),(30,30,30))
for i,f in enumerate(fs):
    t=Image.open(f).resize((tw,th),Image.LANCZOS)
    x=16+(i%cols)*(tw+16); y=16+(i//cols)*(th+16); sheet.paste(t,(x,y))
    d=ImageDraw.Draw(sheet); d.rectangle((x,y,x+46,y+34),fill=(0,0,0)); d.text((x+8,y+6),f.split('-')[2][:2] if False else f.split('halloween-')[1][:2],fill=(255,255,255))
sheet.save('final/overzicht-alle-versies.jpg',quality=90)
PY
rm -rf _tmp
