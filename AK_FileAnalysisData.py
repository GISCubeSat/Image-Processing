"""RUN THIS ONLY ONCE (when you have all the files)"""

import os
from AK_FileSizeAnalysis import File
import AK_Pixels as pixels

data_upload = open('graph_data.satdata', 'w')

directory = "LEO"
files = os.listdir(directory)

file_objs = [File(directory, file) for file in files]

sizes = [obj.size() for obj in file_objs]
percentages = [pixels.pixel_percentage(directory+'/'+file, (0, 0, 0)) for file in files]

for i in range(len(sizes)):
    data_upload.write(str(percentages[i]) + " " + str(sizes[i]) + '\n')
