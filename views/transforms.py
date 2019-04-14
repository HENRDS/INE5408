from gi.repository import Gtk
from geometry import translate, hpt, scale, rotate2D
from .ui import WinTranslate, WinScale, WinRotate
import numpy as np


class TranslateController(WinTranslate):

    def on_btn_apply_translation_clicked(self, _: Gtk.Button) -> None:
        selected = self.model.selected
        x, y = float(self.entry_translatex.get_text()), float(self.entry_translatey.get_text())
        m = translate(3, hpt(x, y))
        pts = [np.matmul(p, m) for p in selected.points]
        selected.points = pts
        self.win.hide()
        self.model.update()


class ScaleController(WinScale):

    def on_btn_add_scale_clicked(self, _: Gtk.Button) -> None:
        selected = self.model.selected
        center = selected.center
        m = scale(hpt(float(self.entry_scalex.get_text()), float(self.entry_scaley.get_text())))
        m = np.matmul(np.matmul(translate(3, -1 * center), m), translate(3, center))
        selected.points = [np.matmul(p, m) for p in selected.points]
        self.win.hide()
        self.model.update()


class RotateController(WinRotate):
    def on_btn_apply_rotate_clicked(self, sender: Gtk.Button) -> None:
        selected = self.model.selected
        center = selected.center
        rad = float(self.entry_radian.get_text())
        m = rotate2D(rad)
        m = np.matmul(np.matmul(translate(3, -1 * center), m), translate(3, center))
        selected.points = [np.matmul(p, m) for p in selected.points]
        self.win.hide()
        self.model.update()
