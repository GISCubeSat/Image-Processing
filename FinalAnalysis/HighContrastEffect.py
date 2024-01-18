def high_contrast_effect_1(path, image, result_name, low, high):
    import cv2, numpy as np
    from PIL import Image

    print(path + '/' + image)

    img = cv2.imread(path + '/' + image)

    if img is None:
        #print(f"Error: Unable to load image at {path}/{image}")
        return

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    b1 = low
    b2 = high

    # define range of blue color in HSV
    low_color = np.array(b1, np.uint8)
    high_color = np.array(b2, np.uint8)

    # Create a mask. Threshold the HSV image to get only yellow colors
    mask = cv2.inRange(hsv, low_color, high_color)

    return cv2.imwrite(result_name, mask)


def high_contrast_effect_2(path, image, result_name):
    import cv2, numpy as np

    print(path + '/' + image)

    img = cv2.imread(path + '/' + image)

    if img is None:
        #print(f"Error: Unable to load image at {path}/{image}")
        return
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

    contours , _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours == 0:
        return
    max_area = 0
    best_cnt = None
    for counter in contours:
        area = cv2.contourArea(counter)
        if area > 1000:
            if area > max_area:
                max_area = area
                best_cnt = counter

    mask = np.zeros((gray.shape), np.uint8)

    cv2.drawContours(mask, [best_cnt], 0, 255, -1)
    cv2.drawContours(mask, [best_cnt], 0, 0, 2)

    # Bitwise-AND mask and original image
    result = cv2.bitwise_and(img,img, mask= mask)

    return cv2.imwrite(result_name, result)

def high_contrast_effect_3(path, image, result_name):
    from PIL import Image, ImageEnhance
    
    img = Image.open(f"{path}/{image}")
    hsv = img.convert('HSV')
    enhancer = ImageEnhance.Contrast(hsv)
    enhanced_img = enhancer.enhance(1.0)
    rgb = enhanced_img.convert('RGB')
    rgb.save(result_name)
    print(f"MASK {image} successfully saved!!")