import random


class Color:
    def __init__(self, r=None, g=None, b=None):
        self.r = r
        self.g = g
        self.b = b

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
        return (self.r, self.g, self.b)
