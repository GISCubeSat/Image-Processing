import os

def pixel_analysis(file, upper_limit):
    from PIL import Image

    img = Image.open(file)
    
    pixels = list(img.getdata())
    new_list = []

    for pixel in pixels:
        if pixel[0] <= upper_limit[0] and pixel[1] <= upper_limit[1] and pixel[2] <= upper_limit[2]:
            new_list.append(pixel)

    return new_list

def pixel_count(file, upper_limit):
    from PIL import Image

    img = Image.open(file)

    pixels = list(img.getdata())
    cnt = 0

    for pixel in pixels:
        if pixel[0] <= upper_limit[0] and pixel[1] <= upper_limit[1] and pixel[2] <= upper_limit[2]:
            cnt += 1
    
    return cnt

def pixel_percentage(file, upper_limit):
    from PIL import Image
    img = Image.open(file)
    count = pixel_count(file, upper_limit)
    return count / len(list(img.getdata())) * 100

def filter_image(folder, files, upper_limit):
    return_list = []
    for file in files:
        percentOfBlackPixels = pixel_percentage(f'{folder}/{file}', upper_limit)
        if percentOfBlackPixels < 20:
            return_list.append(file)
    return return_list

print(filter_image("10_SEGMENTED_IMAGES", os.listdir(f"10_SEGMENTED_IMAGES"), [50, 50, 50]))

"""for file_name in sorted(os.listdir(f'10_SEGMENTED_IMAGES')):
    path_name = f'10_SEGMENTED_IMAGES/{file_name}'
    max_color = [50, 50, 50]
    #print(pixel_count(path_name, max_color))
    print(f"Values for {file_name}: {pixel_count(path_name, max_color)} px, {pixel_percentage(path_name, max_color)}%")
    """