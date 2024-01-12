import os

def fix_resolution(directory, image, result_name):
    from PIL import Image

    img = Image.open(directory + '/' + image)
    img.resize((300, 300))
    img.save(result_name, dpi=(300,300))
    return True

dirs = "/Users/Arush/Documents/GitHub/Image-Processing/LEO"
files = os.listdir(dirs)

for file in files:
    fix_resolution(dirs, file, f"LEO_Resized/R:{file}")
