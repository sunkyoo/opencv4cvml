import numpy as np
import cv2 as cv


def on_hue_changed(_=None):
    lower_hue = cv.getTrackbarPos('Lower Hue', 'mask')
    upper_hue = cv.getTrackbarPos('Upper Hue', 'mask')

    lowerb = (lower_hue, 100, 0)
    upperb = (upper_hue, 255, 255)
    mask = cv.inRange(src_hsv, lowerb, upperb)

    cv.imshow('mask', mask)


def main():
    global src_hsv

    src = cv.imread('candies.png', cv.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return

    src_hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)

    cv.imshow('src', src)

    cv.namedWindow('mask')
    cv.createTrackbar('Lower Hue', 'mask', 40, 179, on_hue_changed)
    cv.createTrackbar('Upper Hue', 'mask', 80, 179, on_hue_changed)
    on_hue_changed(0)

    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
