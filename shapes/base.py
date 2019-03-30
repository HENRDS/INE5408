import abc
from cairo import Context


class GraphicalObject:
    def __init__(self, name: str):
        self._name = name
        self.points = []

    @property
    def name(self) -> str:
        return self._name

    @abc.abstractmethod
    def draw(self, ctx: Context, transform) -> None:
        pass

    @abc.abstractmethod
    def __iter__(self):
        pass


