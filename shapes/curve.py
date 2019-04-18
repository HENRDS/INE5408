from cairo import Context
import numpy as np
from core import GraphicalObject


class Curve(GraphicalObject):
    def __init__(self, name: str):
        super().__init__(name)