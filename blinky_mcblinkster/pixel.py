import random
import time

from blinky_mcblinkster.color import Color
from blinky_mcblinkster import constants


class ColorMode:
    LINEAR_UP_DOWN = 1


class Pixel:
    def __init__(self, pos):
        self.pos = pos
        self.frame = 0
        self.mode = ColorMode.LINEAR_UP_DOWN
        self.new_cycle()
        self.randomize_frame()

    def randomize_frame(self):
        self.frame = int(random.random() * self.cycle)

    def compute_frame(self):
        if self.frame >= self.cycle:
            self.new_cycle()
            self.frame = 0
        else:
            self.frame += 1

    def new_cycle(self):
        self.set_cycle_duration()
        if self.mode == ColorMode.LINEAR_UP_DOWN:
            self.color = random.choice([
                Color(255, 0, 0),
                Color(0, 255, 0),
                Color(255, 255, 255),
                Color(0, 0, 0),
            ])
            #print(f"color: {self.color.to_tuple()}")

    def set_cycle_duration(self, ms=500, randomness=0.1):
        cycle = (ms/1000) * constants.FPS
        self.cycle = int(cycle + (random.random() * cycle * randomness))

    def get_current_color(self):
        if self.mode == ColorMode.LINEAR_UP_DOWN:
            half_cycle = int(self.cycle / 2) + 1
            if self.frame <= half_cycle:
                dim = self.frame / half_cycle
            else:
                dim = 1-((self.frame - half_cycle) / half_cycle)
            #print(f"frame:{self.frame} cycle:{self.cycle} hc:{half_cycle} dim:{dim}")
            return self.color.dim(dim)
