import time
from datetime import datetime

import board
import neopixel

from blinky_mcblinkster.renderers.base import BaseRenderer

pixel_pin = board.D18
c=(255, 0,0)

class NeoPixelRenderer(BaseRenderer):

    def __init__(self, size):
        ORDER = neopixel.GRB
        self.size = size
        self.neo_pixels = neopixel.NeoPixel(
            pixel_pin, size,
            #brightness=0.2,
            auto_write=False, pixel_order=ORDER
        )
        self.frame_count = 0
        self.last_frame_count = 0
        self.last_fps_print = datetime.now()

    def render_frame(self, strand):
        for pixel in strand.pixels:
            color = pixel.get_current_color()
            self.neo_pixels[pixel.pos] = pixel.get_current_color().to_tuple()
            #self.neo_pixels[pixel.pos] = c
        self.neo_pixels.show()
        self.frame_count += 1
        self.print_fps()

    def print_fps(self):
        now = datetime.now() 
        since_last = (now - self.last_fps_print).total_seconds()
        if since_last > 1:
            fps = (self.frame_count - self.last_frame_count) / (since_last)
            print(f"FPS: {fps}")
            self.last_fps_print = datetime.now()
            self.last_frame_count = self.frame_count
