import numpy as np
import cv2 as cv


src = cv.imread('rose.bmp', cv.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    exit()

emboss = np.array([[-1, -1, 0],
                   [-1, 0, 1],
                   [0, 1, 1]], np.float32)

dst = cv.filter2D(src, -1, emboss, delta=128)

cv.imshow('src', src)
cv.imshow('dst', dst)

cv.waitKey()
cv.destroyAllWindows()
