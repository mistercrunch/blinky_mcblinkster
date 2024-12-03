import random

MAX_COLOR_VALUE = 255


class Color:
    def __init__(self, r=None, g=None, b=None, randomize_perc=None):
        if r is None and g is None and b is None:
            self.set_random()
        else:
            self.r = r
            self.g = g
            self.b = b

        if randomize_perc:
            self.randomize(randomize_perc)

    def set_random(self):
        self.r = random.randint(0, 90)
        self.g = random.randint(0, 90)
        self.b = random.randint(0, 90)

    def dim(self, perc):
        return Color(self.r * perc, self.g * perc, self.b * perc)

    def to_rgb_tuple(self):
        return (self.r, self.g, self.b)

    def __str__(self):
        return f"r:{int(self.r)} g:{int(self.g)} b:{int(self.b)}"

    def to_tuple(self, intify=True):
        if intify:
            return (int(self.r), int(self.g), int(self.b))
        return self.to_rgb_tuple()

    def fade_to(self, color, perc):
        new_r = self.r + (color.r - self.r) * perc
        new_g = self.g + (color.g - self.g) * perc
        new_b = self.b + (color.b - self.b) * perc
        return Color(new_r, new_g, new_b)

    def _apply_random_change(self, perc):
        change_range = MAX_COLOR_VALUE * perc
        self.r = max(0, min(MAX_COLOR_VALUE, self.r + random.uniform(-change_range, change_range)))
        self.g = max(0, min(MAX_COLOR_VALUE, self.g + random.uniform(-change_range, change_range)))
        self.b = max(0, min(MAX_COLOR_VALUE, self.b + random.uniform(-change_range, change_range)))

    def randomize(self, perc):
        self._apply_random_change(perc)

    def get_randomized(self, perc):
        new_color = Color(self.r, self.g, self.b)
        new_color._apply_random_change(perc)
        return new_color
