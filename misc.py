import numpy as np
import geometry
import operator as op
import functools as fn
import itertools as itt


class Window:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def translation_matrix(self, n):
        return geometry.translate(n, self.p1)


class Viewport:
    def __init__(self, top_left, size):
        self.top_left = top_left
        self.size = size

    def resize(self, width, height):
        size = geometry.hpt(width, height)
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
