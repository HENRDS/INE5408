import abc
import numpy as np
from geometry import hpt
from cairo import Context
import typing as tp
import weakref
import inspect
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk


class Window:
    def __init__(self, p1, p2):
        super().__init__()
        self.p1 = p1
        self.p2 = p2

    def move_up(self, amount):
        self.p1 += hpt(0., amount)
        self.p2 += hpt(0., amount)

    def move_down(self, amount):
        self.p1 -= hpt(0., amount)
        self.p2 -= hpt(0., amount)

    def move_left(self, amount):
        self.p1 += hpt(amount, 0.)
        self.p2 += hpt(amount, 0.)

    def move_right(self, amount):
        self.p1 -= hpt(amount, 0.)
        self.p2 -= hpt(amount, 0.)

    def zoom_in(self, amount):
        self.p1 += hpt(amount, amount)
        self.p2 -= hpt(amount, amount)

    def zoom_out(self, amount):
        self.p1 -= hpt(amount, amount)
        self.p2 += hpt(amount, amount)


class Viewport:
    def __init__(self, top_left, size):
        self.top_left = top_left
        self.size = size

    def resize(self, width, height):
        size = hpt(width, height)
        self.size = size

    def transformer(self, window: Window):
        def transform(p):
            u = (window.p2 - window.p1)[:-1]
            x, y = (p - window.p1)[:-1] / u
            z = np.array([x, 1 - y, 1])
            return self.size * z

        return transform


class GraphicalObject:
    def __init__(self, name: str):
        self._name = name
        self.points: tp.List[np.ndarray] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def center(self) -> np.ndarray:
        n = len(self.points)
        return sum(self.points) / n

    @abc.abstractmethod
    def draw(self, ctx: Context, transform, verbose=False) -> None:
        pass


class GraphicalModel:

    def __init__(self, list_model: Gtk.ListStore):
        self.display_file: tp.Dict[str, GraphicalObject] = {}
        self.subscriptions = []
        self.list_model = list_model
        self.window = Window(hpt(0., 0.), hpt(800., 600.))
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
    def __init__(self, window):
        self.window = window

    def __call__(self, obj: GraphicalObject) -> tp.Optional[GraphicalObject]:
        name = obj.__class__.__name__.lower()
        meth = f"clip_{name}"
        if hasattr(self, meth):
            return getattr(self, meth)(self, obj)
        raise TypeError(f"This clipper cannot clip a {name}.")


class WindowEventHandler:
    def __init__(self, app_handler: "ApplicationHandler", builder: Gtk.Builder):
        """
        :param app_handler: Handler for events of the whole application
        :param builder: GtkBuilder used to load the controls, windows and connect their signals
        :type Gtk.Builder
        """
        self.app_handler: ApplicationHandler = weakref.proxy(app_handler)
        self.model: GraphicalModel = weakref.proxy(app_handler.model)


class ApplicationHandler:
    def __init__(self, builder: Gtk.Builder, model: GraphicalModel = ...):
        if model is ...:
            model = GraphicalModel(builder.get_object("lst_store_objects"))
        self.model: GraphicalModel = model

    @property
    def main_window(self) -> WindowEventHandler:
        raise NotImplemented

    def clean_entries(self, win):
        for attr_name in dir(win):
            attr = getattr(win, attr_name)
            if isinstance(attr, Gtk.Entry):
                p = attr.get_input_purpose()
                if p == Gtk.InputPurpose.NUMBER:
                    attr.set_text("0.0")
                else:
                    attr.set_text("")
