from views.ui import WinPoint, WinLine, WinAddPolygon, PopAddObj
import typing as tp
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from geometry import hpt
from shapes import Line, Point, Polygon


class AddObjController(PopAddObj):
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


class AddPolygonController(WinAddPolygon):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.__points = Gtk.ListStore(float, float, float)
        self.x_rt = Gtk.CellRendererText()
        self.y_rt = Gtk.CellRendererText()
        self.z_rt = Gtk.CellRendererText()
        self.x_col = Gtk.TreeViewColumn("x", self.x_rt, text=0)
        self.y_col = Gtk.TreeViewColumn("y", self.y_rt, text=1)
        self.z_col = Gtk.TreeViewColumn("z", self.z_rt, text=2)
        self.tree_polygon_points.set_model(self.__points)
        self.tree_polygon_points.append_column(self.x_col)
        self.tree_polygon_points.append_column(self.y_col)
        self.tree_polygon_points.append_column(self.z_col)

    def get_selected_name(self) -> tp.Optional[str]:
        selection = self.__points.get_selection()
        model, tree_iter = selection.get_selected()
        if tree_iter is None:
            return None
        return model[tree_iter][0]

    def on_btn_add_polygon_point_clicked(self, sender: Gtk.Button) -> None:
        self.__points.append(float(self.entry_poligonx.get_text()),
                             float(self.entry_poligony.get_text()),
                             float(self.entry_poligonz.get_text()))

    def on_btn_remove_polygon_point_clicked(self, sender: Gtk.Button) -> None:
        selection = self.__points.get_selection()
        model, tree_iter = selection.get_selected()
        if tree_iter is None:
            return None
        self.__points.remove(tree_iter)

    def on_btn_add_polygon_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_close_polygon_clicked(self, sender: Gtk.Button) -> None:
        self.win.hide()

