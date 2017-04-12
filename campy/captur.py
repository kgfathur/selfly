from cv2 import *
import cv2
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    imshow("cam-test",img)
waitKey(0)
cv2.destroyAllWindows()
imwrite("image.jpg",img) #save image
