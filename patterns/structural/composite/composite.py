class Component:
    def __init__(self, name, price=""):
        self.name = name; self.price = price

    def add(self, component):
        raise NotImplementedError

    def remove(self, component):
        raise NotImplementedError


class Composite(Component):
    def __init__(self, name, price=""):
        super().__init__(name, price)
        self.children = []

    def add(self, component):
        self.children.append(component)
        return self

    def remove(self, component):
        self.children = [c for c in self.children if c is not component]
        return self


class Leaf(Component):
    pass
