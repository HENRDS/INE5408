
from .base import GraphicalObject


class Polygon(GraphicalObject):
    def __init__(self, name: str, *points):
        super().__init__(name)
        self.points = points

    def draw(self, ctx) -> None:
        pass

