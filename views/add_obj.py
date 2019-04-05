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

    def on_btn_include_line_clicked(self, sender: Gtk.Button) -> None:
        self.app_handler.win_add_line.win.show()

    def on_btn_include_polygon_clicked(self, sender: Gtk.Button) -> None:
        self.app_handler.win_add_polygon.win.show()

    def on_btn_include_bezier_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_include_spline_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_include_3d_clicked(self, sender: Gtk.Button) -> None:
        pass





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

class AddLineHandler(WinAddLine):

    def on_btn_add_line_show(self, sender: Gtk.Window) -> None:
        self.entry_add_line_name.set_text("")
        self.entry_add_line_x.set_text("0.0")
        self.entry_add_line_y.set_text("0.0")
        self.entry_add_line_x2.set_text("0.0")
        self.entry_add_line_y2.set_text("0.0")

    def on_btn_add_line_clicked(self, sender: Gtk.Button) -> None:
        name = self.entry_add_line_name.get_text()
        x1 = float(self.entry_add_line_x.get_text())
        y1 = float(self.entry_add_line_y.get_text())
        x2 = float(self.entry_add_line_x2.get_text())
        y2 = float(self.entry_add_line_y2.get_text())
        self.model.add_obj(Line(name, hpt(x1, y1), hpt(x2, y2)))
        self.win.hide()

