# https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/  

import numpy as np
import cv2
from subprocess import call
import time
import os
import random 

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

not_run_yet = True
now = 0

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    
    if any(map(lambda x: any(x), faces)) and not_run_yet:
        now = time.time()
        print "Face(s) detected"
        cv2.imwrite("face.jpg", img)
        print "Image file written"
        # run email script 
        call(["python", "send_mail.py"])
	# run aws script
	call(["python", "upload_s3.py"])
        not_run_yet = False

    if time.time() - now > 15:
        not_run_yet = True
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
