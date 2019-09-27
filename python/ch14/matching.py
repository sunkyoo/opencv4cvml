import numpy as np
import cv2


def keypoint_matching():
    src1 = cv2.imread('box.png', cv2.IMREAD_GRAYSCALE)
    src2 = cv2.imread('box_in_scene.png', cv2.IMREAD_GRAYSCALE)

    if src1 is None or src2 is None:
        print('Image load failed!')
        return

    orb = cv2.ORB_create()

    keypoints1, desc1 = orb.detectAndCompute(src1, None)
    keypoints2, desc2 = orb.detectAndCompute(src2, None)
    print('desc1.shape:', desc1.shape)
    print('desc2.shape:', desc2.shape)

    matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING)
    matches = matcher.match(desc1, desc2)

    dst = cv2.drawMatches(src1, keypoints1, src2, keypoints2, matches, None)

    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


def good_matching():
    src1 = cv2.imread('box.png', cv2.IMREAD_GRAYSCALE)
    src2 = cv2.imread('box_in_scene.png', cv2.IMREAD_GRAYSCALE)

    if src1 is None or src2 is None:
        print('Image load failed!')
        return

    orb = cv2.ORB_create()

    keypoints1, desc1 = orb.detectAndCompute(src1, None)
    keypoints2, desc2 = orb.detectAndCompute(src2, None)

    matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING)
    matches = matcher.match(desc1, desc2)

    matches = sorted(matches, key=lambda x: x.distance)
    good_matches = matches[:50]

    dst = cv2.drawMatches(src1, keypoints1, src2, keypoints2, good_matches, None,
                         flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


def find_homography():
    src1 = cv2.imread('box.png', cv2.IMREAD_GRAYSCALE)
    src2 = cv2.imread('box_in_scene.png', cv2.IMREAD_GRAYSCALE)

    if src1 is None or src2 is None:
        print('Image load failed!')
        return

    orb = cv2.ORB_create()

    keypoints1, desc1 = orb.detectAndCompute(src1, None)
    keypoints2, desc2 = orb.detectAndCompute(src2, None)

    matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING)
    matches = matcher.match(desc1, desc2)

    matches = sorted(matches, key=lambda x: x.distance)
    good_matches = matches[:50]

    dst = cv2.drawMatches(src1, keypoints1, src2, keypoints2, good_matches, None,
                         flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    pts1 = np.array([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2).astype(np.float32)
    pts2 = np.array([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2).astype(np.float32)

    H, _ = cv2.findHomography(pts1, pts2, cv2.RANSAC)

    (h, w) = src1.shape[:2]
    corners1 = np.array([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2).astype(np.float32)
    corners2 = cv2.perspectiveTransform(corners1, H)
    corners2 = corners2 + np.float32([w, 0])

    cv2.polylines(dst, [np.int32(corners2)], True, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    keypoint_matching()
    good_matching()
    find_homography()
