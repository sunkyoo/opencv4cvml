import numpy as np
import cv2


train = []
label = []
k_value = 1


def on_k_changed(pos):
    global k_value

    k_value = pos
    if k_value < 1:
        k_value = 1

    trainAndDisplay()


def addPoint(x, y, c):
    train.append([x, y])
    label.append([c])


def trainAndDisplay():
    train_array = np.array(train).astype(np.float32)
    label_array = np.array(label)
    knn.train(train_array, cv2.ml.ROW_SAMPLE, label_array)

    for j in range(img.shape[0]):
        for i in range(img.shape[1]):
            sample = np.array([[i, j]]).astype(np.float32)

            ret, res, _, _ = knn.findNearest(sample, k_value)

            response = int(res[0, 0])
            if response == 0:
                img[j, i] = (128, 128, 255)
            elif response == 1:
                img[j, i] = (128, 255, 128)
            elif response == 2:
                img[j, i] = (255, 128, 128)

    for i in range(len(train)):
        x, y = train[i]
        l = label[i][0]

        if l == 0:
            cv2.circle(img, (x, y), 5, (0, 0, 128), -1, cv2.LINE_AA)
        elif l == 1:
            cv2.circle(img, (x, y), 5, (0, 128, 0), -1, cv2.LINE_AA)
        elif l == 2:
            cv2.circle(img, (x, y), 5, (128, 0, 0), -1, cv2.LINE_AA)

    cv2.imshow('knn', img)


img = np.zeros((500, 500, 3), np.uint8)
knn = cv2.ml.KNearest_create()

cv2.namedWindow('knn')
cv2.createTrackbar('k_value', 'knn', k_value, 5, on_k_changed)

NUM = 30
rn = np.zeros((NUM, 2), np.int32)

cv2.randn(rn, 0, 50)
for i in range(NUM):
    addPoint(rn[i, 0] + 150, rn[i, 1] + 150, 0)

cv2.randn(rn, 0, 50)
for i in range(NUM):
    addPoint(rn[i, 0] + 350, rn[i, 1] + 150, 1)

cv2.randn(rn, 0, 70)
for i in range(NUM):
    addPoint(rn[i, 0] + 250, rn[i, 1] + 400, 2)

trainAndDisplay()

cv2.imshow('knn', img)
cv2.waitKey()
cv2.destroyAllWindows()
