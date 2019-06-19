import numpy as np
import cv2 as cv


def blurring_mean():
    src = cv.imread('rose.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    cv.imshow('src', src)

    for ksize in range(3, 9, 2):
        dst = cv.blur(src, (ksize, ksize))

        desc = "Mean: %dx%d" % (ksize, ksize)
        cv.putText(dst, desc, (10, 30), cv.FONT_HERSHEY_SIMPLEX,
                   1.0, 255, 1, cv.LINE_AA)

        cv.imshow('dst', dst)
        cv.waitKey()

    cv.destroyAllWindows()


def blurring_gaussian():
    src = cv.imread('rose.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    cv.imshow('src', src)

    for sigma in range(1, 6):
        dst = cv.GaussianBlur(src, (0, 0), sigma)

        desc = "Gaussian: sigma = %d" % (sigma)
        cv.putText(dst, desc, (10, 30), cv.FONT_HERSHEY_SIMPLEX,
                   1.0, 255, 1, cv.LINE_AA)

        cv.imshow('dst', dst)
        cv.waitKey()

    cv.destroyAllWindows()


if __name__ == '__main__':
    blurring_mean()
    blurring_gaussian()
