from views.ui import WinAddLine, WinAddPoint, WinScale
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from shapes import Line


class AddLineHandler(WinAddLine):

    def on_btn_add_line_clicked(self, sender: Gtk.Button) -> None:
        line = self.app_handler.model.add_line(self.entry_add_line_name.get_text(),
                                               float(self.entry_add_line_x.get_text()),
                                               float(self.entry_add_line_y.get_text()),
                                               float(self.entry_add_line_x2.get_text()),
                                               float(self.entry_add_line_y2.get_text()))

class AddPointHandler(WinAddPoint):
    def on_btn_add_point_clicked(self, sender: Gtk.Button) -> None:
        point = self.app_handler.model.add_point(self.entry_add_name.get_text(),
                                                float(self.entry_add_pointx.get_text()),
                                                float(self.entry_add_pointy.get_text()))

class WinScaleHandler(WinScale):
    def on_btn_add_escale_clicked(self, sender: Gtk.Button) -> None:
        scale = self.app_handler.model.scale_object()
