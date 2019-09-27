import numpy as np
import cv2


def calcGrayHist(img):
    channels = [0]
    histSize = [256]
    histRange = [0, 256]

    hist = cv2.calcHist([img], channels, None, histSize, histRange)

    return hist


def getGrayHistImage(hist):
    _, histMax, _, _ = cv2.minMaxLoc(hist)

    imgHist = np.ones((100, 256), np.uint8) * 255
    for x in range(imgHist.shape[1]):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist


def histgoram_stretching():
    src = cv2.imread('hawkes.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    gmin, gmax, _, _ = cv2.minMaxLoc(src)

    dst = cv2.convertScaleAbs(src, alpha=255.0/(gmax - gmin), beta=-gmin * 255.0/(gmax - gmin))

    cv2.imshow('src', src)
    cv2.imshow('srcHist', getGrayHistImage(calcGrayHist(src)))

    cv2.imshow('dst', dst)
    cv2.imshow('dstHist', getGrayHistImage(calcGrayHist(dst)))

    cv2.waitKey()
    cv2.destroyAllWindows()


def histgoram_equalization():
    src = cv2.imread('hawkes.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    dst = cv2.equalizeHist(src)

    cv2.imshow('src', src)
    cv2.imshow('srcHist', getGrayHistImage(calcGrayHist(src)))

    cv2.imshow('dst', dst)
    cv2.imshow('dstHist', getGrayHistImage(calcGrayHist(dst)))

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    histgoram_stretching()
    histgoram_equalization()
