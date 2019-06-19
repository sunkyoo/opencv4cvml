import numpy as np
import cv2 as cv


def contrast1():
    src = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    s = 2.0
    dst = cv.multiply(src, s)

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def contrast2():
    src = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    alpha = 1.0
    dst = cv.convertScaleAbs(src, alpha=1+alpha, beta=-128*alpha)

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == '__main__':
    contrast1()
    contrast2()
