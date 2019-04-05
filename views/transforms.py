from gi.repository import Gtk
from geometry import translate, hpt
from .ui import WinTranslate



class TranslateController(WinTranslate):
    def on_win_translate_activate_focus(self, sender: Gtk.Window) -> None:
        self.entry_translatex.set_text("0.0")
        self.entry_translatey.set_text("0.0")

    def on_btn_apply_translation_clicked(self, sender: Gtk.Button) -> None:
        # nm = self.app_handler.win_main.get_selected_name()
        # if nm is None:
        #     return
        # selected = self.model.display_file[nm]
        # self.
        # m = translate(3, hpt())
        # selected.points = []
        pass

