import numpy as np
from geometry import hpt, translate
import operator as op
import functools as fn
import itertools as itt


class Window:
    def __init__(self, p1, p2):
        super().__init__()
        self.p1 = p1
        self.p2 = p2

    def move_up(self, amount):
        self.p1 += hpt(0., amount)
        self.p2 += hpt(0., amount)

    def move_down(self, amount):
        self.p1 -= hpt(0., amount)
        self.p2 -= hpt(0., amount)

    def move_left(self, amount):
        self.p1 += hpt(amount, 0.)
        self.p2 += hpt(amount, 0.)

    def move_right(self, amount):
        self.p1 -= hpt(amount, 0.)
        self.p2 -= hpt(amount, 0.)

    def zoom_in(self, amount):
        self.p1 += hpt(amount, amount)
        self.p2 -= hpt(amount, amount)

    def zoom_out(self, amount):
        self.p1 -= hpt(amount, amount)
        self.p2 += hpt(amount, amount)


class Viewport:
    def __init__(self, top_left, size):
        self.top_left = top_left
        self.size = size

    def resize(self, width, height):
        size = hpt(width, height)
        self.size = size

    def transformer(self, window: Window):
        def transform(p):
            u = (window.p2 - window.p1)[:-1]
            x, y = (p - window.p1)[:-1] / u
            z = np.array([x, 1 - y, 1])
            return self.size * z

        return transform


class Clipper:
    pass
