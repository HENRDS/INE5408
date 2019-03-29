import abc
from cairo import Context

class GraphicalObject:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @abc.abstractmethod
    def draw(self, ctx: Context) -> None:
        pass