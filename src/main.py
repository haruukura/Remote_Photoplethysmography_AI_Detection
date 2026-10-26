import numpy as np
import cv2 as cv


videoName = "SampleVideos/data1_7/7-gt.avi"
cascadeFileName = "data/haarcascade_frontalface_default.xml"


video = cv.VideoCapture(videoName)

cv.CascadeClassifier(cascadeFileName)






while video.isOpened():
    active, frame  = video.read()

    #break if end
    if not active:
        print("Video read error (Steam end?)...")
        break


    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiscale(gray, scaleFactor = 1, minNeighboors = 5)

    print(faces)
    cv.imshow('frame',frame)


    #Exit press 'q'
    if cv.waitKey(1) == ord('q'):
        break

video.release()
cv.destroyAllWindows
