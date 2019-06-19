import numpy as np
import cv2 as cv


img = cv.imread('circuit.bmp', cv.IMREAD_COLOR)
templ = cv.imread('crystal.bmp', cv.IMREAD_COLOR)

if img is None or templ is None:
    print('Image load failed!')
    exit()

img = img + (50, 50, 50)

noise = np.zeros(img.shape, np.int32)
cv.randn(noise, 0, 10)
img = cv.add(img, noise, dtype=cv.CV_8UC3)

res = cv.matchTemplate(img, templ, cv.TM_CCOEFF_NORMED)
res_norm = cv.normalize(res, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

_, maxv, _, maxloc = cv.minMaxLoc(res)
print('maxv:', maxv)

(th, tw) = templ.shape[:2]
cv.rectangle(img, maxloc, (maxloc[0] + tw, maxloc[1] + th), (0, 0, 255), 2)

cv.imshow('templ', templ)
cv.imshow('res_norm', res_norm)
cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()
