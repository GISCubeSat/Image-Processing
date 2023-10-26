# Matthew's Idea
import os

class File():
    def __init__(self, file):
        self.file = file
        self.img_size = os.stat(self.file).st_size
    
    def size(self):
        return self.img_size
    
    def fits_constraint(self, size_limit):
        return True if self.img_size <= size_limit else False
    
    def __repr__(self):
        return str(self.file)

def create_file(file_name):
    return File(file_name)

files = [create_file("CMPBlueEarthTest.jpeg"), create_file("CMPEarth2560x1920.jpeg")]
limit_kb = 2
for file in files:
    print(file.size(), file.fits_constraint(limit_kb*1000))