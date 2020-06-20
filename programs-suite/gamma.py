from __future__ import print_function
import cv2
import numpy as np


img  = cv2.imread("test/test6.png",cv2.IMREAD_GRAYSCALE)
img = cv2.bitwise_not(img)
gamma = 0.01
invGamma = 1.0/gamma
table = np.array([((i /255.0)** invGamma)*255
        for i in np.arange(0,256)]).astype("uint8")

img_final = cv2.LUT(img,table)

cv2.imwrite("gamma1.png",img_final)