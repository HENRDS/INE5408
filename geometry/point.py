from functools import partial

class Point:
    def __init__(self, x, y, z, t, *other):
        self._coordinates = (x, y, z, t, *other)
        getter = partial(self._coordinates.__getitem__)
        self.x = property()