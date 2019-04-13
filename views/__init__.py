import numpy as np
from shapes import Line, Rect, Point
from geometry import hpt
from .ui import UI
from .main import MainController
from .add_obj import AddObjController, AddPointHandler
from .transforms import TranslateController, ScaleController
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk


class SGI(UI):
    _WIN_MAIN = MainController
    _WIN_TRANSLATE = TranslateController
    _OBJPOPOVER = AddObjController
    _WIN_ADD_POINT = AddPointHandler
    _WIN_SCALE = ScaleController

    def __init__(self, builder: Gtk.Builder):
        super().__init__(builder)
        self.model.add_obj(Line("noia", np.array([10, 10, 1]), np.array([100, 100, 1])))
        self.model.add_obj(Rect("wee", np.array([10, 10, 1]), np.array([23, 70, 0])))
        self.model.add_obj(Point("kkk", hpt(69, 69)))
        self.win_main: MainController = self.win_main


__all__ = [
    "AddObjController",
    "SGI",
    "MainController",
    "ScaleController",
    "TranslateController",
]
