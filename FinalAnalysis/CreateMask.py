import os
import HighContrastEffect as hce

directory = "LEO_Resized"
files = os.listdir(directory)
#print(files)
path = "/Users/Arush/Documents/GitHub/Image-Processing/"
for file in files:
    hce.high_contrast_effect_3(directory, file, path + "LEO_Masks/MASK " + file)
