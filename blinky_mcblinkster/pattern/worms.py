import random
import time
from blinky_mcblinkster.pattern.base import BasePattern
from blinky_mcblinkster.color import Color
from blinky_mcblinkster import constants

BLACK_TUPLE = Color(0 ,0 ,0).to_tuple()

class Worm:
    def __init__(self, length=6, pix_per_second=60, color=None):
        self.length = length
        self.pix_per_second = pix_per_second + (random.random() * (pix_per_second/5))
        self.pos = random.random() * 500
        self.color = color or Color()


    def compute_frame(self):
        self.pos += self.pix_per_second / constants.FPS


class WormsPattern(BasePattern):
    def __init__(self, strand, worm_count=5, gen_color=None):
        self.strand = strand
        print(f"WORMS {worm_count}")

        self.worms = []
        for i in range(worm_count):
            if gen_color:
                color = gen_color()
            else:
                color = Color()
            print(color)
            self.worms.append(Worm(color=color))

    def next_frame(self):
        for worm in self.worms:
            worm.compute_frame()

        for i in range(self.strand.led_count):
            self.strand.pixels[i] = BLACK_TUPLE

        for i in range(self.strand.led_count):
            for worm in self.worms:
                pos = worm.pos % self.strand.led_count
                if pos <= i < pos + worm.length:
                    self.strand.pixels[i] = worm.color.to_tuple()
