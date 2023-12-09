import pygame
import sys

from blinky_mcblinkster.renderers.base import BaseRenderer
from blinky_mcblinkster import constants

CIRCLE_SIZE = 2


class PyGameRenderer(BaseRenderer):
    def __init__(self, size, width=800, height=600, show_fps=False):
        pygame.init()
        self.width = width
        self.height = height
        self.size = size
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Blinky McBlinkster")
        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()

        self.last_fps_print_time = pygame.time.get_ticks()
        self.start_time = pygame.time.get_ticks()
        self.frame_count = 0
        self.show_fps = show_fps

    def calculate_and_print_fps(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.start_time
        time_since_last_print = current_time - self.last_fps_print_time

        if time_since_last_print >= 1000:  # Check if 1 second has passed
            if elapsed_time > 0:
                fps = self.frame_count / (elapsed_time / 1000.0)
                print(f"FPS: {fps:.2f}")
            # Reset counters
            self.last_fps_print_time = current_time
            self.frame_count = 0
            self.start_time = pygame.time.get_ticks()

    def get_pixel_position(self, pixel_position):
        # Calculate the number of levels for the triangle
        levels = 0
        while (levels * (levels + 1)) // 2 < self.size:
            levels += 1

        # Find the level and position within the level for this pixel
        level = 1
        total_pixels_before_level = 0
        while pixel_position >= total_pixels_before_level + level:
            total_pixels_before_level += level
            level += 1

        position_in_level = pixel_position - total_pixels_before_level

        # Calculate x and y positions
        y = (self.height / (levels + 1)) * level
        x_spacing = self.width / levels
        x = (x_spacing / 2 + x_spacing * position_in_level) + (self.width / 2)

        # Center each level
        x -= (x_spacing * (level - 1)) / 2

        return int(x), int(y)

    def render_strand(self, strand):
        for i, pixel in enumerate(strand.pixels):
            pygame.draw.circle(
                self.screen,
                pixel,
                self.get_pixel_position(i),
                CIRCLE_SIZE,
            )
        if self.show_fps:
            self.calculate_and_print_fps()

        self.frame_count += 1
        pygame.display.flip()
        self.clock.tick(constants.FPS)
