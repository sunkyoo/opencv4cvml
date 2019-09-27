import numpy as np
import cv2


def on_mouse(event, x, y, flags, param):
    global cnt, src_pts
    if event == cv2.EVENT_LBUTTONDOWN:
        if cnt < 4:
            src_pts[cnt, :] = np.array([x, y]).astype(np.float32)
            cnt += 1

            cv2.circle(src, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow('src', src)
        
        if cnt == 4:
            w = 200
            h = 300

            dst_pts = np.array([[0, 0],
                                [w - 1, 0],
                                [w - 1, h - 1],
                                [0, h - 1]]).astype(np.float32)

            pers_mat = cv2.getPerspectiveTransform(src_pts, dst_pts)

            dst = cv2.warpPerspective(src, pers_mat, (w, h))

            cv2.imshow('dst', dst)


cnt = 0
src_pts = np.zeros([4, 2], dtype=np.float32)
src = cv2.imread('card.bmp')

if src is None:
    print('Image load failed!')
    exit()

cv2.namedWindow('src')
cv2.setMouseCallback('src', on_mouse)

cv2.imshow('src', src)
cv2.waitKey(0)
cv2.destroyAllWindows()
