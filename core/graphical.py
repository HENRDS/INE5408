import abc
import numpy as np
from .viewport import Viewport
from .window import Window
from cairo import Context
from geometry import hpt



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

    @abc.abstractmethod
    def draw_verbose(self, ctx: DrawContext) -> None:
        pass
