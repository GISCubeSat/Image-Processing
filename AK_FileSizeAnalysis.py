# Matthew's Idea
import os

class File():
    def __init__(self, directory, file):
        self.file = file
        self.img_size = os.stat(directory + '/' + self.file).st_size
    
    def size(self):
        return self.img_size
    
    def fits_constraint(self, size_limit):
        return True if self.img_size <= size_limit else False
    
    def __repr__(self):
        return str(self.file)

def create_file(directory, file_name):
    return File(directory, file_name)

folder = "ORIGINAL_IMAGES"
file_names = os.listdir(folder)
files = []

for name in file_names:
    files.append(create_file(folder, name))

limit_kb = 2000
limit_b = limit_kb*1000
for file in files:
    print(file.file, '|', file.img_size, '=', file.fits_constraint(limit_b))