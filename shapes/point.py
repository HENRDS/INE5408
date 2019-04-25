import numpy as np
from core import GraphicalObject, DrawContext


class Point(GraphicalObject):

    def __init__(self, name: str, pos):
        super().__init__(name)
        self.points = np.array([pos])

    def draw_verbose(self, ctx: DrawContext) -> None:
        self.draw(ctx)
        cairo_ctx = ctx.ctx
        x, y = ctx.viewport_transform(self.points[0])[:-1]
        cairo_ctx.move_to(x + 5, y + 5)
        src = cairo_ctx.get_source()
        cairo_ctx.set_source_rgb(0., 1., 0.)
        cairo_ctx.show_text(self.name)
        cairo_ctx.set_source(src)

    def draw(self, ctx: DrawContext) -> None:
        cairo_ctx = ctx.ctx
        x, y = ctx.viewport_transform(self.points[0])[:-1]
        cairo_ctx.arc(x, y, 5, 0, 2 * np.pi)
        cairo_ctx.fill()


