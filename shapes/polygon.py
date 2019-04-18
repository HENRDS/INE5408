import numpy as np
from geometry import hpt
from core import GraphicalObject, DrawContext


class Polygon(GraphicalObject):
    def __init__(self, name: str, *points):
        super().__init__(name)
        self.points = np.vstack(points)

    def draw(self, ctx: DrawContext) -> None:
        cairo_ctx = ctx.ctx
        pts = iter(self.points)
        x = ctx.viewport_transform(next(pts))
        cairo_ctx.move_to(*x[:-1])
        for p in pts:
            cairo_ctx.line_to(*ctx.viewport_transform(p)[:-1])
        cairo_ctx.line_to(*x[:-1])
        cairo_ctx.stroke()

    def draw_verbose(self, ctx: DrawContext) -> None:
        self.draw(ctx)
        cairo_ctx = ctx.ctx
        src = cairo_ctx.get_source()
        cairo_ctx.set_source_rgb(0., 1., 0.)
        for point in self.points:
            x, y = ctx.viewport_transform(point)[:-1]
            cairo_ctx.arc(x, y, 5, 0, 2 * np.pi)
            cairo_ctx.fill()
            cairo_ctx.close_path()
        cairo_ctx.set_source(src)


def rect(name: str, tl, size) -> Polygon:
    br = tl + size
    x0, y0 = tl[:-1]
    x1, y1 = br[:-1]
    return Polygon(name, hpt(x0, y0), hpt(x1, y0), hpt(x1, y1), hpt(x0, y1))
