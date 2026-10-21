import numpy as np
import cv2 as cv


videoName = "SampleVideos/data1_7/7-gt.avi"
video = cv.VideoCapture(videoName)

while video.isOpened():
    active, frame  = video.read()

    if not active:
        print("Video read error (Steam end?)...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BRR2GRAY)

    cv.imshow('frame',gray)

    if cv.waitKey(1) == ord('q'):
        break

video.realease()
cv.destoryAllWindows
