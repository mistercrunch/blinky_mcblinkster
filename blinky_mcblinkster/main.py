import random
from blinky_mcblinkster.strand import Strand
from blinky_mcblinkster.color import Color
from blinky_mcblinkster.pattern.pixel_cycle import PixelCyclePattern, BlinkMode
from blinky_mcblinkster.pattern.worms import WormsPattern


XMAS_COLORS = [
    Color(255, 255, 255),
    Color(255, 0, 0),
    Color(0, 255, 0),
]

def gen_xmas_color():
    return random.choice(XMAS_COLORS)

ENV = "NEOA"
LED_COUNT = 500
strand = Strand(LED_COUNT)

pattern = PixelCyclePattern(strand, XMAS_COLORS, BlinkMode.LINEAR_UP_DOWN, 500)
pattern = PixelCyclePattern(strand, [Color(255,255,255), Color(0,0,0), Color(0,0,0), Color(0,0,0)], BlinkMode.LINEAR_UP_DOWN, 200)
pattern = WormsPattern(strand, gen_color=gen_xmas_color)


if ENV == "NEO":
    from blinky_mcblinkster.renderers.neopixels import NeoPixelRenderer

    renderer = NeoPixelRenderer(LED_COUNT)

else:
    from blinky_mcblinkster.renderers.pygame import PyGameRenderer

    renderer = PyGameRenderer(LED_COUNT)


renderer.animate(pattern)
