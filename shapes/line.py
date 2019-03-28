from geometry.base import GraphicalObject


class Line(GraphicalObject):

    def __init__(self, name: str, p1, p2):
        super().__init__(name)
        self.points = p1, p2

    def draw(self, ctx) -> None:
        p1, p2 = self.points
        ctx.move_to(*p1[0:-1])
        ctx.line_to(*p2[0:-1])
        ctx.stroke()
