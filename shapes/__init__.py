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
    def add_line(self, name, x0, y0, x1, y1) -> Line:
        pass

    @abc.abstractmethod
    def add_point(self, name, x, y) -> Point:
        pass

    @abc.abstractmethod
    def add_polygon(self, name) -> Polygon:
        pass

    @abc.abstractmethod
    def translate_object(self, obj, x, y) -> GraphicalObject:
        pass

    @abc.abstractmethod
    def scale_object(self, obj, x, y) -> GraphicalObject:
        pass



__all__ = [
    "GraphicalObject",
    "Line",
    "Point",
    "Polygon",
    "Rect"
]
