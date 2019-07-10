import numpy as np
from cairo import Context
from geometry import hpt
from util import this_source_rgb


class Viewport:
    def __init__(self, top_left, size):
        self.top_left = top_left
        self.size = size

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    @property
    def top(self):
        return self.top_left[0]

    @property
    def left(self):
        return self.top_left[1]

    def resize(self, width, height):
        size = hpt(width, height)
        self.size = size

    def draw(self, ctx: Context):
        with this_source_rgb(ctx, 1., 1., 1.):
            ctx.set_line_width(20)
            ctx.rectangle(0, 0, 894.0, 468.0)
            ctx.stroke()
        ctx.set_line_width(1)
        with this_source_rgb(ctx, 1., 0., 0.):
            ctx.rectangle(*self.top_left[:-1], *(self.top_left + self.size)[:-1])
            ctx.stroke()

    def matrix(self):
        sx, sy, _ = self.size
        x0, y0, _ = self.top_left
        return np.array(
                [[sx, 0., 0.],
                 [0., sy, 0.],
                 [x0, y0, 1.]]
        )
