import numpy as np
import cv2 as cv


src = cv.imread('box_in_scene.png', cv.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    exit()

orb = cv.ORB_create()

keypoints = orb.detect(src)
keypoints, desc = orb.compute(src, keypoints)

print('len(keypoints):', len(keypoints))
print('desc.shape:', desc.shape)

dst = cv.drawKeypoints(src, keypoints, None, (-1, -1, -1),
                       cv.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

cv.imshow('src', src)
cv.imshow('dst', dst)

cv.waitKey()
cv.destroyAllWindows()
