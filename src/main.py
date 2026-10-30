from pyexpat import features

import numpy as np
import cv2 as cv


videoName = "SampleVideos/data1_7/7-gt.avi"
cascadeFileName = "data/haarcascade_frontalface_default.xml"


video = cv.VideoCapture(videoName)

face_cascade = cv.CascadeClassifier(cascadeFileName)






while video.isOpened():
    active, frame  = video.read()

    #break if end
    if not active:
        print("Video read error (Steam end?)...")
        break


    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)

    for (x,y,w,h) in faces:
        startPoint = (x,y)
        endPoint = (x+w, y+h)
        green = (0,255,0)
        cv.rectangle(frame, startPoint, endPoint, green, 2)
        features.pop


    print(faces)
    cv.imshow('frame',frame)


    #Exit press 'q'
    if cv.waitKey(1) == ord('q'):
        break
    #if cv.waitKey(1) == ord('esc'):
    #    break
video.release()
cv.destroyAllWindows()
