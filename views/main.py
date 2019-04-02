from views.ui import WinMain
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from shapes import GraphicalObject
from misc import Window, Viewport
from geometry import hpt
import  typing as tp


class MainHandler(WinMain):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        w, h = float(self.canvas.get_allocated_width()), float(self.canvas.get_allocated_height())
        print(w, h)
        self.window = Window(hpt(0., 0.), hpt(w, h))
        self.viewport = Viewport(hpt(0., 0.), hpt(w, h))
        self.tree_model = Gtk.ListStore(str, str, )
        self.name_rt = Gtk.CellRendererText()
        self.type_rt = Gtk.CellRendererText()
        self.name_col = Gtk.TreeViewColumn("Name", self.name_rt, text=0)
        self.type_col = Gtk.TreeViewColumn("Type", self.type_rt, text=1)
        self.connect_model()

    def connect_model(self):
        self.tree_objects.set_model(self.tree_model)
        self.tree_objects.append_column(self.name_col)
        self.tree_objects.append_column(self.type_col)


    def add_obj(self, obj: GraphicalObject):
        self.app_handler.display_file.append(obj)
        self.tree_model.append([obj.name, type(obj).__name__])

    def on_main_window_clicked_focus(self, sender: Gtk.Window) -> None:
        self.canvas.draw_queue()

    def on_canvas_draw(self, sender: Gtk.DrawingArea, ctx) -> None:
        tr = self.viewport.transformer(self.window)
        for obj in self.app_handler.display_file:
            obj.draw(ctx, tr)

    def on_btn_add_object_clicked(self, sender: Gtk.Button) -> None:
        self.app_handler.win_include_object.win.show()

    def on_btn_up_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_left_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_right_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_down_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_zoom_out_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_zoom_in_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_left_rotate_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_right_rotate_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_scale_clicked(self, sender: Gtk.Button) -> None:
        self.app_handler.win_scale.present()

    def on_btn_translate_clicked(self, sender: Gtk.Button) -> None:
        self.app_handler.win_translate.present()



