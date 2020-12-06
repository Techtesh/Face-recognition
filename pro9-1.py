# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:12:50 2020

@author: Hitesh
"""


import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

name=1


while name<97:
    path='data/'+str(name)+'.jpg'
    pathsave='op1resize/'+str(name)+'.jpg'
    pathsave2='op2/'+str(name)+'.jpg'
    print(name)
    name=name+1
    img=cv2.imread(path)
    width=480
    scale=img.shape[0]/480
    height=int(img.shape[1]/scale)
    img=cv2.resize(img,(width,height),interpolation = cv2.INTER_AREA)
    
    #cv2.imshow("",img)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces =face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h)in faces:
        
        print("face",x,y,w,h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_color=img[y:y+h,x:x+w]
        roi_gray=gray[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (x2,y2,w2,h2)in eyes:
            print("eye",x+x2,y+y2)
            #cv2.rectangle(roi_color,(x2,y2),(x2+w2,y2+h2),(0,255,0),2)
        
         
        cv2.imwrite(pathsave2,roi_color) 
    cv2.imwrite(pathsave,img)              
cv2.destroyAllWindows()