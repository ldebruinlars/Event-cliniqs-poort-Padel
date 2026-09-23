#!/bin/sh
# Rendert poster.html (1744 x 2336) op 2x naar de printposter en maakt daaruit de Instagram feed (4:5) en story (9:16).
cd "$(dirname "$0")"
CHROME=${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}
"$CHROME" --headless=new --no-sandbox --hide-scrollbars --window-size=1744,2436 --force-device-scale-factor=2 --virtual-time-budget=8000 --screenshot=build/_r.png "file://$PWD/poster.html" 2>/dev/null
python3 - <<'PY'
from PIL import Image
OUT='../final/'
WALL=(14,12,10)
import numpy as np
big=Image.open('build/_r.png').crop((0,0,3488,4672)).convert('RGB')
# krijteffect: waar de render van het kale bord afwijkt (tekst, balken, patroon) de dekking laten variëren met ruis
board=Image.open('build/board.jpg').convert('RGB').resize(big.size,Image.LANCZOS)
R=np.asarray(big).astype(np.float32); B=np.asarray(board).astype(np.float32)
rng=np.random.default_rng(5); n=rng.random((big.height//2,big.width//2)).astype(np.float32)
from PIL import ImageFilter
n=np.asarray(Image.fromarray((n*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.7)).resize(big.size,Image.BILINEAR)).astype(np.float32)/255
a=(0.70+0.30*n)[:,:,None]
LOGO_Y=2130*2   # onder deze regel (logostrook) geen krijteffect
a[LOGO_Y:,:,:]=1.0
big=Image.fromarray((R*a+B*(1-a)).astype(np.uint8))
big.save(OUT+'padel-quiz-v2-poster.jpg',quality=95)
big.save(OUT+'padel-quiz-v2-poster-30x40cm.pdf',resolution=big.width/(30/2.54))
fb=big.resize((int(big.width*2700/big.height),2700),Image.LANCZOS); feed=Image.new('RGB',(2160,2700),WALL); feed.paste(fb,((2160-fb.width)//2,0)); feed.save(OUT+'padel-quiz-v2-ig-feed-4x5.jpg',quality=95)
sb=big.resize((2160,int(big.height*2160/big.width)),Image.LANCZOS); story=Image.new('RGB',(2160,3840),WALL); story.paste(sb,(0,(3840-sb.height)//2)); story.save(OUT+'padel-quiz-v2-ig-story-9x16.jpg',quality=95)
prev=big.resize((1080,1446),Image.LANCZOS); prev.save('build/_prev.jpg',quality=88)
print('poster',big.size,'feed',feed.size,'story',story.size)
PY
rm -f build/_r.png
