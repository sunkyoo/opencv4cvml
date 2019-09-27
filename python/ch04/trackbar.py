import numpy as np
import cv2


def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0

    return value


def on_level_change(pos):
    img[:] = saturated(pos * 16)
    cv2.imshow('image', img)


img = np.zeros((400, 400), np.uint8)

cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
