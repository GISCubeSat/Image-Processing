import cv2
import numpy as np

path = "/Users/Arush/Documents/GitHub/Image-Processing/ORIGINAL_IMAGES/"
img = cv2.imread(path + 'NAmericaEarth.jpeg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

b1 = [0, 0, 0]
b2 = [150, 50, 50]

# define range of blue color in HSV
low_blue = np.array(b1, np.uint8)
upper_blue = np.array(b2, np.uint8)

# Create a mask. Threshold the HSV image to get only yellow colors
mask = cv2.inRange(hsv, low_blue, upper_blue)

# Bitwise-AND mask and original image
result = cv2.bitwise_and(img,img, mask= mask)

# display the mask and masked image
cv2.imshow('Mask',mask)
cv2.waitKey(0)
cv2.imshow('Masked Image',result)
cv2.waitKey(0)
cv2.destroyAllWindows()