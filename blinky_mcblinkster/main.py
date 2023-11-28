from blinky_mcblinkster.strand import Strand
from blinky_mcblinkster.renderers.pygame import PyGameRenderer

LED_COUNT = 500
strand = Strand(LED_COUNT)

renderer = PyGameRenderer(LED_COUNT)

renderer.animate(strand)
