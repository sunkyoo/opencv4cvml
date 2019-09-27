import numpy as np
import cv2


src = cv2.imread('box_in_scene.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    exit()

orb = cv2.ORB_create()

keypoints = orb.detect(src)
keypoints, desc = orb.compute(src, keypoints)

print('len(keypoints):', len(keypoints))
print('desc.shape:', desc.shape)

dst = cv2.drawKeypoints(src, keypoints, None, (-1, -1, -1),
                       cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()
