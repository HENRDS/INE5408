import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from .ui import UI
from .main import MainHandler
import numpy as np
from shapes import Line, Rect


class SGI(UI):
    _WIN_MAIN = MainHandler

    def __init__(self, builder: Gtk.Builder):
        super().__init__(builder)
        self.win_main.add_obj(Line("noia", np.array([10, 10, 1]), np.array([100, 100, 1])))
        self.win_main.add_obj(Rect("wee", np.array([10, 10, 1]), np.array([23, 70, 1])))


__all__ = [
    "SGI",
    "MainHandler",
]
