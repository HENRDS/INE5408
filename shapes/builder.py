from .point import Point


class GraphicObjectBuilder:
    def __init__(self):
        self.vertices = []


    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def point(self, vertex) -> Point:
        return Point("", *self.vertices[vertex])

