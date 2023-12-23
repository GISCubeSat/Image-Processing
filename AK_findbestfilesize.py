import os
from AK_FileSizeAnalysis import File
import cv2

directory = "LEO_Masks"
files = os.listdir(directory)
objects = []

for file in files:
    objects.append(File(directory, file))

objects.sort(key=lambda x: x.size(), reverse=True)

the_chosen_one = objects[0].file
print(the_chosen_one)

img = cv2.imread(directory + '/' + the_chosen_one)
cv2.imshow("Best Image Selected", img)
cv2.waitKey(0)
cv2.destroyAllWindows()