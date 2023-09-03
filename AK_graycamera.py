import cv2
import numpy as np

files = [
    'ORIGINAL_IMAGES/NAmericaEarth.jpeg',
    'ORIGINAL_IMAGES/BlueEarthTest.jpeg',
    'ORIGINAL_IMAGES/Polar(Clouds).jpeg',
]

def analyze_color_range_score(filename):
    img = cv2.imread(filename)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #npix = cv2.countNonZero(img_bw)
    bestpixs = cv2.inRange(img_hsv, np.array([0, 0, 0]), np.array([150, 100, 100]))
    rows, cols = img.shape[:2]

    return cv2.countNonZero(bestpixs)/(rows*cols)*100

def analyze_positive_space(filename):
    
    img = cv2.imread(filename)
    img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #thresholding, so it could detect slightly lighter shades of black
    threshold = 20
    _, img_bw = cv2.threshold(img_bw, threshold, 255, cv2.THRESH_BINARY_INV)


    npix = cv2.countNonZero(img_bw)
    rows, cols = img.shape[:2]

    return (1 - npix/(rows*cols))*100

# for file in files:
#     print(f"Scores for {file}:", (analyze_color_range_score(file), analyze_positive_space(file)))