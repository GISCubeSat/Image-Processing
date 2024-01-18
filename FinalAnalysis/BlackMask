import cv2
import numpy as np

images = [
  "img1.jpeg",
  "img2.jpeg"
]

def countBlack(img) :
	#reading the image which is to be masked
	imagergb = cv2.imread(img)
	#defining the lower bounds and upper bounds
	lower_bound = np.array([0, 0, 0])
	upper_bound = np.array([50, 50, 50])
	#masking the image using inRange() function
	imagemask = cv2.inRange(imagergb, lower_bound, upper_bound)
	
	total_pixels = imagergb.size
	print(total_pixels)
	print(np.count_nonzero(imagemask))
	blackpeople = np.count_nonzero(imagemask)
	print(blackpeople/total_pixels)
	black_pixel_percentage = blackpeople/total_pixels
	#displaying the resulting masked image
	cv2.imwrite("result-" + img, imagemask)
	return black_pixel_percentage

img_result = {}
most_pixels = ""
most_pixels_count = 0
for i in images:
	img_result[i] = countBlack(i)
	if most_pixels_count < img_result[i]:
		most_pixels_count = img_result[i]
		most_pixels = i

print(img_result)
print(most_pixels, " ", most_pixels_count)
