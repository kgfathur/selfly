from cv2 import *

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
#imwrite("image.jpg",img) #save image
#img = cv2.imread("image.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.show()
r,g,b=cv2.split(img)
h,w=r.shape
enol = np.zeros((h,w),'uint8')
enols=np.ones((h,w),'uint8')
enols=enols * 255
imgr = cv2.merge((r,enol,enol))
imgg = cv2.merge((enol,g,enol))
imgb = cv2.merge((enol,enol,b))
plt.subplot(2,2,1)
plt.imshow(imgr)
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2)
plt.imshow(imgg)
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3)
plt.imshow(imgb)
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4)
plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()
del(cam)
