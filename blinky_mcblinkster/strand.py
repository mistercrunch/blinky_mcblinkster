from blinky_mcblinkster.pixel import Pixel


class Strand:
    def __init__(self, led_count):
        self.led_count = led_count
        self.pixels = [Pixel(i) for i in range(led_count)]

    def compute_frame(self):
        for pixel in self.pixels:
            pixel.compute_frame()
