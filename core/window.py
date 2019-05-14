import numpy as np
import typing as tp
from geometry import rotate2D, hpt, pt, rad


class Window:

    def __init__(self, center, size):
        self.center = center
        self.size = size
        self.axes = np.eye(3)
        self._ppc: tp.Optional[np.ndarray] = None

    @property
    def origin(self):
        sz = (.5 * self.size) * (self.x + self.y)
        return hpt(*(self.center - sz)[:-1])

    @property
    def angle(self):
        x, y, _ = self.y
        return np.arctan2(x, y)

    @property
    def width(self) -> float:
        return self.size[0]

    @property
    def height(self) -> float:
        return self.size[1]

    @property
    def x(self):
        return self.axes[0]

    @property
    def y(self):
        return self.axes[1]

    @property
    def z(self):
        return self.axes[2]

    def move_up(self, amount):
        self.center += self.y * amount

    def move_down(self, amount):
        self.center += self.y * -amount

    def move_left(self, amount: float):
        self.center += self.x * -amount

    def move_right(self, amount: float):
        self.center += self.x * amount

    def zoom_in(self, amount: float):
        self.center += pt(amount, amount, 0)
        self.size -= pt(2 * amount, 2 * amount, 0)

    def zoom_out(self, amount: float):
        self.center -= pt(amount, amount, 0)
        self.size += pt(2 * amount, 2 * amount, 0)

    def rotate(self, angle):
        self.axes = self.axes @ rotate2D(rad(angle))

    def __repr__(self):
        return f"Window(origin={self.origin}, x={self.x}, y={self.y}, z={self.z}))"
