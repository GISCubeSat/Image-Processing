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

def pixel_count(file, lower_limit, upper_limit, step):
    from PIL import Image

    img = Image.open(file)

    pixels = list(img.getdata())
    cnt = 0

    for i in range(0, len(pixels), step):
        if lower_limit[0] <= pixels[i][0] <= upper_limit[0] and \
        lower_limit[1] <= pixels[i][1] <= upper_limit[1] \
        and lower_limit[2] <= pixels[i][2] <= upper_limit[2]:
            cnt += 1
    
    return cnt

def pixel_percentage(file, lower_limit, upper_limit, step):
    from PIL import Image
    img = Image.open(file)
    count = pixel_count(file, lower_limit, upper_limit, step)
    return count / (len(list(img.getdata()))/step) * 100

def filter_image(folder, files, lower_limit, upper_limit, percent_limit, step):
    return_list = []
    for file in files:
        percentOfBlackPixels = pixel_percentage(f'{folder}/{file}', lower_limit, upper_limit, step)
        if percentOfBlackPixels < percent_limit:
            return_list.append(file[0:11])
    return return_list

"""folder = "10_SEGMENTED_IMAGES"
files = os.listdir(f"10_SEGMENTED_IMAGES")
u_color = [6, 6, 6]
l_color = [4, 4, 4]
step = 10
percentage = 1
directory = f'{folder}/'
#print(pixel_percentage(f'{folder}/{files[6]}', color, 10))
filtered_list = sorted(filter_image(folder, files, l_color, u_color, percentage, step))
print(filtered_list)
for file in files:
    print(pixel_percentage(directory + file, l_color, u_color, step))"""