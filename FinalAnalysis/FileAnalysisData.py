"""RUN THIS ONLY ONCE (when you have all the files)"""

import os
from FileSizeAnalysis import File
import PixelPercentages as pixels

data_upload = open('graph_data.satdata', 'w')

directory = "/Users/Arush/Documents/GitHub/Image-Processing/LEO_Masks"
files = os.listdir(directory)

file_objs = [File(directory, file) for file in files]

sizes = [obj.size() for obj in file_objs]
percentages = [pixels.pixel_percentage(directory+'/'+file, (0, 0, 0)) for file in files]

for i in range(len(sizes)):
    data_upload.write(str(percentages[i]) + " " + str(sizes[i]) + '\n')
