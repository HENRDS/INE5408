import gi
import typing as tp

from misc import Viewport, Window

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from .ui import UI
from .main import MainHandler
import numpy as np
from shapes import GraphicalModel, Line, Rect, Point, GraphicalObject, Polygon
from geometry import hpt, translate


class SGI(UI, GraphicalModel):
    _WIN_MAIN = MainHandler

    def __init__(self, builder: Gtk.Builder):
        super().__init__(builder, self)
        self.display_file: tp.List[GraphicalObject] = []
        self.win_main.add_obj(Line("noia", np.array([10, 10, 1]), np.array([100, 100, 1])))
        self.win_main.add_obj(Rect("wee", np.array([10, 10, 1]), np.array([23, 70, 1])))
        self.win_main.add_obj(Point("kkk", hpt(69, 69)))
        self.win_main: MainHandler = self.win_main

    def add_object(self, obj: GraphicalObject):
        self.win_main.add_obj(obj)

    @property
    def window(self) -> Window:
        return self.win_main.window

    @property
    def viewport(self) -> Viewport:
        return self.win_main.viewport

    def translate_object(self, x, y, obj=...) -> GraphicalObject:

        m = translate(3, (x, y))
        for p in obj:
            p *= m
        return obj





    def scale_object(self, x, y, obj=...) -> GraphicalObject:
        pass


__all__ = [
    "SGI",
    "MainHandler",
]
