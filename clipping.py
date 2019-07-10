import core
from shapes import Line, Point, Polygon, Bezier
from enum import IntFlag
import typing as tp
from geometry import slope, hpt
import numpy as np
from itertools import chain


class Direction(IntFlag):
    CENTER = 0
    LEFT = 1
    RIGHT = 2
    UP = 4
    DOWN = 8


class CohenSutherland(core.Clipper):

    def snap(self, direction, v, point):
        x, y, *_ = point
        xv, yv, *_ = v
        win_p1, win_p2 = self.window._ppc
        m = 0. if xv == 0. else yv / xv
        if direction & Direction.LEFT:
            new_x = win_p1[0]
            new_y = m * (win_p1[0] - x) + y
        elif direction & Direction.RIGHT:
            new_x = win_p2[0]
            new_y = m * (new_x - x) + y
        elif direction & Direction.UP:
            new_y = win_p2[1]
            m = 1. / m if m else 0.0
            new_x = x + m * (new_y - y)
        elif direction & Direction.DOWN:
            new_y = win_p1[1]
            m = 1. / m if m else 0.0
            new_x = x + m * (new_y - y)
        else:
            new_x, new_y = x, y
        return hpt(new_x, new_y)

    def clip_line(self, line: Line) -> tp.Optional[Line]:
        p1, p2 = line._ppc
        d1, d2 = self.direction_of(p1), self.direction_of(p2)
        if not (d1 | d2):
            # completely inside the window
            return line
        elif d1 & d2:
            # completely outside the window
            return None
        new_p1 = self.snap(d1, p2 - p1, p1)
        new_p2 = self.snap(d2, p1 - p2, p2)
        line._ppc = np.vstack((new_p1, new_p2))
        return line

    def clip_point(self, pt: Point):
        x, y, _ = pt._ppc[0]
        x0, y0, _ = self.window.origin
        x1, y1, _ = self.window.origin + self.window.size
        if not (x0 < x < x1):
            return None
        if not (y0 < y < y1):
            return None
        pt._ppc = np.array([[x, y, 1.]])
        return pt

    def direction_of(self, point):
        p1, p2 = self.window._ppc
        cod = Direction.CENTER
        if point[1] > p2[1]:
            cod |= Direction.UP
        elif point[1] < p1[1]:
            cod |= Direction.DOWN

        if point[0] > p2[0]:
            cod |= Direction.RIGHT
        elif point[0] < p1[0]:
            cod |= Direction.LEFT
        return cod

    def clip_polygon(self, polygon: Polygon):
        """Sutherland-Hodgeman"""
        points = polygon._ppc
        for direction in Direction:
            if not direction:
                continue
            points = self.clip(direction, points)
            if points is None:
                return None

        polygon._ppc = points
        return polygon

    def clip_bezier(self, bezier: Bezier):
        return bezier

    def clip(self, direction: Direction, points: np.ndarray):
        n = len(points)
        new_points = []
        for i, point in enumerate(points):
            direct = self.direction_of(point)
            following = points[(i + 1) % n]
            follo_dir = self.direction_of(following)
            if direct & direction:
                if not (follo_dir & direction):
                    new_points.append(self.snap(direct, following - point, point))
                    new_points.append(following)
            else:
                if follo_dir & direction:
                    new_points.append(self.snap(follo_dir, point - following, following))
                else:
                    new_points.append(following)

        return np.vstack(new_points) if new_points else None


class LiangBarsky(CohenSutherland):
    def clip_line(self, line: Line) -> tp.Optional[Line]:
        p1, p2 = line._ppc
        win_p1, win_p2 = self.window._ppc
        point = []
        vector = p2 - p1
        u1 = 0.0
        u2 = 1.0
        p = 0
        q = 0
        r = 0
        draw = True

        for side in Direction:
            if not Direction:
                continue

            if side == Direction.LEFT:
                p = -(p2[0] - p1[0])
                q = p1[0] - win_p1[0]

            if side == Direction.RIGHT:
                p = p2[0] - p1[0]
                q = win_p2[0] - p1[0]

            if side == Direction.DOWN:
                p = -(p2[1] - p1[1])
                q = p1[1] - win_p1[1]

            if side == Direction.UP:
                p = p2[1] - p1[1]
                q = win_p2[1] - p1[1]

            if p == 0:
                p = 1

            r = q / p

            if p == 0 and q < 0:
                draw = False

            if p < 0:
                if r > u2:
                    draw = False
                if r > u1:
                    u1 = r

            if p > 0:
                if r < u1:
                    draw = False
                if r < u2:
                    u2 = r

        if draw:
            p1[0] = p1[0] + u1 * (p2[0] - p1[0])
            p1[1] = p1[1] + u1 * (p2[1] - p1[1])
            p2[0] = p1[0] + u2 * (p2[0] - p1[0])
            p1[1] = p1[1] + u2 * (p2[1] - p1[1])

            point.append(p1[0])
            point.append(p1[1])
            point.append(p2[0])
            point.append(p1[1])

        return point
