import random
import time

import board
import neopixel

PIXEL_COUNT = 500

neo_pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT)
frame_number = 0

neo_pixels.fill((0, 0, 0))
for i in range(PIXEL_COUNT):
    neo_pixels[i] = (0, 0, 0)
    frame_number = frame_number + 1
    print("test " + str(frame_number))
neo_pixels.show()
print("Done!")
