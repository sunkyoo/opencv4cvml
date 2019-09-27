import numpy as np
import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Video open failed!')
    exit()

detector = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()

    if not ret:
        print('Frame load failed!')
        break

    info, points, _ = detector.detectAndDecode(frame)

    if points is not None:
        points = np.array(points, dtype=np.int32).reshape(4, 2)
        cv2.polylines(frame, [points], True, (0, 0, 255), 2)

    if len(info) > 0:
        cv2.putText(frame, info, (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), lineType=cv2.LINE_AA)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
