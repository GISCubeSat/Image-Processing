# Write your code here :-)
import sys
import board
import busio
import time
import digitalio
import adafruit_ov5640
#import adafruit_tca9548a
import displayio
import gc
gc.enable()
print("memory before allocation: {}".format(gc.mem_free()))
height=480
width=640
quality=30
buf=bytearray(height*width//quality)
print("memory after allocation: {}".format(gc.mem_free()))

i2c1=busio.I2C(board.I2C1_SCL,board.I2C1_SDA)
cam = adafruit_ov5640.OV5640(
    i2c1,
    data_pins=(
        board.D3,
        board.D13,
        board.PC,
        board.VS,
        board.D4,
        board.D5,
        board.D6,
        board.D8,
    ),
    clock=board.D2,
    vsync=board.D7,
    href=board.D9,
    mclk=None,
    shutdown=None,
    reset=None,
    size=adafruit_ov5640.OV5640_SIZE_VGA
)


cam.colorspace = adafruit_ov5640.OV5640_COLOR_JPEG
cam.flip_y = False
cam.flip_x = False
cam.test_pattern = False

cam.effect=0
cam.exposure_value=-2
cam.white_balance=2
cam.night_mode=False
cam.quality=quality
print("memory before collection: {}".format(gc.mem_free()))
gc.collect()
print("memory after collection: {}".format(gc.mem_free()))
while True:
    time.sleep(2)
    print("memory before picture: {}".format(gc.mem_free()))
    try:
        print("bout to take dat pic")
        cam.capture(buf)
        print("done")
        eoi = buf.find(b"\xff\xd9")
        if eoi != -1:
            # terminate the JPEG data just after the EOI marker
            print(memoryview(buf)[: eoi + 2].hex())
        else:
            print(buf)
            print("image corrupted!")

    except Exception as e:
        print("error! " + str(e))
        gc.collect()
    print("memory after picture: {}".format(gc.mem_free()))

"""
bus = busio.I2C(board.GP9, board.GP8)
reset = digitalio.DigitalInOut(board.GP10)
cam = adafruit_ov5640.OV5640(
    bus,
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
    reset=reset,
    size=adafruit_ov5640.OV5640_SIZE_QQVGA,
)
"""
"""
time.sleep(2)
print("memory before picture: {}".format(gc.mem_free()))
try:
    print("bout to take dat pic")
    cam.capture(buf)
    print("done")
    eoi = buf.find(b"\xff\xd9")
    if eoi != -1:
        # terminate the JPEG data just after the EOI marker
        print(memoryview(buf)[: eoi + 2].hex())
    else:
        #print(buf)
        print("image corrupted!")

except Exception as e:
    print("error! " + str(e))
    #gc.collect()
print("memory after picture: {}".format(gc.mem_free()))
"""