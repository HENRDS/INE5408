import numpy as np
from .base import GraphicalObject


class Polygon(GraphicalObject):
    def __init__(self, name: str, *points):
        super().__init__(name)
        self.points = points

    def draw(self, ctx, tr) -> None:
        pts = iter(self.points)
        x = tr(next(pts))
        ctx.move_to(*x[:-1])
        for p in pts:
            ctx.line_to(*tr(p)[:-1])
        ctx.line_to(*x[:-1])
        ctx.stroke()


class Rect(Polygon):
    def __init__(self, name: str, tl, size):
        br = tl + size
        x0, y0, _ = tl
        x1, y1, _ = br
        super().__init__(name, tl, np.array([x1, y0, 1]), br, np.array([x0, y1, 1]))

    @staticmethod
    def square(name, tl, side):
        return Rect(name, tl, np.array([side, side]))

