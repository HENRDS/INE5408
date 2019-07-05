from cairo import Context
import numpy as np
from core import GraphicalObject


class Curve(GraphicalObject):

    def __init__(self, name: str, points: np.ndarray):
        super().__init__(name, points)

def forward_differences(G, delta: float, M):
    C = M @ G
    D = np.array(
            [[0., 0., 0., 1.],
             [delta ** 3, delta ** 2, delta, 0.],
             [6.0 * delta ** 3, 2.0 * delta ** 2, 0., 0.],
             [6.0 * delta ** 3, 0., 0., 0.]]
    ) @ C




class Bezier(Curve):
    MATRIX = np.array(
            [[-1., 3., -3., 1.],
             [3., -6., 3., 0.],
             [-3., 3., 0., 0.],
             [1., 0., 0., 0.]]
    )

    def fwd_differences(self, delta: float):
        pass



