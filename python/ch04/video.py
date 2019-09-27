import numpy as np
import cv2


def camera_in():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera open failed!")
        exit()

    print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        inversed = ~frame

        cv2.imshow('frame', frame)
        cv2.imshow('inversed', inversed)

        if cv2.waitKey(10) == 27:
            break

    cv2.destroyAllWindows()


def video_in():
    cap = cv2.VideoCapture('stopwatch.avi')

    if not cap.isOpened():
        print("Video open failed!")
        exit()

    print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('Frame count:', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

    fps = cap.get(cv2.CAP_PROP_FPS)
    print('FPS:', fps)

    delay = round(1000 / fps)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        inversed = ~frame

        cv2.imshow('frame', frame)
        cv2.imshow('inversed', inversed)

        if cv2.waitKey(delay) == 27:
            break

    cv2.destroyAllWindows()


def camera_in_video_out():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera open failed!")
        exit()

    w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    delay = round(1000 / fps)

    outputVideo = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

    if not outputVideo.isOpened():
        print('File open failed!')
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        inversed = ~frame

        outputVideo.write(inversed)

        cv2.imshow('frame', frame)
        cv2.imshow('inversed', inversed)

        if cv2.waitKey(delay) == 27:
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    camera_in()
    video_in()
    camera_in_video_out()
