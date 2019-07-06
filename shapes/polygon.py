import numpy as np
from geometry import hpt
from core import GraphicalObject, DrawContext
from util import this_source_rgb
from .point import PointLike, as_ndarray


class Polygon(GraphicalObject):
    def __init__(self, name: str, *points: PointLike):
        t = tuple((as_ndarray(p) for p in points))
        super().__init__(name, np.vstack(t))
        self.points = np.vstack(points)

    def draw(self, ctx: DrawContext) -> None:
        cairo_ctx = ctx.ctx
        pts = iter(self._ppc)
        x = ctx.viewport_transform(next(pts))
        cairo_ctx.move_to(*x[:-1])
        for p in pts:
            cairo_ctx.line_to(*ctx.viewport_transform(p)[:-1])
        cairo_ctx.line_to(*x[:-1])
        cairo_ctx.stroke()

    def draw_verbose(self, ctx: DrawContext) -> None:
        self.draw(ctx)
        cairo_ctx = ctx.ctx
        with this_source_rgb(cairo_ctx, 0., 1., 0.):
            for point in self._ppc:
                x, y = ctx.viewport_transform(point)[:-1]
                cairo_ctx.arc(x, y, 5, 0, 2 * np.pi)
                cairo_ctx.fill()
                cairo_ctx.close_path()


def rect(name: str, tl, size) -> Polygon:
    br = tl + size
    x0, y0 = tl[:-1]
    x1, y1 = br[:-1]
    return Polygon(name, hpt(x0, y0), hpt(x1, y0), hpt(x1, y1), hpt(x0, y1))
