import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk, GObject
import abc

class UI:
    def __init__(self, builder: Gtk.Builder):
        self.entry_add_name: Gtk.Gtk.Entry = builder.get_object("entry_add_name")
        self.entry_add_pointx: Gtk.Gtk.Entry = builder.get_object("entry_add_pointx")
        self.entry_add_pointy: Gtk.Gtk.Entry = builder.get_object("entry_add_pointy")
        self.add_line_window: Gtk.Gtk.Window = builder.get_object("add_line_window")
        self.entry_add_line_name: Gtk.Gtk.Entry = builder.get_object("entry_add_line_name")
        self.entry_add_line_x: Gtk.Gtk.Entry = builder.get_object("entry_add_line_x")
        self.entry_add_line_y: Gtk.Gtk.Entry = builder.get_object("entry_add_line_y")
        self.entry_add_line_x2: Gtk.Gtk.Entry = builder.get_object("entry_add_line_x2")
        self.entry_add_line_y2: Gtk.Gtk.Entry = builder.get_object("entry_add_line_y2")
        self.btn_add_line: Gtk.Gtk.Button = builder.get_object("btn_add_line")
        self.add_object_3D: Gtk.Gtk.Window = builder.get_object("add_object_3D")
        self.box49: Gtk.Gtk.Box = builder.get_object("box49")
        self.box50: Gtk.Gtk.Box = builder.get_object("box50")
        self.label32: Gtk.Gtk.Label = builder.get_object("label32")
        self.entry_add_object_name: Gtk.Gtk.Entry = builder.get_object("entry_add_object_name")
        self.box51: Gtk.Gtk.Box = builder.get_object("box51")
        self.label33: Gtk.Gtk.Label = builder.get_object("label33")
        self.entry_add_objectx: Gtk.Gtk.Entry = builder.get_object("entry_add_objectx")
        self.box52: Gtk.Gtk.Box = builder.get_object("box52")
        self.label34: Gtk.Gtk.Label = builder.get_object("label34")
        self.entry_add_objecty: Gtk.Gtk.Entry = builder.get_object("entry_add_objecty")
        self.box54: Gtk.Gtk.Box = builder.get_object("box54")
        self.label35: Gtk.Gtk.Label = builder.get_object("label35")
        self.entry_add_objectz: Gtk.Gtk.Entry = builder.get_object("entry_add_objectz")
        self.box53: Gtk.Gtk.Box = builder.get_object("box53")
        self.btn_add_vertice: Gtk.Gtk.Button = builder.get_object("btn_add_vertice")
        self.btn_finish_object: Gtk.Gtk.Button = builder.get_object("btn_finish_object")
        self.add_polygon_window: Gtk.Gtk.Window = builder.get_object("add_polygon_window")
        self.entry_add_polygon_name: Gtk.Gtk.Entry = builder.get_object("entry_add_polygon_name")
        self.entry_add_polygonx: Gtk.Gtk.Entry = builder.get_object("entry_add_polygonx")
        self.entry_add_polygony: Gtk.Gtk.Entry = builder.get_object("entry_add_polygony")
        self.entry_add_polygonz: Gtk.Gtk.Entry = builder.get_object("entry_add_polygonz")
        self.btn_add_polygon: Gtk.Gtk.Button = builder.get_object("btn_add_polygon")
        self.adjustment1: Gtk.Gtk.Adjustment = builder.get_object("adjustment1")
        self.escalonate_window1: Gtk.Gtk.Window = builder.get_object("escalonate_window1")
        self.entry_escalex: Gtk.Gtk.Entry = builder.get_object("entry_escalex")
        self.entry_escaley: Gtk.Gtk.Entry = builder.get_object("entry_escaley")
        self.btn_add_escale: Gtk.Gtk.Button = builder.get_object("btn_add_escale")
        self.includeObject_window: Gtk.Gtk.Window = builder.get_object("includeObject_window")
        self.btn_include_point: Gtk.Gtk.Button = builder.get_object("btn_include_point")
        self.btn_include_polygon: Gtk.Gtk.Button = builder.get_object("btn_include_polygon")
        self.btn_include_line: Gtk.Gtk.Button = builder.get_object("btn_include_line")
        self.btn_include_spline: Gtk.Gtk.Button = builder.get_object("btn_include_spline")
        self.btn_include_object3d: Gtk.Gtk.Button = builder.get_object("btn_include_object3d")
        self.btn_include_bezier: Gtk.Gtk.Button = builder.get_object("btn_include_bezier")
        self.main_window: Gtk.Gtk.Window = builder.get_object("main_window")
        self.btn_new: Gtk.Gtk.Button = builder.get_object("btn_new")
        self.btn_save: Gtk.Gtk.Button = builder.get_object("btn_save")
        self.btn_open: Gtk.Gtk.Button = builder.get_object("btn_open")
        self.tree_objects: Gtk.Gtk.TreeView = builder.get_object("tree_objects")
        self.btn_add_object: Gtk.Gtk.Button = builder.get_object("btn_add_object")
        self.btn_up: Gtk.Gtk.Button = builder.get_object("btn_up")
        self.btn_left: Gtk.Gtk.Button = builder.get_object("btn_left")
        self.btn_right: Gtk.Gtk.Button = builder.get_object("btn_right")
        self.btn_down: Gtk.Gtk.Button = builder.get_object("btn_down")
        self.comboboxtext_options: Gtk.Gtk.ComboBoxText = builder.get_object("comboboxtext_options")
        self.btn_zoom_out: Gtk.Gtk.Button = builder.get_object("btn_zoom_out")
        self.btn_zoom_in: Gtk.Gtk.Button = builder.get_object("btn_zoom_in")
        self.btn_left_rotate: Gtk.Gtk.Button = builder.get_object("btn_left_rotate")
        self.btn_right_rotate: Gtk.Gtk.Button = builder.get_object("btn_right_rotate")
        self.btn_rotate_object: Gtk.Gtk.Button = builder.get_object("btn_rotate_object")
        self.btn_rotate_world: Gtk.Gtk.Button = builder.get_object("btn_rotate_world")
        self.btn_rotate_specific: Gtk.Gtk.Button = builder.get_object("btn_rotate_specific")
        self.btn_scale: Gtk.Gtk.Button = builder.get_object("btn_scale")
        self.btn_translate: Gtk.Gtk.Button = builder.get_object("btn_translate")
        self.canvas: Gtk.Gtk.DrawingArea = builder.get_object("canvas")
        self.lstLog: Gtk.Gtk.ListBox = builder.get_object("lstLog")
        self.translate_window: Gtk.Gtk.Window = builder.get_object("translate_window")
        self.entry_translatex: Gtk.Gtk.Entry = builder.get_object("entry_translatex")
        self.entry_translatey: Gtk.Gtk.Entry = builder.get_object("entry_translatey")
        self.btn_apply_translation: Gtk.Gtk.Button = builder.get_object("btn_apply_translation")
        # btn_add_line
        self.btn_add_line.connect("clicked", self.on_btn_add_line_activate)
        # btn_add_vertice
        self.btn_add_vertice.connect("clicked", self.on_btn_add_vertice_activate)
        # btn_finish_object
        self.btn_finish_object.connect("clicked", self.on_btn_finish_object_activate)
        # btn_add_polygon
        self.btn_add_polygon.connect("clicked", self.on_btn_add_polygon_activate)
        # btn_add_escale
        self.btn_add_escale.connect("clicked", self.on_btn_add_escale_activate)
        # btn_include_point
        self.btn_include_point.connect("clicked", self.on_btn_include_point_activate)
        # btn_include_polygon
        self.btn_include_polygon.connect("clicked", self.on_btn_include_polygon_activate)
        # btn_include_line
        self.btn_include_line.connect("clicked", self.on_btn_include_line_activate)
        # btn_include_spline
        self.btn_include_spline.connect("clicked", self.on_btn_include_spline_activate)
        # btn_include_object3d
        self.btn_include_object3d.connect("clicked", self.on_btn_include_object3d_activate)
        # btn_include_bezier
        self.btn_include_bezier.connect("clicked", self.on_btn_include_bezier_activate)
        # main_window
        self.main_window.connect("activate-focus", self.on_main_window_activate_focus)
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
        # btn_apply_translation
        self.btn_apply_translation.connect("clicked", self.on_btn_apply_translation_clicked)
    
        self.main_window.connect("destroy", Gtk.main_quit)

    def show(self):
        self.main_window.show()

    @abc.abstractmethod
    def on_btn_add_line_activate(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_add_vertice_activate(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_finish_object_activate(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_add_polygon_activate(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_add_escale_activate(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_include_point_activate(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_include_polygon_activate(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_include_line_activate(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_include_spline_activate(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_include_object3d_activate(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_include_bezier_activate(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_main_window_activate_focus(self, sender: Gtk.Window) -> None:
        pass

    @abc.abstractmethod
    def on_btn_add_object_clicked(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_up_clicked(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_left_clicked(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_right_clicked(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_down_clicked(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_zoom_out_clicked(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_zoom_in_clicked(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_left_rotate_clicked(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_right_rotate_clicked(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_scale_clicked(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_btn_translate_clicked(self, sender: Gtk.Button) -> None:
        pass

    @abc.abstractmethod
    def on_canvas_draw(self, sender: Gtk.DrawingArea, ctx) -> None:
        pass

    @abc.abstractmethod
    def on_btn_apply_translation_clicked(self, sender: Gtk.Button) -> None:
        pass

