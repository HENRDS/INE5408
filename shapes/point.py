import numpy as np
from cairo import Context
from .base import GraphicalObject


class Point(GraphicalObject):

    def __init__(self, name: str, pos):
        super().__init__(name)
        self.pos = pos

    def draw(self, ctx: Context, transform, verbose=False) -> None:
        x, y = transform(self.pos)[:-1]
        ctx.arc(x, y, 5, 0, 2 * np.pi)
        ctx.fill()
        if verbose:
            ctx.move_to(x + 5, y + 5)
            src = ctx.get_source()
            ctx.set_source_rgb(0., 1., 0.)
            ctx.show_text(self.name)
            ctx.set_source(src)
