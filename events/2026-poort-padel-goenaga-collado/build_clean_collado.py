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
