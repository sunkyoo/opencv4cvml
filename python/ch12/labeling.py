import numpy as np
import cv2 as cv


def labeling_basic():
    src = np.array([[0, 0, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0, 0, 1, 0],
                    [1, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 1, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]).astype(np.uint8)

    src = src * 255

    cnt, labels = cv.connectedComponents(src)

    print('src:'), 
    print(src)
    print('labels:')
    print(labels)
    print('number of labels:', cnt)


def labeling_stats():
    src = cv.imread('keyboard.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    _, src_bin = cv.threshold(src, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

    cnt, labels, stats, centroids = cv.connectedComponentsWithStats(src_bin)

    dst = cv.cvtColor(src, cv.COLOR_GRAY2BGR)

    for i in range(1, cnt):
        (x, y, w, h, area) = stats[i]

        if area < 20:
            continue

        pt1 = (x, y)
        pt2 = (x + w, y + h)
        cv.rectangle(dst, pt1, pt2, (0, 255, 255))

    cv.imshow('src', src)
    cv.imshow('dst', dst)

    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == "__main__":
    labeling_basic()
    labeling_stats()
