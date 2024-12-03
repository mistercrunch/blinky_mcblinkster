import random
import time
from blinky_mcblinkster.pattern.base import BasePattern
from blinky_mcblinkster.color import Color
from blinky_mcblinkster import constants


class BlinkMode:
    LINEAR_UP_DOWN = 1
    BLINK = 2
    FADE_TO = 3


class Pixel:
    def __init__(self, pos, colors, mode=BlinkMode.LINEAR_UP_DOWN, blink_duration=1000):
        self.pos = pos
        self.colors = colors
        self.frame = 0
        self.blink_duration = blink_duration
        self.mode = mode
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
        self.set_cycle_duration(self.blink_duration)
        if self.mode in [BlinkMode.LINEAR_UP_DOWN, BlinkMode.BLINK]:
            if callable(self.colors):
                color = self.colors()
            else:
                color = random.choice(colors)
            self.color = color

    def set_cycle_duration(self, ms=1000, randomness=0.1):
        cycle = (ms / 1000) * constants.FPS
        self.cycle = int(cycle + (random.random() * cycle * randomness))

    def get_current_color(self):
        if self.mode == BlinkMode.LINEAR_UP_DOWN:
            half_cycle = int(self.cycle / 2) + 1
            if self.frame <= half_cycle:
                dim = self.frame / half_cycle
            else:
                dim = 1 - ((self.frame - half_cycle) / half_cycle)
            return self.color.dim(dim)

        elif self.mode == BlinkMode.BLINK:
            half_cycle = int(self.cycle / 2) + 1
            if self.frame <= half_cycle:
                return self.color
            else:
                return self.color.dim(0)


class PixelCyclePattern(BasePattern):
    def __init__(
        self, strand, colors, mode=BlinkMode.LINEAR_UP_DOWN, blink_duration=1000
    ):
        self.strand = strand
        self.pixels = [
            Pixel(i, colors, mode, blink_duration) for i in range(strand.led_count)
        ]
        self.colors = colors

    def next_frame(self):
        for pixel in self.pixels:
            pixel.compute_frame()
        self.strand.pixels = [
            pixel.get_current_color().to_tuple() for i, pixel in enumerate(self.pixels)
        ]
