import numpy as np
import cv2 as cv
import math


def setLabel(img, pts, label):
    (x, y, w, h) = cv.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv.putText(img, label, pt1, cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))


def main():
    img = cv.imread('polygon.bmp', cv.IMREAD_COLOR)

    if img is None:
        print('Image load failed!')
        return

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, img_bin = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    contours, _ = cv.findContours(img_bin, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    for pts in contours:
        if cv.contourArea(pts) < 400:
            continue

        approx = cv.approxPolyDP(pts, cv.arcLength(pts, True)*0.02, True)

        vtc = len(approx)

        if vtc == 3:
            setLabel(img, pts, 'TRI')
        elif vtc == 4:
            setLabel(img, pts, 'RECT')
        else:
            lenth = cv.arcLength(pts, True)
            area = cv.contourArea(pts)
            ratio = 4. * math.pi * area / (lenth * lenth)

            if ratio > 0.85:
                setLabel(img, pts, 'CIR')

    cv.imshow('img', img)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
