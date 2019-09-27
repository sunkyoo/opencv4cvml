import numpy as np
import cv2

def drawLines():
    img = np.full((400, 400, 3), 255, np.uint8)

    cv2.line(img, (50, 50), (200, 50), (0, 0, 255))
    cv2.line(img, (50, 100), (200, 100), (255, 0, 255), 3)
    cv2.line(img, (50, 150), (200, 150), (255, 0, 0), 10)

    cv2.line(img, (250, 50), (350, 100), (0, 0, 255), 1, cv2.LINE_4)
    cv2.line(img, (250, 70), (350, 120), (255, 0, 255), 1, cv2.LINE_8)
    cv2.line(img, (250, 90), (350, 140), (255, 0, 0), 1, cv2.LINE_AA)

    cv2.arrowedLine(img, (50, 200), (150, 200), (0, 0, 255), 1)
    cv2.arrowedLine(img, (50, 250), (350, 250), (255, 0, 255), 1)
    cv2.arrowedLine(img, (50, 300), (350, 300), (255, 0, 0), 1, cv2.LINE_8, 0, 0.05)

    cv2.drawMarker(img, (50, 350), (0, 0, 255), cv2.MARKER_CROSS)
    cv2.drawMarker(img, (100, 350), (0, 0, 255), cv2.MARKER_TILTED_CROSS)
    cv2.drawMarker(img, (150, 350), (0, 0, 255), cv2.MARKER_STAR)
    cv2.drawMarker(img, (200, 350), (0, 0, 255), cv2.MARKER_DIAMOND)
    cv2.drawMarker(img, (250, 350), (0, 0, 255), cv2.MARKER_SQUARE)
    cv2.drawMarker(img, (300, 350), (0, 0, 255), cv2.MARKER_TRIANGLE_UP)
    cv2.drawMarker(img, (350, 350), (0, 0, 255), cv2.MARKER_TRIANGLE_DOWN)

    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def drawPolys():
    img = np.full((400, 400, 3), 255, np.uint8)

    cv2.rectangle(img, (50, 50), (150, 100), (0, 0, 255), 2)
    cv2.rectangle(img, (50, 150), (150, 200), (0, 0, 128), -1)

    cv2.circle(img, (300, 120), 30, (255, 255, 0), -1, cv2.LINE_AA)
    cv2.circle(img, (300, 120), 60, (255, 0, 0), 3, cv2.LINE_AA)

    cv2.ellipse(img, (120, 300), (60, 30), 20, 0, 270, (255, 255, 0), cv2.FILLED, cv2.LINE_AA)
    cv2.ellipse(img, (120, 300), (100, 50), 20, 0, 360, (0, 255, 0), 2, cv2.LINE_AA)

    pts = np.array([[250, 250], [300, 250], [300, 300], [350, 300], [350, 350], [250, 350]])
    cv2.polylines(img, [pts], True, (255, 0, 255), 2)

    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def drawText1():
    img = np.full((500, 800, 3), 255, np.uint8)

    cv2.putText(img, "FONT_HERSHEY_SIMPLEX", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
    cv2.putText(img, "FONT_HERSHEY_PLAIN", (20, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
    cv2.putText(img, "FONT_HERSHEY_DUPLEX", (20, 150), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))
    cv2.putText(img, "FONT_HERSHEY_COMPLEX", (20, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
    cv2.putText(img, "FONT_HERSHEY_TRIPLEX", (20, 250), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0))
    cv2.putText(img, "FONT_HERSHEY_COMPLEX_SMALL", (20, 300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0))
    cv2.putText(img, "FONT_HERSHEY_SCRIPT_SIMPLEX", (20, 350), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 0, 255))
    cv2.putText(img, "FONT_HERSHEY_SCRIPT_COMPLEX", (20, 400), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 255))
    cv2.putText(img, "FONT_HERSHEY_COMPLEX | FONT_ITALIC", (20, 450), cv2.FONT_HERSHEY_COMPLEX | cv2.FONT_ITALIC, 1, (255, 0, 0))

    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def drawText2():
    img = np.full((200, 640, 3), 255, np.uint8)

    text = "Hello, OpenCV"
    fontFace = cv2.FONT_HERSHEY_TRIPLEX
    fontScale = 2.0
    thickness = 1

    sizeText, _ = cv2.getTextSize(text, fontFace, fontScale, thickness)

    org = ((img.shape[1] - sizeText[0]) // 2, (img.shape[0] + sizeText[1]) // 2)
    cv2.putText(img, text, org, fontFace, fontScale, (255, 0, 0), thickness)
    cv2.rectangle(img, org, (org[0] + sizeText[0], org[1] - sizeText[1]), (0, 255, 0), 1)

    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    drawLines()
    drawPolys()
    drawText1()
    drawText2()
