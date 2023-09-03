import cv2
import numpy as np
from PIL import Image

files = [
    # '/Users/a970/Documents/CamCode/NAmericaEarth.jpeg',
    # '/Users/a970/Documents/CamCode/BlueEarthTest.jpeg',
    # '/Users/a970/Documents/CamCode/Polar(Clouds).jpeg'
    'NAmericaEarth.jpeg',
    'BlueEarthTest.jpeg',
    'Polar(Clouds).jpeg'
]

def compress(file, factor, img_quality):
    img = Image.open(file)

    width, height = img.size
    new_size = (width//factor, height//factor)
    resized = img.resize(new_size)

    new_name = "CMP" + file
    resized.save(new_name, 'JPEG', optimize=True, quality=img_quality)
    return new_name

def thumbnail(file, factor, img_quality):
    img = Image.open(file)
    width, height = img.size
    img.thumbnail((width//factor, height//factor), Image.LANCZOS)

    new_name = "THB" + file
    img.save(new_name, 'JPEG', optimize=True, quality=img_quality)

    return new_name

def analyze_color_range_score(filename):
    img = cv2.imread(filename)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #npix = cv2.countNonZero(img_bw)
    bestpixs = cv2.inRange(img_hsv, np.array([0, 0, 0]), np.array([150, 100, 100]))
    rows, cols = img.shape[:2]

    return cv2.countNonZero(bestpixs)/(rows*cols)*100

def analyze_black_score(filename):
    img = cv2.imread(filename)
    img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    threshold = 30
    _, img_bw = cv2.threshold(img_bw, threshold, 255, cv2.THRESH_BINARY_INV)

    npix = cv2.countNonZero(img_bw)
    rows, cols = img.shape[:2]

    return 100 - (1 - npix/(rows*cols))*100

for file in files:
    new_file = thumbnail(file, 10, 50)
    print(f"Color range score for {new_file}:", (analyze_color_range_score(new_file)))
    print(f"\t Negative Space: {analyze_black_score(new_file)}")