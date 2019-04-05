from cairo import Context
import numpy as np
from .base import GraphicalObject


class Line(GraphicalObject):

    def __init__(self, name: str, p1, p2):
        super().__init__(name)
        self.p1 = p1
        self.p2 = p2

    def draw(self, ctx: Context, transform, verbose=False) -> None:
        p1, p2 = transform(self.p1), transform(self.p2)
        ctx.move_to(*p1[:-1])
        ctx.line_to(*p2[:-1])
        ctx.stroke()
        if verbose:
            src = ctx.get_source()
            ctx.set_source_rgb(0., 1., 0.)
            ctx.arc(*p1[:-1], 5, 0, 2 * np.pi)
            ctx.fill()
            ctx.arc(*p2[:-1], 5, 0, 2 * np.pi)
            ctx.fill()
            ctx.set_source(src)
