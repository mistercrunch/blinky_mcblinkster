import random
import time

import board
import neopixel

PIXEL_COUNT = 500
FPS = 30

neo_pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, auto_write=False)


class Color:
    def __init__(self, r=None, g=None, b=None):
        if not r:
            self.set_random()
        else:
            self.r = r
            self.g = g
            self.b = b

    def set_random(self):
        self.r = random.randint(0, 90)
        self.g = random.randint(0, 90)
        self.b = random.randint(0, 90)


class Pixel:
    def __init__(self, pos):
        self.pos = pos
        self.frame = 0
        self.cycle = random.randint(FPS * 0.1, FPS * 1)
        self.color = Color()

    def animate(self):
        if self.frame >= self.cycle:
            #print(f"pos: {self.pos} | frame: {self.frame}")
            self.frame = 0
            self.color =  Color()
        else:
            self.frame += 1
        self.set_neo_pixel()

    def set_neo_pixel(self):
        neo_pixels[self.pos] = (self.color.r, self.color.g, self.color.b)

pixels = [Pixel(i) for i in range(PIXEL_COUNT)]

while True:
    for i in range(PIXEL_COUNT):
        pixels[i].animate()
    time.sleep(1/FPS);
    neo_pixels.show()
