import cv2
import numpy as np
cap=cv2.VideoCapture(0)
lower=np.array([90,100,20])
upper=np.array([132,255,255])
while True:
    ret,frame=cap.read()
    image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(image,lower,upper)
    contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours)!=0:
        for contour in contours:
            if cv2.contourArea(contour)>500:
               x,y,w,h=cv2.boundingRect(contour)
               cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',image)
    cv2.waitKey(1) 
