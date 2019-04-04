from views.ui import WinAddLine, WinAddPoint, WinAddPolygon, Objpopover
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from geometry import hpt
from shapes import Line, Point, Polygon


class AddObjController(Objpopover):
    def on_btn_include_point_clicked(self, sender: Gtk.Button) -> None:
        self.app_handler.win_add_point.win.show()


class AddLineHandler(WinAddLine):
    def on_btn_add_line_clicked(self, sender: Gtk.Button) -> None:
        fields = (self.entry_add_line_x,
                  self.entry_add_line_y,
                  self.entry_add_line_x2,
                  self.entry_add_line_y2)
        for f in fields:
            if not f.get_text().is_num():
                f.set_tooltip_text("Invalid Number")


class AddPointHandler(WinAddPoint):

    def on_win_add_point_show(self, sender: Gtk.Window) -> None:
        self.entry_add_name.set_text("")
        self.entry_add_pointx.set_text("0.0")
        self.entry_add_pointy.set_text("0.0")

    def on_btn_add_point_clicked(self, sender: Gtk.Button) -> None:
        name = self.entry_add_name.get_text()
        x = float(self.entry_add_pointx.get_text())
        y = float(self.entry_add_pointy.get_text())
        self.model.add_obj(Point(name, hpt(x, y)))
        self.win.hide()


class AddPolygonHandler(WinAddPolygon):
    def on_btn_add_polygon__clicked(self, sender: Gtk.Button) -> None:
        polygon = Polygon(self.entry_add_polygon_name.get_text(),
                          float(self.entry_add_polygonx.get_text()),
                          float(self.entry_add_polygony.get_text()),
                          float(self.entry_add_polygonz.get_text()))
        self.app_handler.win_main.add_obj(polygon)
