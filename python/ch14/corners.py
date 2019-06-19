import numpy as np
import cv2 as cv


def corner_harris():
    src = cv.imread('building.jpg', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    harris = cv.cornerHarris(src, 3, 3, 0.04)
    harris_norm = cv.normalize(harris, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

    dst = cv.cvtColor(src, cv.COLOR_GRAY2BGR)

    for y in range(harris_norm.shape[0]):
        for x in range(harris_norm.shape[1]):
            if harris_norm[y, x] > 120:
                if (harris[y, x] > harris[y-1, x] and
                        harris[y, x] > harris[y-1, x] and
                        harris[y, x] > harris[y-1, x] and
                        harris[y, x] > harris[y-1, x]):
                    cv.circle(dst, (x, y), 5, (0, 0, 255), 2)

    cv.imshow('src', src)
    cv.imshow('harris_norm', harris_norm)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def corner_fast():
    src = cv.imread('building.jpg', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    fast = cv.FastFeatureDetector_create(60)
    keypoints = fast.detect(src)

    dst = cv.cvtColor(src, cv.COLOR_GRAY2BGR)

    for kp in keypoints:
        pt = (int(kp.pt[0]), int(kp.pt[1]))
        cv.circle(dst, pt, 5, (0, 0, 255), 2)

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == "__main__":
    corner_harris()
    corner_fast()
