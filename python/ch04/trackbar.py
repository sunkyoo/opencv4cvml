import numpy as np
import cv2 as cv


def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0

    return value


def on_level_change(pos):
    img[:] = saturated(pos * 16)
    cv.imshow('image', img)


img = np.zeros((400, 400), np.uint8)

cv.namedWindow('image')
cv.createTrackbar('level', 'image', 0, 16, on_level_change)

cv.imshow('image', img)
cv.waitKey()
cv.destroyAllWindows()
