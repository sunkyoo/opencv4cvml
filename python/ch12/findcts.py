import numpy as np
import cv2 as cv
import random


def contours_basic():
    src = cv.imread('contours.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    contours, _ = cv.findContours(src, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

    dst = cv.cvtColor(src, cv.COLOR_GRAY2BGR)

    for i in range(len(contours)):
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv.drawContours(dst, contours, i, c, 2)

    cv.imshow('src', src)
    cv.imshow('dst', dst)

    cv.waitKey()
    cv.destroyAllWindows()


def contours_hier():
    src = cv.imread('contours.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    contours, hierarchy = cv.findContours(src, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

    dst = cv.cvtColor(src, cv.COLOR_GRAY2BGR)

    idx = 0
    while idx >= 0:
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv.drawContours(dst, contours, idx, c, -1, cv.LINE_8, hierarchy)
        idx = hierarchy[0, idx, 0]

    cv.imshow('src', src)
    cv.imshow('dst', dst)

    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == "__main__":
    contours_basic()
    contours_hier()
