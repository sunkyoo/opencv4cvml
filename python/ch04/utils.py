import numpy as np
import cv2


def mask_setTo():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)
    mask = cv2.imread('mask_smile.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None or mask is None:
        print('Image load failed!')
        return

    src[mask > 0] = (0, 255, 255)

    cv2.imshow('src', src)
    cv2.imshow('mask', mask)
    cv2.waitKey()
    cv2.destroyAllWindows()


def mask_copyTo():
    src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
    mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
    dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

    if src is None or mask is None or dst is None:
        print('Image load failed!')
        return

    cv2.copyTo(src, mask, dst)
    # dst[mask > 0] = src[mask > 0]

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.imshow('mask', mask)
    cv2.waitKey()
    cv2.destroyAllWindows()


def time_inverse():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    dst = np.empty(src.shape, dtype=src.dtype)

    tm = cv2.TickMeter()
    tm.start()

    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = 255 - src[y, x]

    tm.stop()
    print('Image inverse implementation took %4.3f ms.' % tm.getTimeMilli())

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


def useful_func():
    img = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if img is None:
        print('Image load failed!')
        return

    sum_img = np.sum(img)
    mean_img = np.mean(img, dtype=np.int32)
    print('Sum:', sum_img)
    print('Mean:', mean_img)

    minVal, maxVal, minPos, maxPos = cv2.minMaxLoc(img)
    print('minVal is', minVal, 'at', minPos)
    print('maxVal is', maxVal, 'at', maxPos)

    src = np.array([[-1, -0.5, 0, 0.5, 1]], dtype=np.float32)
    dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
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
