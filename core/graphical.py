import abc
import numpy as np
from .viewport import Viewport
from .window import Window
from cairo import Context
from geometry import hpt


class DrawContext:
    def __init__(self, viewport: Viewport, win: Window, ctx: Context):
        self.viewport = viewport
        self.win = win
        self.ctx = ctx

    def viewport_transform(self, p):
        x, y, _ = (p - self.win._ppc[0]) / self.win.size
        return hpt(x, 1 - y) @ self.viewport.matrix()


class GraphicalObject:
    def __init__(self, name: str, points: np.ndarray):
        self._name = name
        self.points: np.ndarray = points
        self._ppc: np.ndarray = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def center(self) -> np.ndarray:
        n = len(self.points[:, 0])
        c = sum(self.points)
        return c / n

    @abc.abstractmethod
    def draw(self, ctx: DrawContext) -> None:
        pass

    def draw_verbose(self, ctx: DrawContext) -> None:
        self.draw(ctx)
