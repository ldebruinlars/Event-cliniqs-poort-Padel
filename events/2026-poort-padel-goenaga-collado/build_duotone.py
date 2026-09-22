"""Maakt de duotone-foto's voor de poster: grijswaarden -> donkergroen (schaduw) -> Poort Padel-groen -> lime (hoge lichten).
Gebruik: python3 build_duotone.py  (schrijft naar build/)"""
from PIL import Image, ImageOps, ImageEnhance
import numpy as np

STOPS = [(0.0, (8, 22, 19)), (0.45, (53, 91, 82)), (0.8, (150, 190, 140)), (1.0, (205, 253, 80))]
# voor huid en haar: zelfde schaduwen, maar de hoge lichten lopen naar een warm, neutraal licht in plaats van lime
STOPS_SKIN = [(0.0, (8, 22, 19)), (0.45, (60, 88, 80)), (0.8, (175, 178, 160)), (1.0, (238, 232, 218))]


def _map(a, stops):
    out = np.zeros(a.shape + (3,), np.float32)
    for (p0, c0), (p1, c1) in zip(stops[:-1], stops[1:]):
        m = (a >= p0) & (a <= p1)
        t = ((a - p0) / (p1 - p0))[m][:, None]
        out[m] = np.array(c0) * (1 - t) + np.array(c1) * t
    return out


def duotone(im, dst, stops=STOPS, mask=None):
    """mask (L-beeld, wit = persoon): daar STOPS_SKIN, elders `stops`; de rand wordt zacht overgeblend."""
    g = ImageOps.autocontrast(ImageOps.grayscale(im.convert('RGB')), cutoff=1)
    g = ImageEnhance.Contrast(g).enhance(1.15)
    a = np.asarray(g).astype(np.float32) / 255.0
    out = _map(a, stops)
    if mask is not None:
        from PIL import ImageFilter
        w = np.asarray(mask.convert('L').filter(ImageFilter.GaussianBlur(3))).astype(np.float32)[:, :, None] / 255.0
        out = _map(a, STOPS_SKIN) * w + out * (1 - w)
    Image.fromarray(out.astype(np.uint8)).save(dst, quality=94)


if __name__ == '__main__':
    duotone(Image.open('build/collado-profile-clean.jpg'), 'build/collado-profile-duotone.jpg',
            mask=Image.open('build/collado-mask.png'))  # flare weg + persoon zonder lime, zie build_clean_collado.py
    duotone(Image.open('assets/goenaga-profile.jpg'), 'build/goenaga-duotone.jpg')
    duotone(Image.open('assets/collado-post-06.jpg').crop((0, 0, 1170, 1150)), 'build/collado-duotone.jpg')
