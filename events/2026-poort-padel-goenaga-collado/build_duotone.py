"""Maakt de duotone-foto's voor de poster: grijswaarden -> donkergroen (schaduw) -> Poort Padel-groen -> lime (hoge lichten).
Gebruik: python3 build_duotone.py  (schrijft naar build/)"""
from PIL import Image, ImageOps, ImageEnhance
import numpy as np

STOPS = [(0.0, (8, 22, 19)), (0.45, (53, 91, 82)), (0.8, (150, 190, 140)), (1.0, (205, 253, 80))]


def duotone(im, dst, stops=STOPS):
    g = ImageOps.autocontrast(ImageOps.grayscale(im.convert('RGB')), cutoff=1)
    g = ImageEnhance.Contrast(g).enhance(1.15)
    a = np.asarray(g).astype(np.float32) / 255.0
    out = np.zeros(a.shape + (3,), np.float32)
    for (p0, c0), (p1, c1) in zip(stops[:-1], stops[1:]):
        m = (a >= p0) & (a <= p1)
        t = ((a - p0) / (p1 - p0))[m][:, None]
        out[m] = np.array(c0) * (1 - t) + np.array(c1) * t
    Image.fromarray(out.astype(np.uint8)).save(dst, quality=94)


if __name__ == '__main__':
    duotone(Image.open('assets/collado-profile.jpg'), 'build/collado-profile-duotone.jpg')
    duotone(Image.open('assets/goenaga-profile.jpg'), 'build/goenaga-duotone.jpg')
    duotone(Image.open('assets/collado-post-06.jpg').crop((0, 0, 1170, 1150)), 'build/collado-duotone.jpg')
