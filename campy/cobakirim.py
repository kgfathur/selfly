#!/usr/bin/env python

import time
import serial

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate = 115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)

img = mpimg.imread("image.jpg")

d=np.array(np.dsplit(img,3),'uint8')
r=d[0]
g=d[1]
b=d[2]
h,w,t=r.shape
enol = np.zeros((h,w),'uint8')

counter=0
x=r.astype(int)
while 1:
	#ser.write('Write counter: %d \n'%(counter))

	ser.write(x)
#	counter += 1

#plt.imshow(imgs)
#plt.xticks([]), plt.yticks([])
#plt.show()
