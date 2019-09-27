import numpy as np
import cv2


src = cv2.imread('pepper.bmp', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

ycrcb_planes = cv2.split(src_ycrcb)

ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0])

dst_ycrcb = cv2.merge(ycrcb_planes)

dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
