"""Maakt het krijtbord met verkleinde illustratie: meer lege bordruimte onderin voor programma, prijs en logo's.
Bron: ../assets/artwork/krijtbord-variant-1-zonder-tekst.jpg (1744 x 2336). Uitvoer: build/board.jpg (zelfde maat)
plus build/chalk-mask.png (ruis voor het krijteffect op de tekst) en build/p-pattern.png (P-patroon, krijtwit)."""
from PIL import Image, ImageFilter, ImageDraw
import numpy as np

SRC = '../assets/artwork/krijtbord-variant-1-zonder-tekst.jpg'
art = Image.open(SRC).convert('RGB'); W, H = art.size
FR = 72                      # dikte houten lijst
SCALE = 0.80                 # illustratie verkleinen
inner = (FR, FR, W - FR, H - FR)

# 1. leeg bord: het lege stuk onderin (rijen 1780-2180) gespiegeld herhalen tot de hele binnenmaat
blank = art.crop((FR, 1780, W - FR, 2180))
board = Image.new('RGB', (W, H)); board.paste(art, (0, 0))
tile = Image.new('RGB', (W - 2 * FR, H - 2 * FR))
y = 0; flip = False
while y < tile.height:
    t = blank.transpose(Image.FLIP_TOP_BOTTOM) if flip else blank
    tile.paste(t, (0, y)); y += blank.height; flip = not flip
tile = tile.filter(ImageFilter.GaussianBlur(0.6))
board.paste(tile, (FR, FR))

# 2. illustratie (bovenste 1700 px binnen de lijst) verkleind en met zachte rand op het bord
ill = art.crop((FR, FR, W - FR, 1700)).resize((int((W - 2 * FR) * SCALE), int((1700 - FR) * SCALE)), Image.LANCZOS)
m = Image.new('L', ill.size, 0); d = ImageDraw.Draw(m); f = 36
d.rectangle((f, f, ill.width - f, ill.height - f), fill=255); m = m.filter(ImageFilter.GaussianBlur(f / 2))
from PIL import ImageEnhance; ill = ImageEnhance.Contrast(ill).enhance(1.08)
board.paste(ill, ((W - ill.width) // 2, FR + 10), m)
board.save('build/board.jpg', quality=95)
print('board', board.size, 'illustratie tot y =', FR + 10 + ill.height)

# 3. krijtmasker: ruis als luminantiemasker (wit = zichtbaar)
rng = np.random.default_rng(3)
n = rng.random((H // 2, W // 2)).astype(np.float32)
n = np.asarray(Image.fromarray((n * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.7))).astype(np.float32) / 255
mask = (255 * (0.72 + 0.28 * n)).astype(np.uint8)
Image.fromarray(mask).resize((W, H), Image.BILINEAR).save('build/chalk-mask.png')

# 4. P-patroon in krijtwit, verspringend
g = Image.open('build/p-poort-padel.png').convert('RGBA'); pw = 110
g = g.resize((pw, int(g.height * pw / g.width)), Image.LANCZOS)
a = g.split()[3].point(lambda v: int(v * 0.045)); glyph = Image.new('RGBA', g.size, (235, 235, 225, 0)); glyph.putalpha(a)
gx, gy = 60, 46; tw, th = 2 * (pw + gx), 2 * (g.height + gy)
t = Image.new('RGBA', (tw, th), (0, 0, 0, 0)); t.alpha_composite(glyph, (0, 0)); t.alpha_composite(glyph, (pw + gx, g.height + gy))
t.save('build/p-pattern.png'); print('klaar')
