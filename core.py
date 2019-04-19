import abc
import numpy as np
from geometry import hpt, pt
from cairo import Context, SolidPattern
import typing as tp
import weakref
from contextlib import contextmanager
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk


@contextmanager
def this_source(ctx: Context, src):
    old = ctx.get_source()
    ctx.set_source(src)
    try:
        yield
    finally:
        ctx.set_source(old)


@contextmanager
def source_rgb(ctx: Context, r: float, g: float, b: float):
    old = ctx.get_source()


class Window:
    def __init__(self, bottom_left, top_left, top_right, bottom_right):
        super().__init__()
        self.bottom_left = bottom_left
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_right = bottom_right

    def move_up(self, amount):
        self.bottom_left += hpt(0., amount, last=0)
        self.top_left += hpt(0., amount, last=0)
        self.top_right += hpt(0., amount, last=0)
        self.bottom_right += hpt(0., amount, last=0)

    def move_down(self, amount):
        self.bottom_left -= hpt(0., amount, last=0)
        self.top_left -= hpt(0., amount, last=0)
        self.top_right -= hpt(0., amount, last=0)
        self.bottom_right -= hpt(0., amount, last=0)

    def move_left(self, amount: float):
        self.bottom_left += hpt(amount, 0., last=0)
        self.top_left += hpt(amount, 0., last=0)
        self.top_right += hpt(amount, 0., last=0)
        self.bottom_right += hpt(amount, 0., last=0)

    def move_right(self, amount: float):
        self.bottom_left -= hpt(amount, 0., last=0)
        self.top_left -= hpt(amount, 0., last=0)
        self.top_right -= hpt(amount, 0., last=0)
        self.bottom_right -= hpt(amount, 0., last=0)

    def zoom_in(self, amount: float):
        self.bottom_left += pt(amount, amount, 0.)
        self.top_left += pt(amount, -amount, 0.)
        self.top_right += pt(-amount, -amount, 0.)
        self.bottom_right += pt(-amount, amount, 0.)

    def zoom_out(self, amount: float):
        self.bottom_left -= pt(amount, amount, 0.)
        self.top_left -= pt(amount, -amount, 0.)
        self.top_right -= pt(-amount, -amount, 0.)
        self.bottom_right -= pt(-amount, amount, 0.)

    @property
    def size(self) -> np.ndarray:
        h = self.top_left[1] - self.bottom_left[1]
        w = self.bottom_right[0] - self.bottom_left[0]
        return hpt(w, h)

    @property
    def center(self):
        return (self.top_right + self.bottom_left) / 2.

    @staticmethod
    def orthogonal(p1, p2) -> "Window":
        w, h, _ = p2 - p1
        x0, y0, _ = p1
        return Window(p1, hpt(x0, y0 + h), p2, hpt(x0 + w, y0 + h))

    def __repr__(self):
        return f"Window({self.bottom_left}, {self.top_right})"


class Viewport:
    def __init__(self, top_left, size):
        self.top_left = top_left
        self.size = size

    def resize(self, width, height):
        size = hpt(width, height)
        self.size = size

    def draw(self, ctx: Context):
        with this_source(ctx, SolidPattern(1, 0, 0)):
            ctx.rectangle(*self.top_left[:-1], *self.size[:-1])
            ctx.stroke()


class DrawContext:
    def __init__(self, viewport: Viewport, win: Window, ctx: Context):
        self.viewport = viewport
        self.win = win
        self.ctx = ctx

    def viewport_transform(self, p):
        x, y, _ = (p - self.win.bottom_left) / self.win.size
        return hpt(x, 1 - y) * self.viewport.size


class GraphicalObject:
    def __init__(self, name: str):
        self._name = name
        self.points: tp.List[np.ndarray] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def center(self) -> np.ndarray:
        n = len(self.points[:, 0])
        c = sum(self.points)
        return c / n

    @abc.abstractmethod
    def draw(self, ctx: DrawContext) -> None:
        pass

    @abc.abstractmethod
    def draw_verbose(self, ctx: DrawContext) -> None:
        pass


class GraphicalModel:

    def __init__(self, list_model: Gtk.ListStore):
        self.display_file: tp.Dict[str, GraphicalObject] = {}
        self.subscriptions = []
        self.list_model = list_model
        # self.window = Window.orthogonal(hpt(-10., -10.), hpt(908., 460.))
        self.window = Window.orthogonal(hpt(-200, -200.), hpt(200., 200.))
        self.selected_name = None

    def subscribe(self, callback):
        self.subscriptions.append(callback)

    @property
    def selected(self) -> tp.Optional[GraphicalObject]:
        return self.display_file.get(self.selected_name)

    def update(self):
        for s in self.subscriptions:
            s()

    def add_obj(self, obj: GraphicalObject):
        self.display_file[obj.name] = obj
        self.list_model.append([obj.name, obj.__class__.__name__])
        self.update()

    def objects(self, clipper=...):
        if clipper is ...:
            clipper = lambda x: x
        for obj in map(clipper, self.display_file.values()):
            if obj is not None:
                yield obj

    def remove_selected(self):
        pass


class Clipper:
    def __init__(self, window):
        self.window = window

    def __call__(self, obj: GraphicalObject) -> tp.Optional[GraphicalObject]:
        name = obj.__class__.__name__.lower()
        meth = f"clip_{name}"
        if hasattr(self, meth):
            return getattr(self, meth)(self, obj)
        raise TypeError(f"This clipper cannot clip a {name}.")


class WindowEventHandler:
    def __init__(self, app_handler: "ApplicationHandler"):
        """
        :param app_handler: Handler for events of the whole application
        """
        self.app_handler: ApplicationHandler = weakref.proxy(app_handler)
        self.model: GraphicalModel = weakref.proxy(app_handler.model)

    def entries(self):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if isinstance(attr, Gtk.Entry):
                yield attr

    def check_numeric_entries(self):
        for entry in self.entries():
            p = entry.get_input_purpose()
            if p == Gtk.InputPurpose.NUMBER:
                try:
                    float(entry.get_text())
                except ValueError:
                    entry.grab_focus()
                    pop_msg(entry, "Invalid real number").show_all()
                    return False
        return True

    def check_name(self, entry: Gtk.Entry):
        valid = entry.get_text() not in self.model.display_file
        if not valid:
            pop_msg(entry, "An object with this name already exists")
        return valid


class ApplicationHandler:
    def __init__(self, builder: Gtk.Builder, model: GraphicalModel = ...):
        if model is ...:
            model = GraphicalModel(builder.get_object("lst_store_objects"))
        self.model: GraphicalModel = model

    @property
    def main_window(self) -> WindowEventHandler:
        raise NotImplemented

    @staticmethod
    def clean_entries(win: WindowEventHandler):
        for entry in win.entries():
            p = entry.get_input_purpose()
            if p == Gtk.InputPurpose.NUMBER:
                entry.set_text("0.0")
            else:
                entry.set_text("")


def pop_msg(widget: Gtk.Widget, msg: str):
    pop = Gtk.Popover.new(widget)
    pop.lbl_txt = Gtk.Label(msg)
    pop.add(pop.lbl_txt)
    pop.set_position(Gtk.PositionType.RIGHT)
    return pop
