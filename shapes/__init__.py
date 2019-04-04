from .base import GraphicalObject
from .line import Line
from .polygon import Rect, Polygon
from .point import Point
import typing as tp
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository.Gtk import ListStore
from misc import Window
from geometry import hpt


class GraphicalModel:

    def __init__(self):
        self.display_file: tp.Dict[str, GraphicalObject] = {}
        self.subscriptions = []
        self.list_model: ListStore = ListStore(str, str)
        self.window = Window(hpt(0., 0.), hpt(800., 600.))

    def subscribe(self, callback):
        self.subscriptions.append(callback)

    def _update(self):
        for s in self.subscriptions:
            s()

    def add_obj(self, obj: GraphicalObject):
        self.display_file[obj.name] = obj
        self.list_model.append([obj.name, obj.__class__.__name__])
        self._update()

    def objects(self, clipper=...):
        if clipper is ...:
            clipper = lambda x: x
        for obj in map(clipper, self.display_file.values()):
            if obj is not None:
                yield obj



__all__ = [
    "GraphicalObject",
    "Line",
    "Point",
    "Polygon",
    "Rect"
]
