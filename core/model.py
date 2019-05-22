import typing as tp
from .graphical import GraphicalObject
from geometry import hpt, rotate2D
from cairo import Context
import numpy as np


class GraphicalModel:
    def __init__(self):
        from .window import Window
        self.display_file: tp.Dict[str, GraphicalObject] = {}
        self.subscriptions = {}
        self.window = Window(hpt(210., 210.), hpt(420., 420.))
        self.selected_name = None

    def subscribe(self, event: str, callback):
        events = self.subscriptions.setdefault(event, [])
        events.append(callback)

    @property
    def selected(self) -> tp.Optional[GraphicalObject]:
        return self.display_file.get(self.selected_name)

    def update(self):
        self.trigger("draw")

    def trigger(self, event: str, *args, **kwargs):
        for callback in self.subscriptions.get(event, ()):
            callback(*args, **kwargs)

    def add_obj(self, obj: GraphicalObject):
        self.display_file[obj.name] = obj
        self.trigger("add", obj)

    def objects(self, clipper=...):
        ppc_matrix = rotate2D(-self.window.angle)
        bl = self.window.origin @ ppc_matrix
        tr = hpt(*(bl + self.window.size)[:-1])
        self.window._ppc = np.vstack((bl, tr))
        if clipper is ...:
            clipper = lambda x: x

        for obj in self.display_file.values():
            obj._ppc = obj.points @ ppc_matrix
            tobj = clipper(obj)
            if tobj is not None:
                yield tobj
