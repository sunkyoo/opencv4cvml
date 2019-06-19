import numpy as np
import cv2 as cv
import random


def noise_gaussian():
    src = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    cv.imshow('src', src)

    for stddev in [10, 20, 30]:
        noise = np.zeros(src.shape, np.int32)
        cv.randn(noise, 0, stddev)

        dst = cv.add(src, noise, dtype=cv.CV_8UC1)

        desc = 'stddev = %d' % stddev
        cv.putText(dst, desc, (10, 30), cv.FONT_HERSHEY_SIMPLEX,
                   1.0, 255, 1, cv.LINE_AA)
        cv.imshow('dst', dst)
        cv.waitKey()

    cv.destroyAllWindows()


def filter_bilateral():
    src = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    noise = np.zeros(src.shape, np.int32)
    cv.randn(noise, 0, 5)
    cv.add(src, noise, src, dtype=cv.CV_8UC1)

    dst1 = cv.GaussianBlur(src, (0, 0), 5)
    dst2 = cv.bilateralFilter(src, -1, 10, 5)
    
    cv.imshow('src', src)
    cv.imshow('dst1', dst1)
    cv.imshow('dst2', dst2)
    cv.waitKey()
    cv.destroyAllWindows()


def filter_median():
    src = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    for i in range(0, int(src.size / 10)):
        x = random.randint(0, src.shape[1] - 1)
        y = random.randint(0, src.shape[0] - 1)
        src[x, y] = (i % 2) * 255

    dst1 = cv.GaussianBlur(src, (0, 0), 1)
    dst2 = cv.medianBlur(src, 3)

    cv.imshow('src', src)
    cv.imshow('dst1', dst1)
    cv.imshow('dst2', dst2)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == '__main__':
    noise_gaussian()
    filter_bilateral()
    filter_median()
