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

def displayUpdate(text, img, x, y):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 18)
    draw.text((x, y), text, font = font, fill = 0)
    print("Refreshing screen...")

    epd.display(epd.getbuffer(img))

def displayClear():
    # Clear screen (255 - fill with white, width x height of the screen)
    image = Image.new('1', (epd2in7.EPD_WIDTH, epd2in7.EPD_HEIGHT), 255)
    ImageDraw.Draw(image)


if __name__ == '__main__':
    print "Waiting for button..."
    
    GPIO.setmode(GPIO.BCM)
    epd = epd2in7.EPD()
    epd.init()
    image = Image.new('1', (epd2in7.EPD_WIDTH, epd2in7.EPD_HEIGHT), 255)
    #draw = ImageDraw.Draw(image)


    key1 = 5
    key2 = 6
    key3 = 13
    key4 = 19

    GPIO.setup(key1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(key2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(key3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(key4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        #print "---> 1"
        getKey1 = GPIO.input(key1)
        getKey2 = GPIO.input(key2)
        getKey3 = GPIO.input(key3)
        getKey4 = GPIO.input(key4)

        #print "---> 2"
        #print "{} {} {} {}".format(getKey1, getKey2, getKey3, getKey4)
        #displayUpdate("Btn prssd", image)
        #time.sleep(0.3)
        
        if getKey1 == False:
            print("Button One")
            displayClear()
            displayUpdate("Button One", image, 10, 30)
            time.sleep(0.2)
        if getKey2 == False:
            print("Button Two")
            displayClear()
            displayUpdate("Button Two", image, 10, 45)
            time.sleep(0.2)
        if getKey3 == False:
            print("Button Three")
            displayClear()
            displayUpdate("Button Three", image, 10, 60)
            time.sleep(0.2)
        if getKey4 == False:
            print("Button Four")
            #displayClear()
            displayUpdate("      x   ", image, 10, 30)
            displayUpdate("Button Four", image, 10, 75)
            time.sleep(0.2)


