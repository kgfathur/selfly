import cv2

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("image.jpg")

#a=np.array([[[11,12,13],[21,22,23],[31,32,33]],[[41,42,43],[51,52,53],[61,62,63]],[[71,72,73],[81,92,93],[91,92,93]],[[101,102,103],[111,112,113],[121,122,123]],[[131,132,133],[141,142,143],[151,152,153]]])
d=np.array(np.dsplit(img,3),'uint8')
r=d[0]
g=d[1]
b=d[2]
h,w,t=r.shape
enol = np.zeros((h,w),'uint8')
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

imgs = cv2.merge((r,g,b))
plt.subplot(2,2,4)
plt.imshow(imgs)
plt.xticks([]), plt.yticks([])
plt.show()
