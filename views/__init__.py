import numpy as np
from shapes import Line, rect, Point
from geometry import hpt
from .ui import UI
from .main import MainController
from .add_obj import AddObjController, AddPointController, AddLineController, AddPolygonController
from .transforms import TranslateController, ScaleController, RotateController
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')


class SGI(UI):
    _WIN_MAIN = MainController
    _POP_ADD_OBJ = AddObjController
    _WIN_ADD_POLYGON = AddPolygonController
    _WIN_POINT = AddPointController
    _WIN_LINE = AddLineController
    _WIN_TRANSLATE = TranslateController
    _WIN_SCALE = ScaleController
    _WIN_ROTATE = RotateController

    def __init__(self):
        super().__init__()
        self.model.add_obj(Line("noia", np.array([10, 10, 1]), np.array([100, 100, 1])))
        self.model.add_obj(rect("wee", np.array([10, 10, 1]), np.array([80, 80, 0])))
        self.model.add_obj(Point("kkk", 69, 69))
        self.win_main: MainController = self.win_main


__all__ = [
    "AddObjController",
    "SGI",
    "MainController",
    "ScaleController",
    "TranslateController",
    "RotateController"
]
