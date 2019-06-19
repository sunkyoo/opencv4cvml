import numpy as np
import cv2 as cv


def on_trackbar(pos):
    bsize = pos
    if bsize % 2 == 0: bsize = bsize - 1
    if bsize < 3: bsize = 3

    dst = cv.adaptiveThreshold(src, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv.THRESH_BINARY, bsize, 5)

    cv.imshow('dst', dst)


src = cv.imread('sudoku.jpg', cv.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    exit()

cv.imshow('src', src)

cv.namedWindow('dst')
cv.createTrackbar('Block Size', 'dst', 0, 200, on_trackbar)
cv.setTrackbarPos('Block Size', 'dst', 11)

cv.waitKey()
cv.destroyAllWindows()
