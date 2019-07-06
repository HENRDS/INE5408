from .graphical import GraphicalObject
from .window import Window
import typing as tp


class Clipper:
    def __init__(self, window: Window):
        self.window = window

    def __call__(self, obj: GraphicalObject) -> tp.Optional[GraphicalObject]:
        name = obj.__class__.__name__
        method = f"clip_{name.lower()}"
        if hasattr(self, method):
            return getattr(self, method)(obj)
        # return obj
        raise TypeError(f"This clipper cannot clip a {name}.")
