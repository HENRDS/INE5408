from .base import GraphicalObject
from .line import Line
from .polygon import Rect, Polygon
from .point import Point
from misc import Viewport, Window
import abc


class GraphicalModel(abc.ABC):

    @property
    @abc.abstractmethod
    def window(self) -> Window:
        pass

    @property
    @abc.abstractmethod
    def viewport(self) -> Viewport:
        pass

    @abc.abstractmethod
    def add_object(self, obj: GraphicalObject):
        pass

    @abc.abstractmethod
    def translate_object(self, x, y, obj=...) -> GraphicalObject:
        pass

    @abc.abstractmethod
    def scale_object(self, x, y, obj=...) -> GraphicalObject:
        pass


__all__ = [
    "GraphicalModel",
    "GraphicalObject",
    "Line",
    "Point",
    "Polygon",
    "Rect"
]
