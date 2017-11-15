import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (250,150), (255,0,0), 5) #cv2.line(What your drawing on, location one, location two, color(bgr), width
cv2.rectangle(img, (15,25), (200,150),(0,255,0), 5)
cv2.circle(img, (255,300), 55, (0,0,255), -1) # -1 fills in the circle

pts = np.array([[500,450],[100,20],[20,100],[450,500]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255),3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCv Tuts!', (300,500), font, 2, (200,255,255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
