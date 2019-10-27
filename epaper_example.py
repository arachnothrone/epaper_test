# p2
# 2.7 inch epaper Waveshare RPi Hat example

import sys
# sys.path.insert(1, "./drivers")
sys.path.insert(1, "./lib")

import epd2in7
from PIL import Image
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

if __name__ == '__main__':
    print "Look at the center of the e-ink screen..."
    displayTest()


