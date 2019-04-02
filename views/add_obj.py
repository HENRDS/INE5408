from views.ui import WinAddLine, WinAddPoint, WinAddPolygon, WinIncludeObject
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from geometry import hpt
from shapes import Line, Point, Polygon


class AddObjController(WinIncludeObject):

    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.selected_window: Gtk.Window = None
        print("AddObjController in da house!")

    def on_btn_include_point_clicked(self, sender: Gtk.Button) -> None:
        self.selected_window = self.app_handler.win_add_point.win
        self.win.close()

    def on_btn_include_polygon_clicked(self, sender: Gtk.Button) -> None:
        self.selected_window = self.app_handler.win_add_polygon.win
        self.win.close()

    def on_btn_include_line_clicked(self, sender: Gtk.Button) -> None:
        self.selected_window = self.app_handler.win_add_line.win
        self.win.close()

        # line = Line(self.entry_add_line_name.get_text(),
        #             hpt(float(self.entry_add_line_x.get_text()),
        #                 float(self.entry_add_line_y.get_text())),
        #             hpt(float(self.entry_add_line_x2.get_text()),
        #                 float(self.entry_add_line_y2.get_text()))

    def on_btn_include_spline_clicked(self, sender: Gtk.Button) -> None:
        raise NotImplemented

    def on_btn_include_object3d_clicked(self, sender: Gtk.Button) -> None:
        raise NotImplemented

    def on_btn_include_bezier_clicked(self, sender: Gtk.Button) -> None:
        raise NotImplemented

    def on_win_include_object_destroy(self, sender: Gtk.Window) -> None:
        print("destroy")

    def on_win_include_object_hide(self, sender: Gtk.Window) -> None:
        print("hide")

    def on_win_include_object_realize(self, sender: Gtk.Window) -> None:
        print("realize")

    def on_win_include_object_show(self, sender: Gtk.Window) -> None:
        print("show")
        self.selected_window = None


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
    def on_win_add_point_activate_focus(self, sender: Gtk.Window) -> None:
        pass


class AddPolygonHandler(WinAddPolygon):
    def on_btn_add_polygon_clicked(self, sender: Gtk.Button) -> None:
        polygon = Polygon(self.entry_add_polygon_name.get_text(),
                          float(self.entry_add_polygonx.get_text()),
                          float(self.entry_add_polygony.get_text()),
                          float(self.entry_add_polygonz.get_text()))
        self.app_handler.win_main.add_obj(polygon)

