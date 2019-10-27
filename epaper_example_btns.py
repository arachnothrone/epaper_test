# p2
# 2.7 inch epaper Waveshare RPi Hat example

import sys
sys.path.insert(1, "./lib")

import time
import epd2in7
import RPi.GPIO as GPIO
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def displayTest():

        # Initialize
        epd = epd2in7.EPD()
        epd.init()

        # Clear screen (255 - fill with white, width x height of the screen)
        image = Image.new('1', (epd2in7.EPD_WIDTH, epd2in7.EPD_HEIGHT), 255)    
        draw = ImageDraw.Draw(image)

        # Square at the center
        draw.rectangle((epd2in7.EPD_WIDTH/2-15, epd2in7.EPD_HEIGHT/2-15, epd2in7.EPD_WIDTH/2+15, epd2in7.EPD_HEIGHT/2+15), fill = 0)

        # Refresh
        epd.display(epd.getbuffer(image))

def displayUpdate(text, img):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
    draw.text((10, 30), text, font = font, fill = 0)
    print("Refreshing screen...")

    epd.display(epd.getbuffer(img))


if __name__ == '__main__':
    print "Waiting for button..."
    
    GPIO.setmode(GPIO.BCM)
    epd = epd2in7.EPD()
    epd.init()
    image = Image.new('1', (epd2in7.EPD_WIDTH, epd2in7.EPD_HEIGHT), 255)

    key1 = 5
    key2 = 6
    key3 = 13
    key4 = 19

    GPIO.setup(key1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(key2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(key3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(key4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        getKey1 = GPIO.input(key1)
        getKey2 = GPIO.input(key2)
        getKey3 = GPIO.input(key3)
        getKey4 = GPIO.input(key4)
         
        #displayUpdate("Btn prssd", image)
        #time.sleep(0.3)
        
        if getKey1 == False:
            print("Button One")
            displayUpdate("Button One", image)
            time.sleep(0.2)
        if getKey2 == False:
            print("Button Two")
            displayUpdate("Button Two", image)
            time.sleep(0.2)
        if getKey3 == False:
            print("Button Three")
            displayUpdate("Button Three", image)
            time.sleep(0.2)
        if getKey4 == False:
            print("Button Four")
            displayUpdate("Button Four", image)
            time.sleep(0.2)


