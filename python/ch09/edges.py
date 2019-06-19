import numpy as np
import cv2 as cv


def sobel_derivative():
    src = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    mx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]], dtype=np.float32)
    my = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]], dtype=np.float32)

    dx = cv.filter2D(src, -1, mx, delta=128)
    dy = cv.filter2D(src, -1, my, delta=128)

    cv.imshow('src', src)
    cv.imshow('dx', dx)
    cv.imshow('dy', dy)
    cv.waitKey()
    cv.destroyAllWindows()


def sobel_edge():
    src = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    dx = cv.Sobel(src, cv.CV_32F, 1, 0)
    dy = cv.Sobel(src, cv.CV_32F, 0, 1)

    fmag = cv.magnitude(dx, dy)
    mag = np.uint8(np.clip(fmag, 0, 255))
    _, edge = cv.threshold(mag, 150, 255, cv.THRESH_BINARY)

    cv.imshow('src', src)
    cv.imshow('mag', mag)
    cv.imshow('edge', edge)
    cv.waitKey()
    cv.destroyAllWindows()


def canny_edge():
    src = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    dst1 = cv.Canny(src, 50, 100)
    dst2 = cv.Canny(src, 50, 150)

    cv.imshow('src', src)
    cv.imshow('dst1', dst1)
    cv.imshow('dst2', dst2)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == '__main__':
    sobel_derivative()
    sobel_edge()
    canny_edge()
