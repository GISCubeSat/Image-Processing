from PIL import Image
import os
from AK_graycamera import analyze_color_range_score, analyze_positive_space
from AK_compression import thumbnail, compress
import cv2

def determine_img_to_seg():
    folder_path = "CMP_IMAGES"
    directory_list = os.listdir(folder_path)

    visual_index_sum = 0
    best_img = None

    for file in directory_list:
        color_range_score = analyze_color_range_score(f"{folder_path}/{file}")
        positive_space_score = analyze_positive_space(f"{folder_path}/{file}")

        print(f"Scores for {file}:", color_range_score, positive_space_score)
        if (color_range_score + positive_space_score) > visual_index_sum:
            visual_index_sum = color_range_score + positive_space_score
            best_img = file

    return best_img # string path of the best image

def segmented_image(input_path, output_folder, segment_size = (160, 120)):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    img = Image.open(input_path)
    img_width, img_height = img.size

    if img_width != 2560 or img_height != 1920:
        print(f"Expecting a 2560 x 1920 image, got {img_width} x {img_height} instead")
        return 
    
    for i in range(0, img_width, segment_size[0]):
        for j in range(0, img_height, segment_size[1]):
            box = (i, j, i+segment_size[0], j+segment_size[1])
            segment = img.crop(box)

            output_path = os.path.join(output_folder, "segment_{}_{}.webp".format(int(i/segment_size[0]), int(j/segment_size[1])))
            segment.save(output_path, 'webp', optimize = True, quality = 10)

    print("Segmentation complete!")
ak_path = "/Users/Arush/Documents/GitHub/Image-Processing/"
compress("/Users/Arush/Documents/GitHub/Image-Processing/ORIGINAL_IMAGES", 'Earth2560x1920.jpeg', 20, 50)
folder_path = "CMP_IMAGES"
output_folder = "/Users/Arush/Documents/GitHub/Image-Processing/10_SEGMENTED_IMAGES"
# best_img = determine_img_to_seg()
#best_img = "/Users/a970/Documents/Image-Processing/ORIGINAL_IMAGES/Earth2560x1920.jpeg"
best_img = "CMPEarth2560x1920.jpeg"
# in our case, b/c CMPNAmericaEarth has the greatest sum of index, it segments that image
segmented_image(f"{folder_path}/{best_img}", output_folder)

    