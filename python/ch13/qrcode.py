import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('Video open failed!')
    exit()

detector = cv.QRCodeDetector()

while True:
    ret, frame = cap.read()

    if not ret:
        print('Frame load failed!')
        break

    info, points, _ = detector.detectAndDecode(frame)

    if points is not None:
        points = np.array(points, dtype=np.int32).reshape(4, 2)
        cv.polylines(frame, [points], True, (0, 0, 255), 2)

    if len(info) > 0:
        cv.putText(frame, info, (10, 30), cv.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), lineType=cv.LINE_AA)

    cv.imshow('frame', frame)
    if cv.waitKey(1) == 27:
        break

cv.destroyAllWindows()
