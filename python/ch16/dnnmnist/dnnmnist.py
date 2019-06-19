import numpy as np
import cv2 as cv


oldx, oldy = -1, -1

def on_mouse(event, x, y, flags, _):
    global oldx, oldy

    if event == cv.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y

    elif event == cv.EVENT_LBUTTONUP:
        oldx, oldy = -1, -1

    elif event == cv.EVENT_MOUSEMOVE:
        if flags & cv.EVENT_FLAG_LBUTTON:
            cv.line(img, (oldx, oldy), (x, y), (255, 255, 255), 40, cv.LINE_AA)
            oldx, oldy = x, y
            cv.imshow('img', img)


net = cv.dnn.readNet('mnist_cnn.pb')

if net.empty():
    print('Network load failed!')
    exit()

img = np.zeros((400, 400), np.uint8)

cv.imshow('img', img)
cv.setMouseCallback('img', on_mouse)

while True:
    c = cv.waitKey()

    if c == 27:
        break
    elif c == ord(' '):
        blob = cv.dnn.blobFromImage(img, 1/255., (28, 28))
        net.setInput(blob)
        prob = net.forward()

        _, maxVal, _, maxLoc = cv.minMaxLoc(prob)
        digit = maxLoc[0]

        print('%d (%f)' % (digit, maxVal * 100))

        img.fill(0)
        cv.imshow('img', img)

cv.destroyAllWindows()
