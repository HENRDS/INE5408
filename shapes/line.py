import numpy as np
from core import GraphicalObject, DrawContext
from .point import PointLike, as_ndarray


class Line(GraphicalObject):

    def __init__(self, name: str, p1: PointLike, p2: PointLike):
        super().__init__(name, np.vstack((as_ndarray(p1), as_ndarray(p2))))

    def draw_verbose(self, ctx: DrawContext) -> None:
        self.draw(ctx)
        p1, p2 = [ctx.viewport_transform(p) for p in self._ppc][:2]
        cairo_ctx = ctx.ctx
        src = cairo_ctx.get_source()
        cairo_ctx.set_source_rgb(0., 1., 0.)
        cairo_ctx.arc(*p1[:-1], 5, 0, 2 * np.pi)
        cairo_ctx.fill()
        cairo_ctx.arc(*p2[:-1], 5, 0, 2 * np.pi)
        cairo_ctx.fill()
        cairo_ctx.set_source(src)

    def draw(self, ctx: DrawContext) -> None:
        p1, p2 = [ctx.viewport_transform(p) for p in self._ppc][:2]
        cairo_ctx = ctx.ctx
        cairo_ctx.move_to(*p1[:-1])
        cairo_ctx.line_to(*p2[:-1])
        cairo_ctx.stroke()


