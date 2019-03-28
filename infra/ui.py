import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk, GObject
import abc

class UI:
    def __init__(self, builder: Gtk.Builder):
        self.entry_add_name: Gtk.Entry = builder.get_object("entry_add_name")
        self.entry_add_pointx: Gtk.Entry = builder.get_object("entry_add_pointx")
        self.entry_add_pointy: Gtk.Entry = builder.get_object("entry_add_pointy")
        self.add_line_window: Gtk.Window = builder.get_object("add_line_window")
        self.entry_add_line_name: Gtk.Entry = builder.get_object("entry_add_line_name")
        self.entry_add_line_x: Gtk.Entry = builder.get_object("entry_add_line_x")
        self.entry_add_line_y: Gtk.Entry = builder.get_object("entry_add_line_y")
        self.entry_add_line_x2: Gtk.Entry = builder.get_object("entry_add_line_x2")
        self.entry_add_line_y2: Gtk.Entry = builder.get_object("entry_add_line_y2")
        self.btn_add_line: Gtk.Button = builder.get_object("btn_add_line")
        self.add_object_3D: Gtk.Window = builder.get_object("add_object_3D")
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
        self.add_polygon_window: Gtk.Window = builder.get_object("add_polygon_window")
        self.entry_add_polygon_name: Gtk.Entry = builder.get_object("entry_add_polygon_name")
        self.entry_add_polygonx: Gtk.Entry = builder.get_object("entry_add_polygonx")
        self.entry_add_polygony: Gtk.Entry = builder.get_object("entry_add_polygony")
        self.entry_add_polygonz: Gtk.Entry = builder.get_object("entry_add_polygonz")
        self.btn_add_polygon: Gtk.Button = builder.get_object("btn_add_polygon")
        self.escalonate_window1: Gtk.Window = builder.get_object("escalonate_window1")
        self.entry_escalex: Gtk.Entry = builder.get_object("entry_escalex")
        self.entry_escaley: Gtk.Entry = builder.get_object("entry_escaley")
        self.btn_add_escale: Gtk.Button = builder.get_object("btn_add_escale")
        self.includeObject_window: Gtk.Window = builder.get_object("includeObject_window")
        self.btn_include_point: Gtk.Button = builder.get_object("btn_include_point")
        self.btn_include_polygon: Gtk.Button = builder.get_object("btn_include_polygon")
        self.btn_include_line: Gtk.Button = builder.get_object("btn_include_line")
        self.btn_include_spline: Gtk.Button = builder.get_object("btn_include_spline")
        self.btn_include_object3d: Gtk.Button = builder.get_object("btn_include_object3d")
        self.btn_include_bezier: Gtk.Button = builder.get_object("btn_include_bezier")
        self.main_window: Gtk.Window = builder.get_object("main_window")
        self.btn_new: Gtk.Button = builder.get_object("btn_new")
        self.btn_save: Gtk.Button = builder.get_object("btn_save")
        self.btn_open: Gtk.Button = builder.get_object("btn_open")
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
        self.translate_window: Gtk.Window = builder.get_object("translate_window")
        self.entry_translatex: Gtk.Entry = builder.get_object("entry_translatex")
        self.entry_translatey: Gtk.Entry = builder.get_object("entry_translatey")
        self.btn_apply_translation: Gtk.Button = builder.get_object("btn_apply_translation")
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
    def on_btn_add_line_activate(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_add_vertice_activate(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_finish_object_activate(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_add_polygon_activate(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_add_escale_activate(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_include_point_activate(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_include_polygon_activate(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_include_line_activate(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_include_spline_activate(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_include_object3d_activate(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_include_bezier_activate(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_up_clicked(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_left_clicked(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_right_clicked(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_down_clicked(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_zoom_out_clicked(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_zoom_in_clicked(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_left_rotate_clicked(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_right_rotate_clicked(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_scale_clicked(self) -> None:
        pass

    @abc.abstractmethod
    def on_btn_translate_clicked(self) -> None:
        pass

    @abc.abstractmethod
    def on_canvas_draw(self, ctx) -> None:
        pass

    @abc.abstractmethod
    def on_btn_apply_translation_clicked(self) -> None:
        pass

