import numpy as np
import cv2 as cv


def keypoint_matching():
    src1 = cv.imread('box.png', cv.IMREAD_GRAYSCALE)
    src2 = cv.imread('box_in_scene.png', cv.IMREAD_GRAYSCALE)

    if src1 is None or src2 is None:
        print('Image load failed!')
        return

    orb = cv.ORB_create()

    keypoints1, desc1 = orb.detectAndCompute(src1, None)
    keypoints2, desc2 = orb.detectAndCompute(src2, None)
    print('desc1.shape:', desc1.shape)
    print('desc2.shape:', desc2.shape)

    matcher = cv.BFMatcher_create(cv.NORM_HAMMING)
    matches = matcher.match(desc1, desc2)

    dst = cv.drawMatches(src1, keypoints1, src2, keypoints2, matches, None)

    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def good_matching():
    src1 = cv.imread('box.png', cv.IMREAD_GRAYSCALE)
    src2 = cv.imread('box_in_scene.png', cv.IMREAD_GRAYSCALE)

    if src1 is None or src2 is None:
        print('Image load failed!')
        return

    orb = cv.ORB_create()

    keypoints1, desc1 = orb.detectAndCompute(src1, None)
    keypoints2, desc2 = orb.detectAndCompute(src2, None)

    matcher = cv.BFMatcher_create(cv.NORM_HAMMING)
    matches = matcher.match(desc1, desc2)

    matches = sorted(matches, key=lambda x: x.distance)
    good_matches = matches[:50]

    dst = cv.drawMatches(src1, keypoints1, src2, keypoints2, good_matches, None,
                         flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def find_homography():
    src1 = cv.imread('box.png', cv.IMREAD_GRAYSCALE)
    src2 = cv.imread('box_in_scene.png', cv.IMREAD_GRAYSCALE)

    if src1 is None or src2 is None:
        print('Image load failed!')
        return

    orb = cv.ORB_create()

    keypoints1, desc1 = orb.detectAndCompute(src1, None)
    keypoints2, desc2 = orb.detectAndCompute(src2, None)

    matcher = cv.BFMatcher_create(cv.NORM_HAMMING)
    matches = matcher.match(desc1, desc2)

    matches = sorted(matches, key=lambda x: x.distance)
    good_matches = matches[:50]

    dst = cv.drawMatches(src1, keypoints1, src2, keypoints2, good_matches, None,
                         flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    pts1 = np.array([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2).astype(np.float32)
    pts2 = np.array([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2).astype(np.float32)

    H, _ = cv.findHomography(pts1, pts2, cv.RANSAC)

    (h, w) = src1.shape[:2]
    corners1 = np.array([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2).astype(np.float32)
    corners2 = cv.perspectiveTransform(corners1, H)
    corners2 = corners2 + np.float32([w, 0])

    cv.polylines(dst, [np.int32(corners2)], True, (0, 255, 0), 2, cv.LINE_AA)

    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == '__main__':
    keypoint_matching()
    good_matching()
    find_homography()
