from core import GraphicalModel, WindowEventHandler, Context, ApplicationHandler
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk


class WinAddLine(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.win: Gtk.Window = builder.get_object("win_add_line")
        self.entry_add_line_name: Gtk.Entry = builder.get_object("entry_add_line_name")
        self.entry_add_line_x: Gtk.Entry = builder.get_object("entry_add_line_x")
        self.entry_add_line_y: Gtk.Entry = builder.get_object("entry_add_line_y")
        self.entry_add_line_x2: Gtk.Entry = builder.get_object("entry_add_line_x2")
        self.entry_add_line_y2: Gtk.Entry = builder.get_object("entry_add_line_y2")
        self.btn_add_line: Gtk.Button = builder.get_object("btn_add_line")
        self.win.connect("activate-focus", self.on_win_add_line_activate_focus)
        # btn_add_line handlers
        self.btn_add_line.connect("clicked", self.on_btn_add_line_clicked)

    def on_win_add_line_activate_focus(self, sender: Gtk.Window) -> None:
        """Handler for event 'activate-focus' of control win_add_line."""
        pass

    def on_btn_add_line_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_line."""
        pass


class WinAddObject3D(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.win: Gtk.Window = builder.get_object("win_add_object3d")
        self.box49: Gtk.Box = builder.get_object("box49")
        self.box50: Gtk.Box = builder.get_object("box50")
        self.label32: Gtk.Label = builder.get_object("label32")
        self.entry_add_object_name: Gtk.Entry = builder.get_object("entry_add_object_name")
        self.box51: Gtk.Box = builder.get_object("box51")
        self.label33: Gtk.Label = builder.get_object("label33")
        self.entry_add_objectx: Gtk.Entry = builder.get_object("entry_add_objectx")
        self.box52: Gtk.Box = builder.get_object("box52")
        self.label34: Gtk.Label = builder.get_object("label34")
        self.entry_add_objecty: Gtk.Entry = builder.get_object("entry_add_objecty")
        self.box54: Gtk.Box = builder.get_object("box54")
        self.label35: Gtk.Label = builder.get_object("label35")
        self.entry_add_objectz: Gtk.Entry = builder.get_object("entry_add_objectz")
        self.box53: Gtk.Box = builder.get_object("box53")
        self.btn_add_vertice: Gtk.Button = builder.get_object("btn_add_vertice")
        self.btn_finish_object: Gtk.Button = builder.get_object("btn_finish_object")
        self.win.connect("activate-focus", self.on_win_add_object3d_activate_focus)
        # btn_add_vertice handlers
        self.btn_add_vertice.connect("clicked", self.on_btn_add_vertice_clicked)
        # btn_finish_object handlers
        self.btn_finish_object.connect("clicked", self.on_btn_finish_object_clicked)

    def on_win_add_object3d_activate_focus(self, sender: Gtk.Window) -> None:
        """Handler for event 'activate-focus' of control win_add_object3d."""
        pass

    def on_btn_add_vertice_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_vertice."""
        pass

    def on_btn_finish_object_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_finish_object."""
        pass


class WinAddPoint(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.win: Gtk.Window = builder.get_object("win_add_point")
        self.btn_add_point: Gtk.Button = builder.get_object("btn_add_point")
        self.win.connect("show", self.on_win_add_point_show)
        # btn_add_point handlers
        self.btn_add_point.connect("clicked", self.on_btn_add_point_clicked)

    def on_win_add_point_show(self, sender: Gtk.Window) -> None:
        """Handler for event 'show' of control win_add_point."""
        pass

    def on_btn_add_point_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_point."""
        pass


class WinAddPolygon(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.win: Gtk.Window = builder.get_object("win_add_polygon")
        self.btn_remove_polygon_point: Gtk.Button = builder.get_object("btn_remove_polygon_point")
        self.btn_add_polygon_point: Gtk.Button = builder.get_object("btn_add_polygon_point")
        self.lst_polygon_points: Gtk.ListBox = builder.get_object("lst_polygon_points")
        self.btn_add_polygon: Gtk.Button = builder.get_object("btn_add_polygon")
        self.win.connect("activate-focus", self.on_win_add_polygon_activate_focus)
        # btn_remove_polygon_point handlers
        self.btn_remove_polygon_point.connect("clicked", self.on_btn_remove_polygon_point_clicked)
        # btn_add_polygon_point handlers
        self.btn_add_polygon_point.connect("clicked", self.on_btn_add_polygon_point_clicked)
        # lst_polygon_points handlers
        self.lst_polygon_points.connect("row-activated", self.on_lst_polygon_points_row_activated)
        # btn_add_polygon handlers
        self.btn_add_polygon.connect("clicked", self.on_btn_add_polygon_clicked)

    def on_win_add_polygon_activate_focus(self, sender: Gtk.Window) -> None:
        """Handler for event 'activate-focus' of control win_add_polygon."""
        pass

    def on_btn_remove_polygon_point_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_remove_polygon_point."""
        pass

    def on_btn_add_polygon_point_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_polygon_point."""
        pass

    def on_lst_polygon_points_row_activated(self, sender: Gtk.ListBox, path: Gtk.TreePath, column: Gtk.TreeViewColumn) -> None:
        """Handler for event 'row-activated' of control lst_polygon_points."""
        pass

    def on_btn_add_polygon_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_polygon."""
        pass


class WinMain(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.win: Gtk.Window = builder.get_object("win_main")
        self.btn_new: Gtk.Button = builder.get_object("btn_new")
        self.btn_save: Gtk.Button = builder.get_object("btn_save")
        self.btn_open: Gtk.Button = builder.get_object("btn_open")
        self.tree_objects: Gtk.TreeView = builder.get_object("tree_objects")
        self.btn_add_obj: Gtk.Button = builder.get_object("btn_add_obj")
        self.btn_menu_object: Gtk.MenuButton = builder.get_object("btn_menu_object")
        self.btn_up: Gtk.Button = builder.get_object("btn_up")
        self.btn_left: Gtk.Button = builder.get_object("btn_left")
        self.btn_right: Gtk.Button = builder.get_object("btn_right")
        self.btn_down: Gtk.Button = builder.get_object("btn_down")
        self.comboboxtext_options: Gtk.ComboBoxText = builder.get_object("comboboxtext_options")
        self.btn_zoom_out: Gtk.Button = builder.get_object("btn_zoom_out")
        self.btn_zoom_in: Gtk.Button = builder.get_object("btn_zoom_in")
        self.btn_left_rotate: Gtk.Button = builder.get_object("btn_left_rotate")
        self.btn_right_rotate: Gtk.Button = builder.get_object("btn_right_rotate")
        self.btn_rotate: Gtk.Button = builder.get_object("btn_rotate")
        self.btn_menu_rotate: Gtk.MenuButton = builder.get_object("btn_menu_rotate")
        self.btn_scale: Gtk.Button = builder.get_object("btn_scale")
        self.btn_translate: Gtk.Button = builder.get_object("btn_translate")
        self.btn_delete_object: Gtk.Button = builder.get_object("btn_delete_object")
        self.btn_clean_window: Gtk.Button = builder.get_object("btn_clean_window")
        self.canvas: Gtk.DrawingArea = builder.get_object("canvas")
        self.lstLog: Gtk.ListBox = builder.get_object("lstLog")
        self.win.connect("activate-focus", self.on_main_window_clicked_focus)
        self.win.connect("key-press-event", self.on_win_main_key_press_event)
        # tree_objects handlers
        self.tree_objects.connect("row-activated", self.on_tree_objects_row_activated)
        # btn_add_obj handlers
        self.btn_add_obj.connect("clicked", self.on_btn_add_obj_clicked)
        # btn_up handlers
        self.btn_up.connect("clicked", self.on_btn_up_clicked)
        # btn_left handlers
        self.btn_left.connect("clicked", self.on_btn_left_clicked)
        # btn_right handlers
        self.btn_right.connect("clicked", self.on_btn_right_clicked)
        # btn_down handlers
        self.btn_down.connect("clicked", self.on_btn_down_clicked)
        # btn_zoom_out handlers
        self.btn_zoom_out.connect("clicked", self.on_btn_zoom_out_clicked)
        # btn_zoom_in handlers
        self.btn_zoom_in.connect("clicked", self.on_btn_zoom_in_clicked)
        # btn_left_rotate handlers
        self.btn_left_rotate.connect("clicked", self.on_btn_left_rotate_clicked)
        # btn_right_rotate handlers
        self.btn_right_rotate.connect("clicked", self.on_btn_right_rotate_clicked)
        # btn_rotate handlers
        self.btn_rotate.connect("clicked", self.on_btn_rotate_clicked)
        # btn_scale handlers
        self.btn_scale.connect("clicked", self.on_btn_scale_clicked)
        # btn_translate handlers
        self.btn_translate.connect("clicked", self.on_btn_translate_clicked)
        # btn_delete_object handlers
        self.btn_delete_object.connect("clicked", self.on_btn_delete_object_clicked)
        # btn_clean_window handlers
        self.btn_clean_window.connect("clicked", self.on_btn_clean_window_clicked)
        # canvas handlers
        self.canvas.connect("draw", self.on_canvas_draw)

    def on_main_window_clicked_focus(self, sender: Gtk.Window) -> None:
        """Handler for event 'activate-focus' of control win_main."""
        pass

    def on_win_main_key_press_event(self, sender: Gtk.Window, event: Gdk.EventKey) -> None:
        """Handler for event 'key-press-event' of control win_main."""
        pass

    def on_tree_objects_row_activated(self, sender: Gtk.TreeView, path: Gtk.TreePath, column: Gtk.TreeViewColumn) -> None:
        """Handler for event 'row-activated' of control tree_objects."""
        pass

    def on_btn_add_obj_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_obj."""
        pass

    def on_btn_up_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_up."""
        pass

    def on_btn_left_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_left."""
        pass

    def on_btn_right_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_right."""
        pass

    def on_btn_down_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_down."""
        pass

    def on_btn_zoom_out_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_zoom_out."""
        pass

    def on_btn_zoom_in_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_zoom_in."""
        pass

    def on_btn_left_rotate_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_left_rotate."""
        pass

    def on_btn_right_rotate_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_right_rotate."""
        pass

    def on_btn_rotate_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_rotate."""
        pass

    def on_btn_scale_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_scale."""
        pass

    def on_btn_translate_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_translate."""
        pass

    def on_btn_delete_object_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_delete_object."""
        pass

    def on_btn_clean_window_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_clean_window."""
        pass

    def on_canvas_draw(self, sender: Gtk.DrawingArea, ctx: Context) -> None:
        """Handler for event 'draw' of control canvas."""
        pass


class PopAddObj(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.win: Gtk.Popover = builder.get_object("pop_add_obj")
        self.btn_include_point: Gtk.Button = builder.get_object("btn_include_point")
        self.btn_include_line: Gtk.Button = builder.get_object("btn_include_line")
        self.btn_include_polygon: Gtk.Button = builder.get_object("btn_include_polygon")
        self.btn_include_spline: Gtk.Button = builder.get_object("btn_include_spline")
        self.btn_include_bezier: Gtk.Button = builder.get_object("btn_include_bezier")
        self.btn_include_3d: Gtk.Button = builder.get_object("btn_include_3d")
        # btn_include_point handlers
        self.btn_include_point.connect("clicked", self.on_btn_include_point_clicked)
        # btn_include_line handlers
        self.btn_include_line.connect("clicked", self.on_btn_include_line_clicked)
        # btn_include_polygon handlers
        self.btn_include_polygon.connect("clicked", self.on_btn_include_polygon_clicked)
        # btn_include_spline handlers
        self.btn_include_spline.connect("clicked", self.on_btn_include_spline_clicked)
        # btn_include_bezier handlers
        self.btn_include_bezier.connect("clicked", self.on_btn_include_bezier_clicked)
        # btn_include_3d handlers
        self.btn_include_3d.connect("clicked", self.on_btn_include_3d_clicked)

    def on_btn_include_point_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_include_point."""
        pass

    def on_btn_include_line_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_include_line."""
        pass

    def on_btn_include_polygon_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_include_polygon."""
        pass

    def on_btn_include_spline_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_include_spline."""
        pass

    def on_btn_include_bezier_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_include_bezier."""
        pass

    def on_btn_include_3d_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_include_3d."""
        pass


class WinRotate(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.win: Gtk.Dialog = builder.get_object("win_rotate")


class WinScale(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.win: Gtk.Dialog = builder.get_object("win_scale")
        self.btn_apply_scale: Gtk.Button = builder.get_object("btn_apply_scale")
        self.entry_scalex: Gtk.Entry = builder.get_object("entry_scalex")
        self.entry_scaley: Gtk.Entry = builder.get_object("entry_scaley")


class WinTranslate(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.win: Gtk.Dialog = builder.get_object("win_translate")
        self.btn_apply_translation: Gtk.Button = builder.get_object("btn_apply_translation")
        self.entry_translatex: Gtk.Entry = builder.get_object("entry_translatex")
        self.entry_translatey: Gtk.Entry = builder.get_object("entry_translatey")


class UI(ApplicationHandler):
    _WIN_ADD_LINE = WinAddLine
    _WIN_ADD_OBJECT3D = WinAddObject3D
    _WIN_ADD_POINT = WinAddPoint
    _WIN_ADD_POLYGON = WinAddPolygon
    _WIN_MAIN = WinMain
    _POP_ADD_OBJ = PopAddObj
    _WIN_ROTATE = WinRotate
    _WIN_SCALE = WinScale
    _WIN_TRANSLATE = WinTranslate

    def __init__(self, builder: Gtk.Builder, model: GraphicalModel = ...):
        super().__init__(builder, model)
        self.win_add_line: WinAddLine = self._WIN_ADD_LINE(self, builder)
        self.win_add_object3d: WinAddObject3D = self._WIN_ADD_OBJECT3D(self, builder)
        self.win_add_point: WinAddPoint = self._WIN_ADD_POINT(self, builder)
        self.win_add_polygon: WinAddPolygon = self._WIN_ADD_POLYGON(self, builder)
        self.win_main: WinMain = self._WIN_MAIN(self, builder)
        self.pop_add_obj: PopAddObj = self._POP_ADD_OBJ(self, builder)
        self.win_rotate: WinRotate = self._WIN_ROTATE(self, builder)
        self.win_scale: WinScale = self._WIN_SCALE(self, builder)
        self.win_translate: WinTranslate = self._WIN_TRANSLATE(self, builder)
        self.main_window.win.connect("destroy", Gtk.main_quit)


    @property
    def main_window(self):
        return self.win_main

    def show(self):
        self.main_window.win.show()