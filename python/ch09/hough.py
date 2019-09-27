import numpy as np
import cv2
import math


def hough_lines():
    src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    edge = cv2.Canny(src, 50, 150)
    lines = cv2.HoughLines(edge, 1, math.pi / 180, 250)

    dst = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

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
            cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


def hough_line_segments():
    src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    edge = cv2.Canny(src, 50, 150)
    lines = cv2.HoughLinesP(edge, 1, math.pi / 180, 160, minLineLength=50, maxLineGap=5)

    dst = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    if lines is not None:
        for i in range(lines.shape[0]):
            pt1 = (lines[i][0][0], lines[i][0][1])
            pt2 = (lines[i][0][2], lines[i][0][3])
            cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


def hough_circles():
    src = cv2.imread('coins.png', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    blurred = cv2.blur(src, (3, 3))
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 50,
                              param1=150, param2=30)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = circles[0][i]
            cv2.circle(dst, (cx, cy), radius, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    hough_lines()
    hough_line_segments()
    hough_circles()
