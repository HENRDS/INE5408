import typing as tp

import gi
import numpy as np
from infra.ui import UI
from shapes import GraphicalObject, Line, Rect

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk


class SGI(UI):
    def __init__(self, builder: Gtk.Builder):
        super().__init__(builder)
        self.objects: tp.List[GraphicalObject] = []
        self.tree_model = Gtk.ListStore(str, str)
        self.name_rt = Gtk.CellRendererText()
        self.type_rt = Gtk.CellRendererText()
        self.name_col = Gtk.TreeViewColumn("Name", self.name_rt, text=0)
        self.type_col = Gtk.TreeViewColumn("Type", self.type_rt, text=1)

    def connect_model(self):
        self.tree_objects.set_model(self.tree_model)
        self.tree_objects.append_column(self.name_col)
        self.tree_objects.append_column(self.type_col)
        self.add_obj(Line("noia", np.array([10, 10, 1]), np.array([100, 100, 1])))
        self.add_obj(Rect("wee", np.array([10, 10, 1]), np.array([23, 70, 1])))

    def add_obj(self, obj: GraphicalObject):
        self.objects.append(obj)
        self.tree_model.append([obj.name, type(obj).__name__])

    def on_canvas_draw(self, sender: Gtk.DrawingArea, ctx) -> None:
        for object in self.objects:
            object.draw(ctx)

    def on_main_window_activate_focus(self, sender: Gtk.Window) -> None:
        self.canvas.queue_draw()

    def on_btn_add_object_clicked(self, sender: Gtk.Button) -> None:
        self.includeObject_window.present()

    def on_btn_include_point_clicked(self, sender: Gtk.Button) -> None:
        self.point_window.present()

    def on_btn_include_line_activate(self, sender: Gtk.Button) -> None:
        self.add_line_window.present()













