import random
from blinky_mcblinkster.strand import Strand
from blinky_mcblinkster.color import Color
from blinky_mcblinkster.show import Show
from blinky_mcblinkster.pattern.pixel_cycle import PixelCyclePattern, BlinkMode
from blinky_mcblinkster.pattern.worms import WormsPattern

ENV = "NEO"
LED_COUNT = 500
strand = Strand(LED_COUNT)

if ENV == "NEO":
    from blinky_mcblinkster.renderers.neopixels import NeoPixelRenderer
    renderer = NeoPixelRenderer(LED_COUNT)

else:
    from blinky_mcblinkster.renderers.pygame import PyGameRenderer

    renderer = PyGameRenderer(LED_COUNT)


XMAS_COLORS = [
    Color(255, 255, 255),
    Color(255, 0, 0),
    Color(0, 255, 0),
    Color(0, 0, 0),
    Color(0, 0, 0),
    Color(0, 0, 0),
    Color(0, 0, 0),
    Color(0, 0, 0),
]

def get_bluey_color():
    return Color(0, 0, 255, randomize_perc=0.7)
    #return random.choice(XMAS_COLORS)

def gen_xmas_color():
    return random.choice(XMAS_COLORS)



patterns = [
    #WormsPattern(strand, gen_color=gen_xmas_color),
    PixelCyclePattern(strand, lambda: Color(0, 255, 0, randomize_perc=5), BlinkMode.LINEAR_UP_DOWN, 10000),
    PixelCyclePattern(strand, lambda: Color(0, 255, 0, randomize_perc=0.3), BlinkMode.LINEAR_UP_DOWN, 500),
    PixelCyclePattern(strand, lambda: Color(0, 0, 255, randomize_perc=0.7), BlinkMode.LINEAR_UP_DOWN, 3000),
    PixelCyclePattern(strand, lambda: Color(255, 0, 0, randomize_perc=0.5), BlinkMode.LINEAR_UP_DOWN, 1000),
    PixelCyclePattern(strand, gen_xmas_color, BlinkMode.LINEAR_UP_DOWN, 1000),
]

show = Show(renderer, patterns, 100)
show.run()
