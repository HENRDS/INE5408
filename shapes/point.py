import numpy as np
from cairo import Context
from .base import GraphicalObject


class Point(GraphicalObject):

    def __init__(self, name: str, pos):
        super().__init__(name)
        self.pos = pos

    def draw(self, ctx: Context) -> None:
        x, y = self.pos
        ctx.arc(x, y, 5, 0, 2 * np.pi)
        ctx.fill()
