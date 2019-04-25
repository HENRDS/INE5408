import numpy as np
from core import GraphicalObject, DrawContext


class Line(GraphicalObject):

    def __init__(self, name: str, p1, p2):
        super().__init__(name)
        self.points = np.vstack((p1, p2))

    def draw_verbose(self, ctx: DrawContext) -> None:
        self.draw(ctx)
        p1, p2 = [ctx.viewport_transform(p) for p in self.points][:2]
        cairo_ctx = ctx.ctx
        src = cairo_ctx.get_source()
        cairo_ctx.set_source_rgb(0., 1., 0.)
        cairo_ctx.arc(*p1[:-1], 5, 0, 2 * np.pi)
        cairo_ctx.fill()
        cairo_ctx.arc(*p2[:-1], 5, 0, 2 * np.pi)
        cairo_ctx.fill()
        cairo_ctx.set_source(src)

    def draw(self, ctx: DrawContext) -> None:
        p1, p2 = [ctx.viewport_transform(p) for p in self.points][:2]
        cairo_ctx = ctx.ctx
        cairo_ctx.move_to(*p1[:-1])
        cairo_ctx.line_to(*p2[:-1])
        cairo_ctx.stroke()



