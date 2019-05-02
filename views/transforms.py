from gi.repository import Gtk
from geometry import translate, hpt, scale, rotate2D, rel_transform, rad
from .ui import WinTranslate, WinScale, WinRotate
import numpy as np


class TranslateController(WinTranslate):
    def on_btn_apply_translation_clicked(self, _: Gtk.Button) -> None:
        selected = self.model.selected
        x, y = float(self.entry_translatex.get_text()), float(self.entry_translatey.get_text())
        m = translate(hpt(x, y))
        selected.points = selected.points @ m
        self.win.hide()
        self.model.update()

    def on_btn_close_translate_clicked(self, sender: Gtk.Button) -> None:
        self.win.hide()


class ScaleController(WinScale):

    def on_btn_apply_scale_clicked(self, _: Gtk.Button) -> None:
        selected = self.model.selected
        center = selected.center
        m = scale(hpt(float(self.entry_scalex.get_text()), float(self.entry_scaley.get_text())))
        m = np.matmul(np.matmul(translate(center * hpt(-1, -1)), m), translate(center))
        selected.points = np.matmul(selected.points, m)
        self.win.hide()
        self.model.update()

    def on_btn_close_scale_clicked(self, sender: Gtk.Button) -> None:
        self.win.hide()


class RotateController(WinRotate):
    def on_btn_apply_rotate_clicked(self, sender: Gtk.Button) -> None:
        selected = self.model.selected
        center = selected.center
        m = rel_transform(center, rotate2D(rad(float(self.entry_radian.get_text()))))
        selected.points = np.matmul(selected.points, m)
        self.win.hide()
        self.model.update()

    def on_btn_close_rotate_clicked(self, sender: Gtk.Button) -> None:
        self.win.hide()

