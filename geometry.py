import numpy as np


def translate(n: int, point) -> np.ndarray:
    matrix = np.eye(n, n)
    m = n - 1
    for i, x in enumerate(point):
        matrix[m, i] = x
    return matrix


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

