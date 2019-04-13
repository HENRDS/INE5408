import numpy as np
from cairo import Context

from core import GraphicalObject


class Polygon(GraphicalObject):
    def __init__(self, name: str, *points):
        super().__init__(name)
        self.points = points

    def draw(self, ctx: Context, transform, verbose=False) -> None:
        pts = iter(self.points)
        x = transform(next(pts))
        ctx.move_to(*x[:-1])
        for p in pts:
            ctx.line_to(*transform(p)[:-1])
        ctx.line_to(*x[:-1])
        ctx.stroke()
        if verbose:
            src = ctx.get_source()
            ctx.set_source_rgb(0., 1., 0.)
            for point in self.points:
                x, y = transform(point)[:-1]
                ctx.arc(x, y, 5, 0, 2*np.pi)
                ctx.fill()
            ctx.set_source(src)


class Rect(Polygon):
    def __init__(self, name: str, tl, size):
        br = tl + size
        x0, y0, _ = tl
        x1, y1, _ = br
        super().__init__(name, tl, np.array([x1, y0, 1]), br, np.array([x0, y1, 1]))

    @staticmethod
    def square(name, tl, side):
        return Rect(name, tl, np.array([side, side]))

