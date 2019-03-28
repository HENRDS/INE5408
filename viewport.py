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

    def transform(self, window: Window, p):
        v = self.bottom_right - self.top_left
        u = np.array([0., -1.])
        return v * (u - ((p - window.p1) / (window.p2 - window.p1)))





