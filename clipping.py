import core
from shapes import Line, Point
from enum import IntFlag
import typing as tp


class Direction(IntFlag):
    CENTER = 0
    LEFT = 1
    RIGHT = 2
    UP = 4
    DOWN = 8


class CohenSutherland(core.Clipper):
    def clip_line(self, line: Line):
        p1, p2 = line.points
        d1, d2 = self.direction_of(p1), self.direction_of(p2)
        if (d1 | d2) == Direction.CENTER:
            return line
        elif d1 != Direction.CENTER:




    def clip_point(self, pt: Point):
        x, y, _ = pt.points[0]
        x0, y0, _ = self.window.origin
        x1, y1, _ = self.window.origin + self.window.size
        if not (x0 < x < x1):
            return None
        if not (y0 < y < y1):
            return None
        return pt

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
