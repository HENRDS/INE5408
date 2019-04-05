from gi.repository import Gtk
from geometry import translate, hpt
from .ui import WinTranslate
import numpy as np

class TranslateController(WinTranslate):


    def on_win_translate_show(self, sender: Gtk.Window) -> None:
        self.entry_translatex.set_text("0.0")
        self.entry_translatey.set_text("0.0")

    def on_btn_apply_translation_clicked(self, sender: Gtk.Button) -> None:
        from .main import MainHandler
        main: MainHandler = self.app_handler.win_main
        nm = main.get_selected_name()
        if nm is None:
            return
        selected = self.model.display_file[nm]
        x, y = float(self.entry_translatex.get_text()), float(self.entry_translatey.get_text())
        m = translate(3, hpt(x, y))
        pts = [np.matmul(p, m) for p in selected.points]
        print(selected.points)
        print(m)
        print(pts)
        selected.points = pts
        self.win.hide()
        main.update_screen()





