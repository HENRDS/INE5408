import numpy as np
import geometry


class Window:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def translation_matrix(self, n):
        return geometry.translate(n, self.p1)


class Viewport:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def transformer(self, window: Window):
        v = self.bottom_right - self.top_left

        def transform(p):

            x, y = (p - window.p1)[:-1] / (window.p2 - window.p1)[:-1]
            return v * np.array([x, 1 - y, 1])

        return transform
