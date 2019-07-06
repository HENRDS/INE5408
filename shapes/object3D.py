import numpy as np
from core import GraphicalObject, DrawContext

class Object3d (GraphicalObject):

    def segments(self):
        for s in zip(self._ppc[:-1], self._ppc[1:]):
            yield s

    def draw(self, ctx: DrawContext) -> None:
        list_points = [ctx.viewport_transform(p) for p in self._ppc]
        cairo_ctx = ctx.ctx
        cairo_ctx.move_to(*list_points[:-1])
        cairo_ctx.line_to(*list_points[:-1])
        cairo_ctx.stroke()



