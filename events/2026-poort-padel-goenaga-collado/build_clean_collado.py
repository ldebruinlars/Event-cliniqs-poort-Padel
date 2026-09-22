"""Werkt de lensflare (lichte streep over borst en arm) weg uit collado-profile.jpg met OpenCV-inpainting.
Schrijft build/collado-profile-clean.jpg; daarna build_duotone.py draaien."""
import cv2, numpy as np

im = cv2.imread('assets/collado-profile.jpg'); h, w = im.shape[:2]
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
S, V = hsv[:, :, 1].astype(int), hsv[:, :, 2].astype(int)
region = np.zeros((h, w), np.uint8)
cv2.line(region, (540, 770), (1079, 390), 255, 150)   # streep over borst en bovenarm
cv2.line(region, (960, 580), (1079, 430), 255, 110)   # kleine flare aan de rechterrand
flare = ((V > 165) & (S < 120)) | (V > 200)           # licht en/of verbleekt; het blauwe shirt blijft verzadigd
mask = cv2.bitwise_and((flare * 255).astype(np.uint8), region)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
mask = cv2.dilate(mask, np.ones((11, 11), np.uint8), iterations=2)
out = cv2.inpaint(im, mask, 12, cv2.INPAINT_TELEA)
cv2.imwrite('build/collado-profile-clean.jpg', out, [cv2.IMWRITE_JPEG_QUALITY, 95])
print('klaar, maskerpixels:', int(mask.sum() / 255))

# --- achtergrond rustig maken: persoon vrijstaand (GrabCut), bokeh erachter donker en zacht ---
mask2 = np.zeros((h, w), np.uint8)
bgd, fgd = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
cv2.grabCut(out, mask2, (230, 90, 850, 990), bgd, fgd, 8, cv2.GC_INIT_WITH_RECT)
fg = np.where((mask2 == cv2.GC_FGD) | (mask2 == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
fg = cv2.morphologyEx(fg, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
fg = cv2.morphologyEx(fg, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
n, lab, stats, _ = cv2.connectedComponentsWithStats(fg)          # alleen het grootste stuk (de persoon) houden
fg = np.where(lab == 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA]), 255, 0).astype(np.uint8)
alpha = cv2.GaussianBlur(fg, (0, 0), 4).astype(np.float32)[:, :, None] / 255.0
bg = cv2.GaussianBlur(out, (0, 0), 9).astype(np.float32) * 0.38  # donkerder en zachter, stippen verdwijnen
comp = out.astype(np.float32) * alpha + bg * (1 - alpha)
cv2.imwrite('build/collado-profile-clean.jpg', comp.astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 95])
cv2.imwrite('build/collado-mask.png', fg)
print('achtergrond gedempt')
