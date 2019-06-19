import numpy as np
import cv2 as cv


def affine_transform():
    src = cv.imread('tekapo.bmp')

    if src is None:
        print('Image load failed!')
        return

    rows = src.shape[0]
    cols = src.shape[1]

    src_pts = np.array([[0, 0],
                        [cols - 1, 0],
                        [cols - 1, rows - 1]]).astype(np.float32)
    dst_pts = np.array([[50, 50],
                        [cols - 100, 100],
                        [cols - 50, rows - 50]]).astype(np.float32)

    affine_mat = cv.getAffineTransform(src_pts, dst_pts)

    dst = cv.warpAffine(src, affine_mat, (0, 0))

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def affine_translation():
    src = cv.imread('tekapo.bmp')

    if src is None:
        print('Image load failed!')
        return

    affine_mat = np.array([[1, 0, 150],
                           [0, 1, 100]]).astype(np.float32)

    dst = cv.warpAffine(src, affine_mat, (0, 0))

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def affine_shear():
    src = cv.imread('tekapo.bmp')

    if src is None:
        print('Image load failed!')
        return

    rows = src.shape[0]
    cols = src.shape[1]

    mx = 0.3
    affine_mat = np.array([[1, mx, 0],
                           [0, 1, 0]]).astype(np.float32)

    dst = cv.warpAffine(src, affine_mat, (int(cols + rows * mx), rows))

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def affine_scale():
    src = cv.imread('rose.bmp')

    if src is None:
        print('Image load failed!')
        return

    dst1 = cv.resize(src, (0, 0), fx=4, fy=4, interpolation=cv.INTER_NEAREST)
    dst2 = cv.resize(src, (1920, 1280))
    dst3 = cv.resize(src, (1920, 1280), interpolation=cv.INTER_CUBIC)
    dst4 = cv.resize(src, (1920, 1280), interpolation=cv.INTER_LANCZOS4)

    cv.imshow('src', src)
    cv.imshow('dst1', dst1[400:800, 500:900])
    cv.imshow('dst2', dst2[400:800, 500:900])
    cv.imshow('dst3', dst3[400:800, 500:900])
    cv.imshow('dst4', dst4[400:800, 500:900])
    cv.waitKey()
    cv.destroyAllWindows()


def affine_rotation():
    src = cv.imread('tekapo.bmp')

    if src is None:
        print('Image load failed!')
        return

    cp = (src.shape[1] / 2, src.shape[0] / 2)
    affine_mat = cv.getRotationMatrix2D(cp, 20, 1)

    dst = cv.warpAffine(src, affine_mat, (0, 0))

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def affine_flip():
    src = cv.imread('eastsea.bmp')

    if src is None:
        print('Image load failed!')
        return

    cv.imshow('src', src)

    for flip_code in [1, 0, -1]:
        dst = cv.flip(src, flip_code)

        desc = 'flipCode: %d' % flip_code
        cv.putText(dst, desc, (10, 30), cv.FONT_HERSHEY_SIMPLEX,
                   1.0, (255, 0, 0), 1, cv.LINE_AA)

        cv.imshow('dst', dst)
        cv.waitKey()

    cv.destroyAllWindows()


if __name__ == '__main__':
    affine_transform()
    affine_translation()
    affine_shear()
    affine_scale()
    affine_rotation()
    affine_flip()
