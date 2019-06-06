from core import Viewport, DrawContext, GraphicalObject
import gi

from views.ui import WinMain

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk
from geometry import hpt, rotate2D, rad, rel_transform
import typing as tp
import numpy as np
from .ui import UI


class MainController(WinMain):
    def __init__(self, app_handler: UI, builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.app_handler: UI = app_handler
        self._step = 10.0
        self.viewport = Viewport(hpt(10., 10.), hpt(400., 400.))
        self.name_rt = Gtk.CellRendererText()
        self.type_rt = Gtk.CellRendererText()
        self.name_col = Gtk.TreeViewColumn("Name", self.name_rt, text=0)
        self.type_col = Gtk.TreeViewColumn("Type", self.type_rt, text=1)
        self.tree_objects.set_model(app_handler.lst_store_objects)
        self.tree_objects.append_column(self.name_col)
        self.tree_objects.append_column(self.type_col)
        self.model.subscribe("draw", self.update_screen)
        self.model.subscribe("add", self.on_add_object)
        self.no_shift = {
            Gdk.KEY_Up: self.on_btn_up_clicked,
            Gdk.KEY_Down: self.on_btn_down_clicked,
            Gdk.KEY_Left: self.on_btn_left_clicked,
            Gdk.KEY_Right: self.on_btn_right_clicked,
        }
        self.with_ctrl = {
            Gdk.KEY_Up: self.on_btn_zoom_in_clicked,
            Gdk.KEY_Down: self.on_btn_zoom_out_clicked,
            Gdk.KEY_Left: self.on_btn_left_rotate_clicked,
            Gdk.KEY_Right: self.on_btn_right_rotate_clicked,
            Gdk.KEY_plus: self.on_btn_zoom_in_clicked,
            Gdk.KEY_minus: self.on_btn_zoom_out_clicked,
        }

    def update_screen(self):
        self.canvas.queue_draw()

    def on_add_object(self, obj: GraphicalObject):
        self.app_handler.lst_store_objects.append([obj.name, obj.__class__.__name__])

    def get_selected_name(self) -> tp.Optional[str]:
        selection = self.tree_objects.get_selection()
        model, tree_iter = selection.get_selected()
        if tree_iter is None:
            return None
        return model[tree_iter][0]

    def on_win_main_key_press_event(self, sender: Gtk.Window, event: Gdk.EventKey) -> None:
        _, val = event.get_keyval()
        if event.get_state() & Gdk.ModifierType.CONTROL_MASK:
            meth = self.with_ctrl.get(val)
        else:
            meth = self.no_shift.get(val)
        if meth is not None:
            meth(None)

    def on_canvas_draw(self, sender: Gtk.DrawingArea, ctx) -> None:
        # self.viewport.resize(float(self.canvas.get_allocated_width()) - 20.,
        #                      float(self.canvas.get_allocated_height()) - 20.)

        draw_ctx = DrawContext(self.viewport, self.model.window, ctx)
        from clipping import CohenSutherland
        for obj in self.model.objects(CohenSutherland(self.model.window)):
            if obj.name == self.get_selected_name():
                ctx.set_source_rgb(1., 0., 0.)
                obj.draw_verbose(draw_ctx)
                ctx.set_source_rgb(0., 0., 0.)
            else:
                obj.draw(draw_ctx)
        self.viewport.draw(ctx)

    def on_btn_new_clicked(self, sender: Gtk.Button) -> None:
        super().on_btn_new_clicked(sender)

    def on_tree_objects_row_activated(self, sender: Gtk.TreeView, path: Gtk.TreePath,
                                      column: Gtk.TreeViewColumn) -> None:
        self.model.selected_name = self.get_selected_name()
        self.update_screen()

    def on_btn_up_clicked(self, sender: Gtk.Button) -> None:
        self.model.window.move_up(self._step)
        self.model.update()

    def on_btn_left_clicked(self, sender: Gtk.Button) -> None:
        self.model.window.move_left(self._step)
        self.update_screen()

    def on_btn_right_clicked(self, sender: Gtk.Button) -> None:
        self.model.window.move_right(self._step)
        self.update_screen()

    def on_btn_down_clicked(self, sender: Gtk.Button) -> None:
        self.model.window.move_down(self._step)
        self.update_screen()

    def on_btn_zoom_out_clicked(self, sender: Gtk.Button) -> None:
        self.model.window.zoom_out(self._step)
        self.model.update()

    def on_btn_zoom_in_clicked(self, sender: Gtk.Button) -> None:
        self.model.window.zoom_in(self._step)
        self.model.update()

    def on_btn_right_rotate_clicked(self, sender: Gtk.Button) -> None:
        self.model.window.rotate(self._step)
        self.model.update()

    def on_btn_left_rotate_clicked(self, sender: Gtk.Button) -> None:
        self.model.window.rotate(-self._step)
        self.model.update()

    def on_btn_scale_clicked(self, sender: Gtk.Button) -> None:
        if self.get_selected_name() is None:
            return
        win_scal = self.app_handler.win_scale
        self.app_handler.clean_entries(win_scal)
        win_scal.win.show()

    def on_btn_translate_clicked(self, sender: Gtk.Button) -> None:
        if self.get_selected_name() is None:
            return
        win_trans = self.app_handler.win_translate
        self.app_handler.clean_entries(win_trans)
        win_trans.win.show()

    def on_btn_add_obj_clicked(self, sender: Gtk.Button) -> None:
        self.app_handler.pop_add_obj.win.show()

    def on_btn_rotate_clicked(self, sender: Gtk.Button) -> None:
        win_rot = self.app_handler.win_rotate
        self.app_handler.clean_entries(win_rot)
        win_rot.win.show()

    def on_btn_delete_object_clicked(self, sender: Gtk.Button) -> None:
        if self.model.selected is None:
            return
        selection = self.tree_objects.get_selection()
        nm = self.get_selected_name()
        _, tree_iter = selection.get_selected()
        self.app_handler.lst_store_objects.remove(tree_iter)
        del self.model.display_file[nm]
        self.model.selected_name = self.get_selected_name()
        self.model.update()

    def on_btn_open_clicked(self, sender: Gtk.Button) -> None:
        pass
