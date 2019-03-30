from views.ui import WinAddLine, WinAddPoint
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from geometry import hpt
from shapes import Line


class AddLineHandler(WinAddLine):

    def on_btn_add_line_clicked(self, sender: Gtk.Button) -> None:
        line = Line(self.entry_add_line_name.get_text(),
                    hpt(float(self.entry_add_line_x.get_text()),
                        float(self.entry_add_line_y.get_text())),
                    hpt(float(self.entry_add_line_x2.get_text()),
                        float(self.entry_add_line_y2.get_text())))
        self.app_handler.win_main.add_obj(line)


class AddPointHandler(WinAddPoint):
    pass
