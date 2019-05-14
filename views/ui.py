from core import GraphicalModel, WindowEventHandler, ApplicationHandler
from cairo import Context
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk


class PopAddObj(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler)
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


class WinMain(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler)
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
        self.btn_scale: Gtk.Button = builder.get_object("btn_scale")
        self.btn_translate: Gtk.Button = builder.get_object("btn_translate")
        self.btn_delete_object: Gtk.Button = builder.get_object("btn_delete_object")
        self.btn_clean_window: Gtk.Button = builder.get_object("btn_clean_window")
        self.canvas: Gtk.DrawingArea = builder.get_object("canvas")
        self.lstLog: Gtk.ListBox = builder.get_object("lstLog")
        self.win.connect("activate-focus", self.on_main_window_clicked_focus)
        self.win.connect("key-press-event", self.on_win_main_key_press_event)
        # btn_new handlers
        self.btn_new.connect("clicked", self.on_btn_new_clicked)
        # btn_save handlers
        self.btn_save.connect("clicked", self.on_btn_save_clicked)
        # btn_open handlers
        self.btn_open.connect("clicked", self.on_btn_open_clicked)
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

    def on_btn_new_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_new."""
        pass

    def on_btn_save_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_save."""
        pass

    def on_btn_open_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_open."""
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


class WinAddPolygon(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler)
        self.win: Gtk.Dialog = builder.get_object("win_add_polygon")
        self.btn_close_polygon: Gtk.Button = builder.get_object("btn_close_polygon")
        self.btn_add_polygon: Gtk.Button = builder.get_object("btn_add_polygon")
        self.btn_remove_polygon_point: Gtk.Button = builder.get_object("btn_remove_polygon_point")
        self.btn_add_polygon_point: Gtk.Button = builder.get_object("btn_add_polygon_point")
        self.tree_polygon_points: Gtk.TreeView = builder.get_object("tree_polygon_points")
        self.entry_name_polygon: Gtk.Entry = builder.get_object("entry_name_polygon")
        self.entry_poligonx: Gtk.Entry = builder.get_object("entry_poligonx")
        self.entry_poligony: Gtk.Entry = builder.get_object("entry_poligony")
        self.entry_poligonz: Gtk.Entry = builder.get_object("entry_poligonz")
        # btn_close_polygon handlers
        self.btn_close_polygon.connect("clicked", self.on_btn_close_polygon_clicked)
        # btn_add_polygon handlers
        self.btn_add_polygon.connect("clicked", self.on_btn_add_polygon_clicked)
        # btn_remove_polygon_point handlers
        self.btn_remove_polygon_point.connect("clicked", self.on_btn_remove_polygon_point_clicked)
        # btn_add_polygon_point handlers
        self.btn_add_polygon_point.connect("clicked", self.on_btn_add_polygon_point_clicked)

    def on_btn_close_polygon_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_close_polygon."""
        pass

    def on_btn_add_polygon_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_polygon."""
        pass

    def on_btn_remove_polygon_point_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_remove_polygon_point."""
        pass

    def on_btn_add_polygon_point_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_polygon_point."""
        pass


class WinCurve(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler)
        self.win: Gtk.Dialog = builder.get_object("win_curve")
        self.btn_close_curve: Gtk.Button = builder.get_object("btn_close_curve")
        self.btn_add_curve: Gtk.Button = builder.get_object("btn_add_curve")
        self.btn_remove_curve_point: Gtk.Button = builder.get_object("btn_remove_curve_point")
        self.btn_add_curve_point: Gtk.Button = builder.get_object("btn_add_curve_point")
        self.tree_curve_points: Gtk.TreeView = builder.get_object("tree_curve_points")
        self.entry_poligonx1: Gtk.Entry = builder.get_object("entry_poligonx1")
        self.entry_poligony1: Gtk.Entry = builder.get_object("entry_poligony1")
        self.entry_poligonz1: Gtk.Entry = builder.get_object("entry_poligonz1")
        self.comboboxtext_curve: Gtk.ComboBoxText = builder.get_object("comboboxtext_curve")
        # btn_close_curve handlers
        self.btn_close_curve.connect("clicked", self.on_btn_close_curve_clicked)
        # btn_add_curve handlers
        self.btn_add_curve.connect("clicked", self.on_btn_add_curve_clicked)
        # btn_remove_curve_point handlers
        self.btn_remove_curve_point.connect("clicked", self.on_btn_remove_curve_point_clicked)
        # btn_add_curve_point handlers
        self.btn_add_curve_point.connect("clicked", self.on_btn_add_curve_point_clicked)

    def on_btn_close_curve_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_close_curve."""
        pass

    def on_btn_add_curve_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_curve."""
        pass

    def on_btn_remove_curve_point_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_remove_curve_point."""
        pass

    def on_btn_add_curve_point_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_curve_point."""
        pass


class WinLine(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler)
        self.win: Gtk.Dialog = builder.get_object("win_line")
        self.btn_close_line: Gtk.Button = builder.get_object("btn_close_line")
        self.btn_add_line: Gtk.Button = builder.get_object("btn_add_line")
        self.name_line: Gtk.Entry = builder.get_object("name_line")
        self.entry_x1_line: Gtk.Entry = builder.get_object("entry_x1_line")
        self.entry_y1_line: Gtk.Entry = builder.get_object("entry_y1_line")
        self.entry_z1_line: Gtk.Entry = builder.get_object("entry_z1_line")
        self.entry_x2_line: Gtk.Entry = builder.get_object("entry_x2_line")
        self.entry_y2_line: Gtk.Entry = builder.get_object("entry_y2_line")
        self.entry_z2_line: Gtk.Entry = builder.get_object("entry_z2_line")
        # btn_close_line handlers
        self.btn_close_line.connect("clicked", self.on_btn_close__clicked)
        # btn_add_line handlers
        self.btn_add_line.connect("clicked", self.on_btn_add_line_clicked)

    def on_btn_close__clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_close_line."""
        pass

    def on_btn_add_line_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_line."""
        pass


class WinObj3D(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler)
        self.win: Gtk.Dialog = builder.get_object("win_obj_3d")
        self.btn_add_vertice: Gtk.Button = builder.get_object("btn_add_vertice")
        self.btn_finish_obj: Gtk.Button = builder.get_object("btn_finish_obj")
        self.entry_obj_name: Gtk.Entry = builder.get_object("entry_obj_name")
        self.entry_verticex: Gtk.Entry = builder.get_object("entry_verticex")
        self.entry_verticey: Gtk.Entry = builder.get_object("entry_verticey")
        self.entry_verticez: Gtk.Entry = builder.get_object("entry_verticez")
        # btn_add_vertice handlers
        self.btn_add_vertice.connect("clicked", self.on_btn_add_vertice_clicked)
        # btn_finish_obj handlers
        self.btn_finish_obj.connect("clicked", self.on_btn_finish_obj_clicked)

    def on_btn_add_vertice_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add_vertice."""
        pass

    def on_btn_finish_obj_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_finish_obj."""
        pass


class WinPoint(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler)
        self.win: Gtk.Dialog = builder.get_object("win_point")
        self.btn_close: Gtk.Button = builder.get_object("btn_close")
        self.btn_add: Gtk.Button = builder.get_object("btn_add")
        self.entry_add_name: Gtk.Entry = builder.get_object("entry_add_name")
        self.entry_add_pointx: Gtk.Entry = builder.get_object("entry_add_pointx")
        self.entry_add_pointy: Gtk.Entry = builder.get_object("entry_add_pointy")
        self.entry_add_pointz: Gtk.Entry = builder.get_object("entry_add_pointz")
        # btn_close handlers
        self.btn_close.connect("clicked", self.on_btn_close_clicked)
        # btn_add handlers
        self.btn_add.connect("clicked", self.on_btn_add_clicked)

    def on_btn_close_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_close."""
        pass

    def on_btn_add_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_add."""
        pass


class WinRotate(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler)
        self.win: Gtk.Dialog = builder.get_object("win_rotate")
        self.btn_close_rotate: Gtk.Button = builder.get_object("btn_close_rotate")
        self.btn_apply_rotate: Gtk.Button = builder.get_object("btn_apply_rotate")
        self.entry_radian: Gtk.Entry = builder.get_object("entry_radian")
        self.entry_rotatex: Gtk.Entry = builder.get_object("entry_rotatex")
        self.entry_rotatey: Gtk.Entry = builder.get_object("entry_rotatey")
        # btn_close_rotate handlers
        self.btn_close_rotate.connect("clicked", self.on_btn_close_rotate_clicked)
        # btn_apply_rotate handlers
        self.btn_apply_rotate.connect("clicked", self.on_btn_apply_rotate_clicked)

    def on_btn_close_rotate_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_close_rotate."""
        pass

    def on_btn_apply_rotate_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_apply_rotate."""
        pass


class WinScale(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler)
        self.win: Gtk.Dialog = builder.get_object("win_scale")
        self.btn_close_scale: Gtk.Button = builder.get_object("btn_close_scale")
        self.btn_apply_scale: Gtk.Button = builder.get_object("btn_apply_scale")
        self.entry_scalex: Gtk.Entry = builder.get_object("entry_scalex")
        self.entry_scaley: Gtk.Entry = builder.get_object("entry_scaley")
        # btn_close_scale handlers
        self.btn_close_scale.connect("clicked", self.on_btn_close_scale_clicked)
        # btn_apply_scale handlers
        self.btn_apply_scale.connect("clicked", self.on_btn_apply_scale_clicked)

    def on_btn_close_scale_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_close_scale."""
        pass

    def on_btn_apply_scale_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_apply_scale."""
        pass


class WinTranslate(WindowEventHandler):
    def __init__(self, app_handler: "UI", builder: Gtk.Builder):
        super().__init__(app_handler)
        self.win: Gtk.Dialog = builder.get_object("win_translate")
        self.btn_close_translate: Gtk.Button = builder.get_object("btn_close_translate")
        self.btn_apply_translation: Gtk.Button = builder.get_object("btn_apply_translation")
        self.entry_translatex: Gtk.Entry = builder.get_object("entry_translatex")
        self.entry_translatey: Gtk.Entry = builder.get_object("entry_translatey")
        # btn_close_translate handlers
        self.btn_close_translate.connect("clicked", self.on_btn_close_translate_clicked)
        # btn_apply_translation handlers
        self.btn_apply_translation.connect("clicked", self.on_btn_apply_translation_clicked)

    def on_btn_close_translate_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_close_translate."""
        pass

    def on_btn_apply_translation_clicked(self, sender: Gtk.Button) -> None:
        """Handler for event 'clicked' of control btn_apply_translation."""
        pass


class UI(ApplicationHandler):
    _POP_ADD_OBJ = PopAddObj
    _WIN_MAIN = WinMain
    _WIN_ADD_POLYGON = WinAddPolygon
    _WIN_CURVE = WinCurve
    _WIN_LINE = WinLine
    _WIN_OBJ_3D = WinObj3D
    _WIN_POINT = WinPoint
    _WIN_ROTATE = WinRotate
    _WIN_SCALE = WinScale
    _WIN_TRANSLATE = WinTranslate

    def __init__(self, model: GraphicalModel = ...):
        super().__init__(model)
        builder = Gtk.Builder.new_from_file("main_window.glade")
        self.finish_obj: Gtk.Image = builder.get_object("finish_obj")
        self.finish_object: Gtk.Image = builder.get_object("finish_object")
        self.image1: Gtk.Image = builder.get_object("image1")
        self.image_clean: Gtk.Image = builder.get_object("image_clean")
        self.image_down: Gtk.Image = builder.get_object("image_down")
        self.image_lef: Gtk.Image = builder.get_object("image_lef")
        self.image_left: Gtk.Image = builder.get_object("image_left")
        self.image_righ: Gtk.Image = builder.get_object("image_righ")
        self.image_right: Gtk.Image = builder.get_object("image_right")
        self.image_up: Gtk.Image = builder.get_object("image_up")
        self.image_zoom_in: Gtk.Image = builder.get_object("image_zoom_in")
        self.image_zoom_out: Gtk.Image = builder.get_object("image_zoom_out")
        self.imagine_remove_object: Gtk.Image = builder.get_object("imagine_remove_object")
        self.lst_store_objects: Gtk.ListStore = builder.get_object("lst_store_objects")
        self.pop_add_obj: PopAddObj = self._POP_ADD_OBJ(self, builder)
        self.win_main: WinMain = self._WIN_MAIN(self, builder)
        self.win_add_polygon: WinAddPolygon = self._WIN_ADD_POLYGON(self, builder)
        self.win_curve: WinCurve = self._WIN_CURVE(self, builder)
        self.win_line: WinLine = self._WIN_LINE(self, builder)
        self.win_obj_3d: WinObj3D = self._WIN_OBJ_3D(self, builder)
        self.win_point: WinPoint = self._WIN_POINT(self, builder)
        self.win_rotate: WinRotate = self._WIN_ROTATE(self, builder)
        self.win_scale: WinScale = self._WIN_SCALE(self, builder)
        self.win_translate: WinTranslate = self._WIN_TRANSLATE(self, builder)
        self.main_window.win.connect("destroy", Gtk.main_quit)


    @property
    def main_window(self):
        return self.win_main

    def show(self):
        self.main_window.win.show()