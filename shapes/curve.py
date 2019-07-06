from cairo import Context
import numpy as np
from core import GraphicalObject, DrawContext


class Curve(GraphicalObject):

    def __init__(self, name: str, points: np.ndarray):
        super().__init__(name, points)


class Bezier(Curve):
    MATRIX = np.array(
            [[-1., 3., -3., 1.],
             [3., -6., 3., 0.],
             [-3., 3., 0., 0.],
             [1., 0., 0., 0.]]
    )

    def __init__(self, name: str, *points, delta=0.05):
        if len(points) % 4 != 0:
            raise RuntimeError("Invalid point number")
        new_points = []
        for i in range(0, len(points), 4):
            pts = points[i: i + 4]
            for t in np.linspace(0, 1, int(1.0 / delta)):
                new_points.append(np.array([t ** 3, t ** 2, t, 1]) @ Bezier.MATRIX @ pts)
        print(new_points)
        super().__init__(name, np.vstack(tuple(new_points)))

    def draw(self, ctx: DrawContext) -> None:
        cairo_ctx = ctx.ctx
        pts = [ctx.viewport_transform(p) for p in self._ppc]
        cairo_ctx.move_to(*pts[0][:2])
        for p in pts[1:]:
            cairo_ctx.line_to(*p[:2])
        cairo_ctx.stroke()
