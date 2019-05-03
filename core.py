import abc
import numpy as np
from operator import itemgetter
from geometry import hpt, pt, rotate2D, rad, rel_transform, scale, vlen, translate, reflect, Axis, scale_translate
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

    def __init__(self, center, size):
        self.center = center
        self.size = size
        self.axes = rotate2D(rad(91.))

    @property
    def origin(self):
        sz = (.5 * self.size) * (self.x + self.y)
        return hpt(*(self.center - sz)[:-1])

    @property
    def angle(self):
        x, y, _ = self.y
        return np.arctan2(x, y)

    @property
    def width(self) -> float:
        return self.size[0]

    @property
    def height(self) -> float:
        return self.size[1]

    @property
    def x(self):
        return self.axes[0]

    @property
    def y(self):
        return self.axes[1]

    @property
    def z(self):
        return self.axes[2]

    def move_up(self, amount):
        self.center += self.y * amount

    def move_down(self, amount):
        self.center += self.y * -amount

    def move_left(self, amount: float):
        self.center += self.x * -amount

    def move_right(self, amount: float):
        self.center += self.x * amount

    def zoom_in(self, amount: float):
        self.center += pt(amount, amount, 0)
        self.size -= pt(2 * amount, 2 * amount, 0)

    def zoom_out(self, amount: float):
        self.center -= pt(amount, amount, 0)
        self.size += pt(2 * amount, 2 * amount, 0)

    def rotate(self, angle):
        self.axes = self.axes @ rotate2D(rad(angle))

    def __repr__(self):
        return f"Window(origin={self.origin}, x={self.x}, y={self.y}, z={self.z}))"


class Viewport:
    def __init__(self, top_left, size):
        self.top_left = top_left
        self.size = size

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    @property
    def top(self):
        return self.top_left[0]

    @property
    def left(self):
        return self.top_left[1]

    def resize(self, width, height):
        size = hpt(width, height)
        self.size = size

    def draw(self, ctx: Context):
        with this_source(ctx, SolidPattern(1, 0, 0)):
            ctx.rectangle(*self.top_left[:-1], *(self.top_left + self.size)[:-1])
            ctx.stroke()

    def matrix(self):
        sx, sy, _ = self.size
        x0, y0, _ = self.top_left
        return np.array(
                [[sx, 0., 0.],
                 [0., sy, 0.],
                 [x0, y0, 1.]]
        )


class DrawContext:
    def __init__(self, viewport: Viewport, win: Window, ctx: Context):
        self.viewport = viewport
        self.win = win
        self.ctx = ctx
        self.origin = self.ppc(self.win.origin)

    def ppc(self, p):
        return p @ rotate2D(-self.win.angle)

    def viewport_transform(self, p):
        x, y, _ = (self.ppc(p) - self.origin) / self.win.size
        return hpt(x, 1 - y) @ self.viewport.matrix()


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
        self.window = Window(hpt(210., 210.), hpt(420., 420.))
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


class Clipper:
    def __init__(self, window: Window):
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
