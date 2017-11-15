import cv2
import numpy as np
from datetime import datetime

def converttostring(c2str): #Returns a String
    string = str(c2str)
    return string

def locationOfFace(x,y,w,h): #Returns the location of a face to the screen
    center_of_width = x+(w/2)
    center_of_height = y + (h/2)
    return center_of_width, center_of_height

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #Naming the Haar Cascade for the Face
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') #Naming the Haar Cascade for eyes

cap = cv2.VideoCapture(0)  #Captures Video from the Webcam
fourcc = cv2.VideoWriter_fourcc(*'XVID') #Video Codex
current_time = str(datetime.now()) #Gets  the Current Time
current_time = current_time.replace(":", ".") #Replaces the colons with periods
current_time = current_time + ".avi" #adds .avi to the fine name
print("File Name: ", current_time)
out = cv2.VideoWriter(current_time, fourcc, 30.0, (640,480)) #cv2.VideoWriter( filename, videotype, 
font = cv2.FONT_HERSHEY_SIMPLEX #Font for CV2

while True:
    ret, img, = cap.read()
    width = int(cap.get(3)) #cap.get(id) gets information from the video its height
    widths = converttostring(width)
    widthstr = "Width: " + widths
    height = int(cap.get(4)) #cap.get(id) gets information from the video in this case its the height
    heights = converttostring(height)
    heightstr = "Height: " + heights
    info = widthstr + " " + heightstr
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #Detects Faces in the image
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        center_x, center_y = locationOfFace(x,y,w,h)
        c_x = int(center_x)
        c_y = int(center_y)
        location = "X-Coord: " + str(center_x) + " Y-Coord: " + str(center_y)
        cv2.circle(img, (c_x,c_y), 5, (0,0,255),1)
        cv2.putText(img, location, (width - 275, height-40), font, .5, (255,255,255), 1,cv2.LINE_AA)
        roi_gray = gray[y:y+h, x:x+h]
        roi_color = img[y:y+h, x:x+w]
##        eyes = eye_cascade.detectMultiScale(roi_gray)
##        for(ex, ey, ew, eh) in eyes:
##            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)

    time = datetime.now() #Gets the current time
    current_time_on_screen = str(time) #Converts to string
    cv2.putText(img, current_time_on_screen, (width - 265, height-20), font, .5, (255,255,255), 1,cv2.LINE_AA) #Places Time Stamp on the video
    cv2.putText(img, info, (width-200, height-60), font, .5, (255,255,255),1,cv2.LINE_AA) #Places the width and height of the video on the screen
    out.write(img)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) &0xff
    if k == 27:
        break

    

cap.release()
out.release()
cv2.destroyAllWindows()
        

