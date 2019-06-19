import numpy as np
import cv2 as cv
import sys


def on_threshold(pos):
    _, dst = cv.threshold(src, pos, 255, cv.THRESH_BINARY)
    cv.imshow('dst', dst)


filename = 'neutrophils.png'
if len(sys.argv) > 1:
    filename = sys.argv[1]

src = cv.imread(filename, cv.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    exit()

cv.imshow('src', src)

cv.namedWindow('dst')
cv.createTrackbar('Threshold', 'dst', 0, 255, on_threshold)
cv.setTrackbarPos('Threshold', 'dst', 128)

cv.waitKey(0)
cv.destroyAllWindows()
