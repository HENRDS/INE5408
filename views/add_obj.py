from views.ui import WinPoint, WinLine, WinAddPolygon, PopAddObj
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from geometry import hpt
from shapes import Line, Point, Polygon


class AddObjController(PopAddObj):
    def on_btn_include_point_clicked(self, sender: Gtk.Button) -> None:
        win_point = self.app_handler.win_add_point
        self.app_handler.clean_entries(win_point)
        win_point.win.show()

    def on_btn_include_line_clicked(self, sender: Gtk.Button) -> None:
        win_line = self.app_handler.win_add_line
        self.app_handler.clean_entries(win_line)
        win_line.win.show()

    def on_btn_include_polygon_clicked(self, sender: Gtk.Button) -> None:
        win_polygon = self.app_handler.win_add_polygon
        self.app_handler.clean_entries(win_polygon)
        win_polygon.win.show()

    def on_btn_include_bezier_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_include_spline_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_include_3d_clicked(self, sender: Gtk.Button) -> None:
        pass


class AddPointController(WinPoint):
    def on_btn_add_clicked(self, sender: Gtk.Button) -> None:
        name = self.entry_add_name.get_text()
        x = float(self.entry_add_pointx.get_text())
        y = float(self.entry_add_pointy.get_text())
        self.model.add_obj(Point(name, hpt(x, y)))
        self.win.hide()


class AddLineController(WinLine):
    def on_btn_add_line_clicked(self, sender: Gtk.Button) -> None:
        name = self.name_line.get_text()
        x1 = float(self.entry_x1_line.get_text())
        y1 = float(self.entry_y1_line.get_text())
        x2 = float(self.entry_x2_line.get_text())
        y2 = float(self.entry_y2_line.get_text())
        self.model.add_obj(Line(name, hpt(x1, y1), hpt(x2, y2)))
        self.win.hide()
