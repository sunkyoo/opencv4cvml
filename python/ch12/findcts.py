import numpy as np
import cv2
import random


def contours_basic():
    src = cv2.imread('contours.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    contours, _ = cv2.findContours(src, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    for i in range(len(contours)):
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.drawContours(dst, contours, i, c, 2)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()


def contours_hier():
    src = cv2.imread('contours.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    contours, hierarchy = cv2.findContours(src, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    idx = 0
    while idx >= 0:
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.drawContours(dst, contours, idx, c, -1, cv2.LINE_8, hierarchy)
        idx = hierarchy[0, idx, 0]

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    contours_basic()
    contours_hier()
