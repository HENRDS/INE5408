import gi
import typing as tp

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from .ui import UI
from .main import MainHandler
from .add_obj import AddObjController, AddPointHandler
import numpy as np
from shapes import Line, Rect, Point, GraphicalObject
from geometry import hpt
from .transforms import TranslateController


class SGI(UI):
    _WIN_MAIN = MainHandler
    # _WIN_ADD_LINE = AddLineHandler
    _WIN_TRANSLATE = TranslateController
    _OBJPOPOVER = AddObjController
    _WIN_ADD_POINT = AddPointHandler

    def __init__(self, builder: Gtk.Builder):
        super().__init__(builder)
        self.model.add_obj(Line("noia", np.array([10, 10, 1]), np.array([100, 100, 1])))
        self.model.add_obj(Rect("wee", np.array([10, 10, 1]), np.array([23, 70, 0])))
        self.model.add_obj(Point("kkk", hpt(69, 69)))
        self.win_main: MainHandler = self.win_main


__all__ = [
    "SGI",
    "MainHandler",
]
