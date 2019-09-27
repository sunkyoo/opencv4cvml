import numpy as np
import cv2


train = np.array([[150, 200], [200, 250],
                  [100, 250], [150, 300],
                  [350, 100], [400, 200],
                  [400, 300], [350, 400]]).astype(np.float32)

label = np.array([0, 0, 0, 0, 1, 1, 1, 1])

svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_RBF)
# svm.setKernel(cv2.ml.SVM_LINEAR)
svm.trainAuto(train, cv2.ml.ROW_SAMPLE, label)

img = np.zeros((500, 500, 3), np.uint8)

for j in range(img.shape[0]):
    for i in range(img.shape[1]):
        test = np.array([[i, j]], dtype=np.float32)
        _, res = svm.predict(test)

        if res == 0:
            img[j, i] = (128, 128, 255)
        elif res == 1:
            img[j, i] = (128, 255, 128)

color = [(0, 0, 128), (0, 128, 0)]

for i in range(train.shape[0]):
    x = train[i, 0]
    y = train[i, 1]
    l = label[i]

    cv2.circle(img, (x, y), 5, color[l], -1, cv2.LINE_AA)

cv2.imshow('svm', img)
cv2.waitKey()
cv2.destroyAllWindows()
