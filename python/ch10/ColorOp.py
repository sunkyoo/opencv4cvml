import numpy as np
import cv2 as cv


def color_op():
    src = cv.imread('butterfly.jpg', cv.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return

    print('src.shape:', src.shape)
    print('src.dtype:', src.dtype)

    # b, g, r = src[0, 0]
    print('The pixel value [B, G, R] at (0, 0) is', src[0, 0])


def color_inverse():
    src = cv.imread('butterfly.jpg', cv.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return

    dst = np.zeros(src.shape, src.dtype)

    for j in range(src.shape[0]):
        for i in range(src.shape[1]):
            p1 = src[j, i]
            p2 = dst[j, i]

            p2[0] = 255 - p1[0]
            p2[1] = 255 - p1[1]
            p2[2] = 255 - p1[2]

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def color_grayscale():
    src = cv.imread('butterfly.jpg', cv.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return

    dst = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def color_split():
    src = cv.imread('candies.png', cv.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return

    # b_plane, g_plane, r_plane = cv.split(src)
    bgr_planes = cv.split(src)

    cv.imshow('src', src)
    cv.imshow('B_plane', bgr_planes[0])
    cv.imshow('G_plane', bgr_planes[1])
    cv.imshow('R_plane', bgr_planes[2])
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == '__main__':
    color_op()
    color_inverse()
    color_grayscale()
    color_split()
