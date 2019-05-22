import numpy as np
from core import GraphicalObject, DrawContext
import typing as tp


class Point(GraphicalObject):

    def __init__(self, name: str, x: float, y: float, z: float = ...):
        if z is ...:
            self.is_3d = False
            super().__init__(name, np.array([[x, y, 1.]]))
        else:
            self.is_3d = True
            super().__init__(name, np.array([[x, y, z]]))



    def draw_verbose(self, ctx: DrawContext) -> None:
        self.draw(ctx)
        cairo_ctx = ctx.ctx
        x, y = ctx.viewport_transform(self._ppc[0])[:-1]
        cairo_ctx.move_to(x + 5, y + 5)
        src = cairo_ctx.get_source()
        cairo_ctx.set_source_rgb(0., 1., 0.)
        cairo_ctx.show_text(self.name)
        cairo_ctx.set_source(src)

    def draw(self, ctx: DrawContext) -> None:
        cairo_ctx = ctx.ctx
        x, y = ctx.viewport_transform(self._ppc[0])[:-1]
        cairo_ctx.arc(x, y, 5, 0, 2 * np.pi)
        cairo_ctx.fill()


PointLike = tp.Union[Point, np.ndarray, tp.Tuple[float, float], tp.Tuple[float, float, float]]


def as_ndarray(point: PointLike) -> np.ndarray:
    if isinstance(point, np.ndarray):
        return point
    elif isinstance(point, tuple):
        return np.array([*point, 1.])
    elif isinstance(point, Point):
        return point.points[0]
    else:
        raise TypeError("Invalid point.")
