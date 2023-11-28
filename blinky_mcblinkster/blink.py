# we bring in a library to generate random numbers
import random

# we bring in a library to manage time, and sometimes wait/sleep
import time

# two libraries to manage the lights
import board
import neopixel

# we set the number of pixels to the number we have in the tree
PIXEL_COUNT = 500

# we initialize the leds
neo_pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, auto_write=False)

# A big loop that never ends
while True:
    # for each pixel
    for i in range(PIXEL_COUNT):
        if random.random() < 0.25:
            r = random.random()
            if r < 0.33:
                # make that LED red
                v = (0, 255, 0)
            elif r < 0.66:
                # make it green
                v = (255, 0, 0)
            else:
                # make it white
                v = (100, 100, 100)
        else:
            # make it black
            v = (0, 0, 0)
        v = (50, 150, 50)
        neo_pixels[i] = v
    neo_pixels.show()
