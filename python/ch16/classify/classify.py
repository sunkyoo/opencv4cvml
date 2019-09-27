import numpy as np
import cv2
import sys


filename = 'space_shuttle.jpg'

if len(sys.argv) > 1:
    filename = sys.argv[1]

img = cv2.imread(filename)

if img is None:
    print('Image load failed!')
    exit()

# Load network

net = cv2.dnn.readNet('bvlc_googlenet.caffemodel', 'deploy.prototxt')

if net.empty():
    print('Network load failed!')
    exit()

# Load class names

classNames = None
with open('classification_classes_ILSVRC2012.txt', 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Inference

inputBlob = cv2.dnn.blobFromImage(img, 1, (224, 224), (104, 117, 123))
net.setInput(inputBlob, 'data')
prob = net.forward()

# Check results & Display

out = prob.flatten()
classId = np.argmax(out)
confidence = out[classId]

str = '%s (%4.2f%%)' % (classNames[classId], confidence * 100)
cv2.putText(img, str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
