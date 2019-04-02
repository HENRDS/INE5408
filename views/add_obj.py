from views.ui import WinAddLine, WinAddPoint, WinAddPolygon
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from geometry import hpt
from shapes import Line, Point, Polygon


class AddLineHandler(WinAddLine):
    def on_btn_add_line_clicked(self, sender: Gtk.Button) -> None:
        line = Line(self.entry_add_line_name.get_text(),
                    hpt(float(self.entry_add_line_x.get_text()),
                        float(self.entry_add_line_y.get_text())),
                    hpt(float(self.entry_add_line_x2.get_text()),
                        float(self.entry_add_line_y2.get_text())))
        self.app_handler.win_main.add_obj(line)


class AddPointHandler(WinAddPoint):
    def on_win_add_point_activate_focus(self, sender: Gtk.Window) -> None:
        point = Point(self.entry_add_name.get_text(),
                      hpt(float(self.entry_add_pointx.get_text()),
                          float(self.entry_add_pointy.get_text())))
        self.app_handler.win_main.add_obj(point)


class AddPolygonHandler(WinAddPolygon):
    def on_btn_add_polygon__clicked(self, sender: Gtk.Button) -> None:
        polygon = Polygon(self.entry_add_polygon_name.get_text(),
                          float(self.entry_add_polygonx.get_text()),
                          float(self.entry_add_polygony.get_text()),
                          float(self.entry_add_polygonz.get_text()))
        self.app_handler.win_main.add_obj(polygon)



