from cairo import Context
from weakref import proxy
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk


class WindowEventHandler:
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        """
        :param app_handler: Handler for events of the whole application
        :param builder: GtkBuilder used to load the controls, windows and connect their signals
        :type Gtk.Builder
        """
        self.app_handler: "UI" = proxy(app_handler)


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
        self.entry_add_name: Gtk.Entry = builder.get_object("entry_add_name")
        self.entry_add_pointx: Gtk.Entry = builder.get_object("entry_add_pointx")
        self.entry_add_pointy: Gtk.Entry = builder.get_object("entry_add_pointy")

    def on_win_add_point_activate_focus(self, sender: Gtk.Window) -> None:
        """Handler for event 'activate-focus' of control win_add_point."""
        pass


class WinAddPolygon(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.win: Gtk.Window = builder.get_object("win_add_polygon")
        self.btn_remove_polygon_point: Gtk.Button = builder.get_object("btn_remove_polygon_point")
        self.btn_add_polygon_point: Gtk.Button = builder.get_object("btn_add_polygon_point")
        self.lst_polygon_points: Gtk.ListBox = builder.get_object("lst_polygon_points")
        self.entry_add_polygon_name: Gtk.Entry = builder.get_object("entry_add_polygon_name")
        self.entry_add_polygonx: Gtk.Entry = builder.get_object("entry_add_polygonx")
        self.entry_add_polygony: Gtk.Entry = builder.get_object("entry_add_polygony")
        self.entry_add_polygonz: Gtk.Entry = builder.get_object("entry_add_polygonz")
        self.btn_add_polygon: Gtk.Button = builder.get_object("btn_add_polygon")
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

    def on_lst_polygon_points_row_activated(self, sender: Gtk.ListBox) -> None:
        """Handler for event 'row-activated' of control lst_polygon_points."""
        pass

    def on_btn_add_polygon_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_polygon."""
        pass


class WinEscalonate(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.win: Gtk.Window = builder.get_object("win_escalonate")
        self.entry_escalex: Gtk.Entry = builder.get_object("entry_escalex")
        self.entry_escaley: Gtk.Entry = builder.get_object("entry_escaley")
        self.btn_add_escale: Gtk.Button = builder.get_object("btn_add_escale")
        # btn_add_escale handlers
        self.btn_add_escale.connect("clicked", self.on_btn_add_escale_clicked)

    def on_win_escalonate_activate_focus(self, sender: Gtk.Window) -> None:
        """Handler for event 'activate-focus' of control win_escalonate."""
        pass

    def on_btn_add_escale_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_escale."""
        pass


class WinIncludeObject(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.win: Gtk.Window = builder.get_object("win_include_object")
        self.btn_include_point: Gtk.Button = builder.get_object("btn_include_point")
        self.btn_include_polygon: Gtk.Button = builder.get_object("btn_include_polygon")
        self.btn_include_line: Gtk.Button = builder.get_object("btn_include_line")
        self.btn_include_spline: Gtk.Button = builder.get_object("btn_include_spline")
        self.btn_include_object3d: Gtk.Button = builder.get_object("btn_include_object3d")
        self.btn_include_bezier: Gtk.Button = builder.get_object("btn_include_bezier")
        # btn_include_point handlers
        self.btn_include_point.connect("clicked", self.on_btn_include_point_clicked)
        # btn_include_polygon handlers
        self.btn_include_polygon.connect("clicked", self.on_btn_include_polygon_clicked)
        # btn_include_line handlers
        self.btn_include_line.connect("clicked", self.on_btn_include_line_clicked)
        # btn_include_spline handlers
        self.btn_include_spline.connect("clicked", self.on_btn_include_spline_clicked)
        # btn_include_object3d handlers
        self.btn_include_object3d.connect("clicked", self.on_btn_include_object3d_clicked)
        # btn_include_bezier handlers
        self.btn_include_bezier.connect("clicked", self.on_btn_include_bezier_clicked)

    def on_win_include_object_destroy(self, sender: Gtk.Window) -> None:
        """Handler for event 'destroy' of control win_include_object."""
        pass

    def on_win_include_object_hide(self, sender: Gtk.Window) -> None:
        """Handler for event 'hide' of control win_include_object."""
        pass

    def on_win_include_object_realize(self, sender: Gtk.Window) -> None:
        """Handler for event 'realize' of control win_include_object."""
        pass

    def on_win_include_object_show(self, sender: Gtk.Window) -> None:
        """Handler for event 'show' of control win_include_object."""
        pass

    def on_btn_include_point_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_include_point."""
        pass

    def on_btn_include_polygon_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_include_polygon."""
        pass

    def on_btn_include_line_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_include_line."""
        pass

    def on_btn_include_spline_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_include_spline."""
        pass

    def on_btn_include_object3d_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_include_object3d."""
        pass

    def on_btn_include_bezier_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_include_bezier."""
        pass


class WinMain(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
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
        # btn_add_object handlers
        self.btn_add_object.connect("clicked", self.on_btn_add_object_clicked)
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
        # btn_scale handlers
        self.btn_scale.connect("clicked", self.on_btn_scale_clicked)
        # btn_translate handlers
        self.btn_translate.connect("clicked", self.on_btn_translate_clicked)
        # canvas handlers
        self.canvas.connect("draw", self.on_canvas_draw)

    def on_main_window_clicked_focus(self, sender: Gtk.Window) -> None:
        """Handler for event 'activate-focus' of control win_main."""
        pass

    def on_btn_add_object_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_object."""
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

    def on_btn_scale_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_scale."""
        pass

    def on_btn_translate_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_translate."""
        pass

    def on_canvas_draw(self, sender: Gtk.DrawingArea, ctx: Context) -> None:
        """Handler for event 'draw' of control canvas."""
        pass


class WinTranslate(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.win: Gtk.Window = builder.get_object("win_translate")
        self.entry_translatex: Gtk.Entry = builder.get_object("entry_translatex")
        self.entry_translatey: Gtk.Entry = builder.get_object("entry_translatey")
        self.btn_apply_translation: Gtk.Button = builder.get_object("btn_apply_translation")
        # btn_apply_translation handlers
        self.btn_apply_translation.connect("clicked", self.on_btn_apply_translation_clicked)

    def on_win_translate_activate_focus(self, sender: Gtk.Window) -> None:
        """Handler for event 'activate-focus' of control win_translate."""
        pass

    def on_btn_apply_translation_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_apply_translation."""
        pass


class UI:
    _WIN_ADD_LINE = WinAddLine
    _WIN_ADD_OBJECT3D = WinAddObject3D
    _WIN_ADD_POINT = WinAddPoint
    _WIN_ADD_POLYGON = WinAddPolygon
    _WIN_ESCALONATE = WinEscalonate
    _WIN_INCLUDE_OBJECT = WinIncludeObject
    _WIN_MAIN = WinMain
    _WIN_TRANSLATE = WinTranslate

    def __init__(self, builder: Gtk.Builder):
        self.win_add_line: WinAddLine = self._WIN_ADD_LINE(self, builder)
        self.win_add_object3d: WinAddObject3D = self._WIN_ADD_OBJECT3D(self, builder)
        self.win_add_point: WinAddPoint = self._WIN_ADD_POINT(self, builder)
        self.win_add_polygon: WinAddPolygon = self._WIN_ADD_POLYGON(self, builder)
        self.win_escalonate: WinEscalonate = self._WIN_ESCALONATE(self, builder)
        self.win_include_object: WinIncludeObject = self._WIN_INCLUDE_OBJECT(self, builder)
        self.win_main: WinMain = self._WIN_MAIN(self, builder)
        self.win_translate: WinTranslate = self._WIN_TRANSLATE(self, builder)
        self.win_main.win.connect("destroy", Gtk.main_quit)

    def show(self):
        self.win_main.win.show()