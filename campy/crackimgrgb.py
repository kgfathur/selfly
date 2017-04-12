from PIL import Image
import numpy as np
rgbArray = np.zeros((512,512,3), 'uint8')
rgbArray[..., 0] = r*256
rgbArray[..., 1] = g*256
rgbArray[..., 2] = b*256
img = Image.fromarray(rgbArray)
img.save('myimg.jpeg')
