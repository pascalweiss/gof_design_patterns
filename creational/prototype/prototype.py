# --- Prototype ---

class Shape:
    def clone(self):
        raise NotImplementedError


# --- Concrete Prototypes ---

class Rectangle(Shape):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def clone(self):
        return Rectangle(self.width, self.height, self.color)


class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def clone(self):
        return Circle(self.radius, self.color)


