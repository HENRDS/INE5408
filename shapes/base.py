import numpy as np
import abc
from cairo import Context
import typing as tp


class GraphicalObject:
    def __init__(self, name: str):
        self._name = name
        self.points: tp.List[np.ndarray] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def center(self) -> np.ndarray:
        n = len(self.points)
        return sum(self.points) / n

    @abc.abstractmethod
    def draw(self, ctx: Context, transform, verbose=False) -> None:
        pass
