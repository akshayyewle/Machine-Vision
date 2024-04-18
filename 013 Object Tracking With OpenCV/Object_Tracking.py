import cv2 as cv
import numpy 
from Object_Detection import Object_Detection

# Initialize Object Detection
obj_detect = Object_Detection()

cap = cv.VideoCapture(0)

while True:
    _,frame = cap.read()
    cv.imshow('frame',frame)
    key = cv.waitKey(1)
    if key == 27: # ESC key
        break

cap.release()   
cv.destroyAllWindows()
