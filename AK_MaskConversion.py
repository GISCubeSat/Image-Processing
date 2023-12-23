import os
import AK_HighContrastEffect as hce

directory = "LEO_Resized"
files = os.listdir(directory)
#print(files)
path = "/Users/Arush/Documents/GitHub/Image-Processing/"
for file in files:
    hce.high_contrast_effect_1(directory, file, path + "LEO_Masks/MASK " + file, [0,0,0],[60,60,60])
