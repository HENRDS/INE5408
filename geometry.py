import numpy as np
from enum import Enum


class Axis(Enum):
    X = 0
    Y = 1
    Z = 2
    T = 3


def pt(*items) -> np.ndarray:
    """builds a simple point"""
    return np.array(items)


def hpt(*items, last=1) -> np.ndarray:
    """Builds an homogeneous coordinate system point"""
    return pt(*items, last)


def translate(point) -> np.ndarray:
    x, y, _ = point
    return np.array(
            [[1., 0., 0.],
             [0., 1., 0.],
             [x, y, 1.]]
    )


def reflect(axis: Axis, n=3) -> np.ndarray:
    m = np.eye(n)
    m[axis.value, axis.value] = -1
    return m


def scale(vector) -> np.ndarray:
    n = len(vector)
    matrix = np.eye(n, n)
    for i, x in enumerate(vector):
        matrix[i, i] = x
    return matrix


def rotate2D(angle: float):
    s, c = np.sin(angle), np.cos(angle)
    return np.array([
        [c, -s, 0],
        [s, c, 0],
        [0, 0, 1]
    ])


def scale_translate(sc, tr):
    sx, sy, _ = sc
    tx, ty, _ = tr
    return np.array(
            [[sx, 0., 0.],
             [0., sy, 0.],
             [tx, ty, 1.]]
    )


def rel_transform(p, *trs):
    n = len(p)
    m = None
    for t in trs:
        if m is None:
            m = t
        else:
            m = m @ t
    return translate(p * hpt(-1, -1)) + m + translate(p)


def rad(degrees: float) -> float:
    return degrees * (np.pi / 180.)


def vlen(vec):
    """Calculates the length of a vector"""
    return np.sqrt(np.sum(vec ** 2))
