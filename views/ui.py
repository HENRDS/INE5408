from shapes import GraphicalObject
from cairo import Context
from typing import List
from weakref import proxy
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk, GObject


class WinAddLine:
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        self.app_handler: "UI" = proxy(app_handler)
        self.win: Gtk.Window = builder.get_object("win_add_line")
        self.entry_add_line_name: Gtk.Entry = builder.get_object("entry_add_line_name")
        self.entry_add_line_x: Gtk.Entry = builder.get_object("entry_add_line_x")
        self.entry_add_line_y: Gtk.Entry = builder.get_object("entry_add_line_y")
        self.entry_add_line_x2: Gtk.Entry = builder.get_object("entry_add_line_x2")
        self.entry_add_line_y2: Gtk.Entry = builder.get_object("entry_add_line_y2")
        self.btn_add_line: Gtk.Button = builder.get_object("btn_add_line")
        # btn_add_line
        self.btn_add_line.connect("clicked", self.on_btn_add_line_clicked)

    def on_btn_add_line_clicked(self, sender: Gtk.Button) -> None:
        pass


class WinAddObject3D:
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        self.app_handler: "UI" = proxy(app_handler)
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
        # btn_add_vertice
        self.btn_add_vertice.connect("clicked", self.on_btn_add_vertice_clicked)
        # btn_finish_object
        self.btn_finish_object.connect("clicked", self.on_btn_finish_object_clicked)

    def on_btn_add_vertice_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_finish_object_clicked(self, sender: Gtk.Button) -> None:
        pass


class WinAddPoint:
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        self.app_handler: "UI" = proxy(app_handler)
        self.win: Gtk.Window = builder.get_object("win_add_point")
        self.entry_add_name: Gtk.Entry = builder.get_object("entry_add_name")
        self.entry_add_pointx: Gtk.Entry = builder.get_object("entry_add_pointx")
        self.entry_add_pointy: Gtk.Entry = builder.get_object("entry_add_pointy")


class WinAddPolygon:
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        self.app_handler: "UI" = proxy(app_handler)
        self.win: Gtk.Window = builder.get_object("win_add_polygon")
        self.entry_add_polygon_name: Gtk.Entry = builder.get_object("entry_add_polygon_name")
        self.entry_add_polygonx: Gtk.Entry = builder.get_object("entry_add_polygonx")
        self.entry_add_polygony: Gtk.Entry = builder.get_object("entry_add_polygony")
        self.entry_add_polygonz: Gtk.Entry = builder.get_object("entry_add_polygonz")
        self.btn_add_polygon: Gtk.Button = builder.get_object("btn_add_polygon")
        # btn_add_polygon
        self.btn_add_polygon.connect("clicked", self.on_btn_add_polygon_clicked)

    def on_btn_add_polygon_clicked(self, sender: Gtk.Button) -> None:
        pass


class WinScale:
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        self.app_handler: "UI" = proxy(app_handler)
        self.win: Gtk.Window = builder.get_object("win_scale")
        self.entry_escalex: Gtk.Entry = builder.get_object("entry_escalex")
        self.entry_escaley: Gtk.Entry = builder.get_object("entry_escaley")
        self.btn_add_escale: Gtk.Button = builder.get_object("btn_add_escale")
        # btn_add_escale
        self.btn_add_escale.connect("clicked", self.on_btn_add_escale_clicked)

    def on_btn_add_escale_clicked(self, sender: Gtk.Button) -> None:
        pass


class WinIncludeObject:
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        self.app_handler: "UI" = proxy(app_handler)
        self.win: Gtk.Window = builder.get_object("win_include_object")
        self.btn_include_point: Gtk.Button = builder.get_object("btn_include_point")
        self.btn_include_polygon: Gtk.Button = builder.get_object("btn_include_polygon")
        self.btn_include_line: Gtk.Button = builder.get_object("btn_include_line")
        self.btn_include_spline: Gtk.Button = builder.get_object("btn_include_spline")
        self.btn_include_object3d: Gtk.Button = builder.get_object("btn_include_object3d")
        self.btn_include_bezier: Gtk.Button = builder.get_object("btn_include_bezier")
        # btn_include_point
        self.btn_include_point.connect("clicked", self.on_btn_include_point_clicked)
        # btn_include_polygon
        self.btn_include_polygon.connect("clicked", self.on_btn_include_polygon_clicked)
        # btn_include_line
        self.btn_include_line.connect("clicked", self.on_btn_include_line_clicked)
        # btn_include_spline
        self.btn_include_spline.connect("clicked", self.on_btn_include_spline_clicked)
        # btn_include_object3d
        self.btn_include_object3d.connect("clicked", self.on_btn_include_object3d_clicked)
        # btn_include_bezier
        self.btn_include_bezier.connect("clicked", self.on_btn_include_bezier_clicked)

    def on_btn_include_point_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_include_polygon_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_include_line_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_include_spline_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_include_object3d_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_btn_include_bezier_clicked(self, sender: Gtk.Button) -> None:
        pass


class WinMain:
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        self.app_handler: "UI" = proxy(app_handler)
        self.win: Gtk.Window = builder.get_object("win_main")
        self.btn_new: Gtk.Button = builder.get_object("btn_new")
        self.btn_save: Gtk.Button = builder.get_object("btn_save")
        self.btn_open: Gtk.Button = builder.get_object("btn_open")
        self.tree_objects: Gtk.TreeView = builder.get_object("tree_objects")
        self.btn_add_object: Gtk.Button = builder.get_object("btn_add_object")
        self.btn_up: Gtk.Button = builder.get_object("btn_up")
        self.btn_left: Gtk.Button = builder.get_object("btn_left")
        self.btn_right: Gtk.Button = builder.get_object("btn_right")
        self.btn_down: Gtk.Button = builder.get_object("btn_down")
        self.comboboxtext_options: Gtk.ComboBoxText = builder.get_object("comboboxtext_options")
        self.btn_zoom_out: Gtk.Button = builder.get_object("btn_zoom_out")
        self.btn_zoom_in: Gtk.Button = builder.get_object("btn_zoom_in")
        self.btn_left_rotate: Gtk.Button = builder.get_object("btn_left_rotate")
        self.btn_right_rotate: Gtk.Button = builder.get_object("btn_right_rotate")
        self.btn_rotate_object: Gtk.Button = builder.get_object("btn_rotate_object")
        self.btn_rotate_world: Gtk.Button = builder.get_object("btn_rotate_world")
        self.btn_rotate_specific: Gtk.Button = builder.get_object("btn_rotate_specific")
        self.btn_scale: Gtk.Button = builder.get_object("btn_scale")
        self.btn_translate: Gtk.Button = builder.get_object("btn_translate")
        self.canvas: Gtk.DrawingArea = builder.get_object("canvas")
        self.lstLog: Gtk.ListBox = builder.get_object("lstLog")
        # btn_add_object
        self.btn_add_object.connect("clicked", self.on_btn_add_object_clicked)
        # btn_up
        self.btn_up.connect("clicked", self.on_btn_up_clicked)
        # btn_left
        self.btn_left.connect("clicked", self.on_btn_left_clicked)
        # btn_right
        self.btn_right.connect("clicked", self.on_btn_right_clicked)
        # btn_down
        self.btn_down.connect("clicked", self.on_btn_down_clicked)
        # btn_zoom_out
        self.btn_zoom_out.connect("clicked", self.on_btn_zoom_out_clicked)
        # btn_zoom_in
        self.btn_zoom_in.connect("clicked", self.on_btn_zoom_in_clicked)
        # btn_left_rotate
        self.btn_left_rotate.connect("clicked", self.on_btn_left_rotate_clicked)
        # btn_right_rotate
        self.btn_right_rotate.connect("clicked", self.on_btn_right_rotate_clicked)
        # btn_scale
        self.btn_scale.connect("clicked", self.on_btn_scale_clicked)
        # btn_translate
        self.btn_translate.connect("clicked", self.on_btn_translate_clicked)
        # canvas
        self.canvas.connect("draw", self.on_canvas_draw)

    def on_main_window_clicked_focus(self, sender: Gtk.Window) -> None:
        pass

    def on_btn_add_object_clicked(self, sender: Gtk.Button) -> None:
        pass

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
        pass

    def on_btn_translate_clicked(self, sender: Gtk.Button) -> None:
        pass

    def on_canvas_draw(self, sender: Gtk.DrawingArea, ctx: Context) -> None:
        pass


class WinTranslate:
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        self.app_handler: "UI" = proxy(app_handler)
        self.win: Gtk.Window = builder.get_object("win_translate")
        self.entry_translatex: Gtk.Entry = builder.get_object("entry_translatex")
        self.entry_translatey: Gtk.Entry = builder.get_object("entry_translatey")
        self.btn_apply_translation: Gtk.Button = builder.get_object("btn_apply_translation")
        # btn_apply_translation
        self.btn_apply_translation.connect("clicked", self.on_btn_apply_translation_clicked)

    def on_btn_apply_translation_clicked(self, sender: Gtk.Button) -> None:
        pass


class UI:
    _WIN_ADD_LINE = WinAddLine
    _WIN_ADD_OBJECT3D = WinAddObject3D
    _WIN_ADD_POINT = WinAddPoint
    _WIN_ADD_POLYGON = WinAddPolygon
    _WIN_SCALE = WinScale
    _WIN_INCLUDE_OBJECT = WinIncludeObject
    _WIN_MAIN = WinMain
    _WIN_TRANSLATE = WinTranslate

    def __init__(self, builder: Gtk.Builder):
        self.display_file: List[GraphicalObject] = []
        self.win_add_line: Gtk.Window = self._WIN_ADD_LINE(self, builder)
        self.win_add_object3d: Gtk.Window = self._WIN_ADD_OBJECT3D(self, builder)
        self.win_add_point: Gtk.Window = self._WIN_ADD_POINT(self, builder)
        self.win_add_polygon: Gtk.Window = self._WIN_ADD_POLYGON(self, builder)
        self.win_scale: Gtk.Window = self._WIN_SCALE(self, builder)
        self.win_include_object: Gtk.Window = self._WIN_INCLUDE_OBJECT(self, builder)
        self.win_main: Gtk.Window = self._WIN_MAIN(self, builder)
        self.win_translate: Gtk.Window = self._WIN_TRANSLATE(self, builder)
        self.adjustment1: Gtk.Adjustment = builder.get_object("btn_apply_translation")

        # btn_apply_translation
        self.win_main.win.connect("destroy", Gtk.main_quit)

    def show(self):
        self.win_main.win.show()

    def on_btn_apply_translation_clicked(self, sender: Gtk.Button) -> None:
        pass

