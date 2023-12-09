from blinky_mcblinkster.strand import Strand
from blinky_mcblinkster.pattern.pixel_cycle import PixelCyclePattern


XMAS_COLORS = [
    (255, 255, 255),
    (255, 0, 0),
    (0, 0, 255),
]

ENV = "NEO"
LED_COUNT = 500
strand = Strand(LED_COUNT)
pattern = PixelCyclePattern(strand, XMAS_COLORS)


if ENV == "NEO":
    from blinky_mcblinkster.renderers.neopixels import NeoPixelRenderer

    renderer = NeoPixelRenderer(LED_COUNT)

else:
    from blinky_mcblinkster.renderers.pygame import PyGameRenderer

    renderer = PyGameRenderer(LED_COUNT)


renderer.animate(pattern)
