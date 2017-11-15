import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

img[155,55] = [255,0,0]
px = img[155,559]
print(px)

roi = img[100:150, 100:150] = [255,0,255]

#print(roi)

watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
