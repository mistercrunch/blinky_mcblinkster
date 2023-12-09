from blinky_mcblinkster.pixel import Pixel


class Strand:
    def __init__(self, led_count):
        self.led_count = led_count
        self.pixels = [i for i in range(led_count)]
