from gi.repository import Gtk
from geometry import translate, hpt, scale, rotate2D
from .ui import WinTranslate, WinScale
import numpy as np


class TranslateController(WinTranslate):

    def on_win_translate_show(self, sender: Gtk.Window) -> None:
        self.entry_translatex.set_text("0.0")
        self.entry_translatey.set_text("0.0")

    def on_btn_apply_translation_clicked(self, sender: Gtk.Button) -> None:
        from .main import MainController
        main: MainController = self.app_handler.win_main
        nm = main.get_selected_name()
        if nm is None:
            return
        selected = self.model.display_file[nm]
        x, y = float(self.entry_translatex.get_text()), float(self.entry_translatey.get_text())
        m = translate(3, hpt(x, y))
        pts = [np.matmul(p, m) for p in selected.points]
        selected.points = pts
        self.win.hide()
        main.update_screen()


class ScaleController(WinScale):

    def on_win_scale_show(self, sender: Gtk.Window) -> None:
        self.entry_scalex.set_text("0.0")
        self.entry_scaley.set_text("0.0")

    def on_btn_add_scale_clicked(self, sender: Gtk.Button) -> None:
        from .main import MainController
        main: MainController = self.app_handler.win_main
        nm = main.get_selected_name()
        if nm is None:
            return
        selected = self.model.display_file[nm]
        center = selected.center
        m = scale(hpt(float(self.entry_scalex.get_text()), float(self.entry_scaley.get_text())))
        m = np.matmul(np.matmul(translate(3, -1 * center), m), translate(3, center))
        selected.points = [np.matmul(p, m) for p in selected.points]
        self.win.hide()
        main.update_screen()
