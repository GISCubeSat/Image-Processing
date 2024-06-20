"""Made by BRONCO SPACE of CAL POLY POMONA
Edited by ARUSH KHARE of IRVINGTON CUBESAT"""

# Initialize Libraries
import board
import busio
import time
import adafruit_ov5640
import gc
import os

# Initialize Camera and Garbage Collector
gc.enable()
print("memory before allocation: {}".format(gc.mem_free()))
FACTOR = 1
height=480
width=640
quality=20
buf=bytearray(height*width//quality)
print("memory after allocation: {}".format(gc.mem_free()))

i2c1=busio.I2C(board.GP9,board.GP8)
cam = adafruit_ov5640.OV5640(
    i2c1,
    data_pins=(
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP15,
        board.GP16,
        board.GP17,
        board.GP18,
        board.GP19,
    ),
    clock=board.GP11,
    vsync=board.GP7,
    href=board.GP21,
    mclk=board.GP20,
    shutdown=None,
    reset=None,
    size=adafruit_ov5640.OV5640_SIZE_VGA
)

# Camera Settings
cam.colorspace = adafruit_ov5640.OV5640_COLOR_JPEG
cam.flip_y = False
cam.flip_x = True
cam.test_pattern = False
cam.effect=0
cam.exposure_value=-4
cam.white_balance=2
cam.night_mode=False
cam.quality=quality
print("memory before collection: {}".format(gc.mem_free()))
gc.collect()
print("memory after collection: {}".format(gc.mem_free()))
time.sleep(2)
print("memory before picture: {}".format(gc.mem_free()))

# Image Capture
"""buff_arr = []
for i in range(10):
    cam.capture(buf)
    buff_arr.append((len(memoryview(buf).hex()), memoryview(buf)))
buff_arr.sort()
photo_file = open("Best Photo.jpeg", 'wb')
photo_file.write(buff_arr[-1][1])
photo_file.close()"""

"""for i in range(10):
    cam.capture(buf)
    print('Done')

    #eoi = buf.find(b"\xff\xd9")
    #print(eoi)

    photo_file = open(f"photo{i}.jpeg", 'wb')

    #if eoi != -1:
        # terminate the JPEG data just after the EOI marker
        #print(memoryview(buf)[: eoi + 2].hex())
    #else:
        #print(buf)
        #print("image corrupted!")

    photo_file.write(buf)
    #time.sleep(1)
    #print("memory after picture: {}".format(gc.mem_free()))
    photo_file.close()"""

"""cam.capture(buf)
print(buf)
photo_file = open(f"photo_test.jpeg", 'wb')
photo_file.write(buf)
photo_file.close()"""
test = []
for i in range(10):
    cam.capture(buf)
    x = memoryview(buf).hex()
    test.append(x.count('a')+x.count('b')+x.count('c')+x.count('d')+x.count('e')+x.count('f'))
    time.sleep(2.0)