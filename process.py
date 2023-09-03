import cv2
import numpy as np



#compile everything into one function for simplicity later
def main():
    filepath = '/Users/pic.jpg' #replace with actual filepath
    image = cv2.imread(filepath)

    #code to dsiplay image
    # cv2.imshow("imagename",image) 
    #cv2.waitKey() waits for any key to be pressed
    #cv2.destroyAllWindows() then destroys all windows of open images
    pass



color_range={}
color_range["blue"] = {(0,0,0),(255,0,0)} #placeholder threshold for blue
color_range["black"] = {(0,0,0),(0,0,0)} #another placeholder threshold for black



#code to mask blue/black to calculate avg percentage of blue/black
def get_mask(bound):
    '''use the upper and lower bounds from color_range with the inRange function to
     find all the pixels with color values in the range and return the theshold array, 
     then use the bitwise_and function to return the mask'''
    pass

def count_pixels(threshold):
    '''count all the pixels that are of each color, remember the in_range function
    returns an array of 0s and 1s'''
    pass

def calc_percentages(image):
    '''find the total number of pixels in the image,
    call the count_pixels function to return a percentage of black/blue,
    return the percentages as a tuple'''

    pass


'''if needed, you can also try and figure out how to calculate avg brightness'''
def calc_brightness():
    '''write code to calculate brightness, hint: convert to hsv and take the mean of brightnes
    values'''
    pass



main()