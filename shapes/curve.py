from cairo import Context
import numpy as np
from core import GraphicalObject


def middle(start, end):
    return (start + end) / 2.

def dumb_curve_gen(p1, p2, p3, resolution):
    stack = []
    yield p1
    while True:
        s = middle(p1, p2)
        e = middle(p2, p3)



class Curve(GraphicalObject):
    def __init__(self, name: str):
        super().__init__(name)

