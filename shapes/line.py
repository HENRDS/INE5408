from cairo import Context

from .base import GraphicalObject


class Line(GraphicalObject):

    def __init__(self, name: str, p1, p2):
        super().__init__(name)
        self.p1 = p1
        self.p2 = p2

    def draw(self, ctx: Context, transform) -> None:
        p1, p2 = transform(self.p1), transform(self.p2)
        ctx.move_to(*p1[0:-1])
        ctx.line_to(*p2[0:-1])
        ctx.stroke()


