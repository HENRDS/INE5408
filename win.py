from infra.ui import UI
from geometry.base import GraphicalObject
import typing as tp
from cairo import Context
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk, GObject


class SGI(UI):

    def __init__(self, builder: Gtk.Builder):
        super().__init__(builder)
        self.objects: tp.List[GraphicalObject] = []

    def add_obj(self, obj: GraphicalObject):
        self.objects.append(obj)

    def on_canvas_draw(self, ctx: Context) -> None:
        for object in self.objects:
            object.draw(ctx)

