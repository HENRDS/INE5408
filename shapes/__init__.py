from .base import GraphicalObject
from .line import Line
from .polygon import Rect, Polygon
from .point import Point
import typing as tp


class GraphicalModel:

    def __init__(self):
        self.display_file: tp.List[GraphicalObject] = []
        self.subscriptions = []

    def subscribe(self, callback):
        self.subscriptions.append(callback)

    def _update(self):
        for s in self.subscriptions:
            s()

    def add_obj(self, obj: GraphicalObject):
        self.display_file.append(obj)
        self._update()

    def objects(self, clipper=...):
        if clipper is ...:
            clipper = lambda x: x

        for obj in filter(bool, map(clipper, self.display_file)):
            yield obj







__all__ = [
    "GraphicalObject",
    "Line",
    "Point",
    "Polygon",
    "Rect"
]
