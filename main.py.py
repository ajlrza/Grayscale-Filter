import numpy as np
import cv2 as cv

cam = cv.VideoCapture(0)

def imageToGray(frame):
    image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    return image

if not cam.isOpened():
    print("Cannot open camera")

grayscale_active = False

while cam.isOpened() is True:

    ret, frame = cam.read()
    key_listen = cv.waitKey(35) & 0xFF

    if ret:

        if key_listen == ord('c'):
            cam.release()

        if grayscale_active is False:
             cv.imshow("TEST", frame)
             if key_listen == ord('g'):
                 grayscale_active = True
        if grayscale_active is True:
            cv.imshow("TEST", imageToGray(frame))
            if key_listen == ord('f'):
                 grayscale_active = False

