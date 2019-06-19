import numpy as np
import cv2 as cv


def mask_setTo():
    src = cv.imread('lenna.bmp', cv.IMREAD_COLOR)
    mask = cv.imread('mask_smile.bmp', cv.IMREAD_GRAYSCALE)

    if src is None or mask is None:
        print('Image load failed!')
        return

    src[mask > 0] = (0, 255, 255)

    cv.imshow('src', src)
    cv.imshow('mask', mask)
    cv.waitKey()
    cv.destroyAllWindows()


def mask_copyTo():
    src = cv.imread('airplane.bmp', cv.IMREAD_COLOR)
    mask = cv.imread('mask_plane.bmp', cv.IMREAD_GRAYSCALE)
    dst = cv.imread('field.bmp', cv.IMREAD_COLOR)

    if src is None or mask is None or dst is None:
        print('Image load failed!')
        return

    dst[mask > 0] = src[mask > 0]

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.imshow('mask', mask)
    cv.waitKey()
    cv.destroyAllWindows()


def time_inverse():
    src = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    dst = np.empty(src.shape, dtype=src.dtype)

    tm = cv.TickMeter()
    tm.start()

    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = 255 - src[y, x]

    tm.stop()
    print('Image inverse implementation took %4.3f ms.' % tm.getTimeMilli())

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def useful_func():
    img = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

    if img is None:
        print('Image load failed!')
        return

    sum_img = np.sum(img)
    mean_img = np.mean(img, dtype=np.int32)
    print('Sum:', sum_img)
    print('Mean:', mean_img)

    minVal, maxVal, minPos, maxPos = cv.minMaxLoc(img)
    print('minVal is', minVal, 'at', minPos)
    print('maxVal is', maxVal, 'at', maxPos)

    src = np.array([[-1, -0.5, 0, 0.5, 1]], dtype=np.float32)
    dst = cv.normalize(src, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    print('src:', src)
    print('dst:', dst)

    print('round(2.5) is', round(2.5))
    print('round(2.51) is', round(2.51))
    print('round(3.499) is', round(3.499))
    print('round(3.5) is', round(3.5))


if __name__ == '__main__':
    mask_setTo()
    mask_copyTo()
    time_inverse()
    useful_func()
