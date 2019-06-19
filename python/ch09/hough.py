import numpy as np
import cv2 as cv
import math


def hough_lines():
    src = cv.imread('building.jpg', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    edge = cv.Canny(src, 50, 150)
    lines = cv.HoughLines(edge, 1, math.pi / 180, 250)

    dst = cv.cvtColor(edge, cv.COLOR_GRAY2BGR)

    if lines is not None:
        for i in range(lines.shape[0]):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            cos_t = math.cos(theta)
            sin_t = math.sin(theta)
            x0, y0 = rho * cos_t, rho * sin_t
            alpha = 1000
            pt1 = (int(x0 - alpha * sin_t), int(y0 + alpha * cos_t))
            pt2 = (int(x0 + alpha * sin_t), int(y0 - alpha * cos_t))
            cv.line(dst, pt1, pt2, (0, 0, 255), 2, cv.LINE_AA)

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def hough_line_segments():
    src = cv.imread('building.jpg', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    edge = cv.Canny(src, 50, 150)
    lines = cv.HoughLinesP(edge, 1, math.pi / 180, 160, minLineLength=50, maxLineGap=5)

    dst = cv.cvtColor(edge, cv.COLOR_GRAY2BGR)

    if lines is not None:
        for i in range(lines.shape[0]):
            pt1 = (lines[i][0][0], lines[i][0][1])
            pt2 = (lines[i][0][2], lines[i][0][3])
            cv.line(dst, pt1, pt2, (0, 0, 255), 2, cv.LINE_AA)

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def hough_circles():
    src = cv.imread('coins.png', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    blurred = cv.blur(src, (3, 3))
    circles = cv.HoughCircles(blurred, cv.HOUGH_GRADIENT, 1, 50,
                              param1=150, param2=30)

    dst = cv.cvtColor(src, cv.COLOR_GRAY2BGR)

    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = circles[0][i]
            cv.circle(dst, (cx, cy), radius, (0, 0, 255), 2, cv.LINE_AA)

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == '__main__':
    hough_lines()
    hough_line_segments()
    hough_circles()
