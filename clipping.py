from shapes import GraphicalObject
from enum import IntFlag
import typing as tp


class Direction(IntFlag):
    LEFT = 1
    RIGHT = 2
    UP = 4
    DOWN = 8
    CENTER = 0


class Clipper:
    def __init__(self, window):
        self.window = window

    def __call__(self, obj: GraphicalObject) -> tp.Optional[GraphicalObject]:
        return obj


class CohenSutherland(Clipper):

    def __call__(self, obj: GraphicalObject) -> tp.Optional[GraphicalObject]:
        return super().__call__(obj)
    

    def direction_of(self, point):
        cod = Direction.CENTER

        if point[1] > self.window.p2[1]:
            cod |= Direction.UP
        elif point[1] < self.window.p1[1]:
            cod |= Direction.DOWN

        if point[0] > self.window.p2[0]:
            cod |= Direction.RIGHT
        elif point[0] < self.window.p1[0]:
            cod |= Direction.LEFT

        return cod


