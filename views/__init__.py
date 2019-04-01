import gi
import typing as tp
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from .ui import UI
from .main import MainHandler
from .add_obj import AddObjController,  AddLineHandler
import numpy as np
from shapes import Line, Rect, Point, GraphicalObject
from geometry import hpt


class SGI(UI):
    _WIN_MAIN = MainHandler
    _WIN_INCLUDE_OBJECT = AddObjController
    _WIN_ADD_LINE = AddLineHandler
    def __init__(self, builder: Gtk.Builder):
        super().__init__(builder)
        self.display_file: tp.List[GraphicalObject] = []
        self.win_main.add_obj(Line("noia", np.array([10, 10, 1]), np.array([100, 100, 1])))
        self.win_main.add_obj(Rect("wee", np.array([10, 10, 1]), np.array([23, 70, 1])))
        self.win_main.add_obj(Point("kkk", hpt(69, 69)))
        self.win_main: MainHandler = self.win_main


__all__ = [
    "SGI",
    "MainHandler",
]
