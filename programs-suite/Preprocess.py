import numpy as np
import cv2

def preprocessFromImage(img):
    
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    img = cv2.bitwise_not(img)

    # increase contrast
    pxmin = np.min(img)
    pxmax = np.max(img)

    imgContrast = (img - pxmin) / (pxmax - pxmin) * 255

    # increase line width
    kernel = np.ones((3, 3), np.uint8)
    img_contrasted = cv2.erode(imgContrast, kernel, iterations = 1)

    # write
    #cv2.imwrite('out.png', imgMorph)
    return img_contrasted