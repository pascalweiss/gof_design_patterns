

# --- Client ---
from creational.prototype.prototype import Circle


class Editor:
    def __init__(self, initial_shapes):
        self.shapes = initial_shapes
        self.selected = None

    def select(self, shape):
        self.selected = [s for s in self.shapes if s is shape][0]

    def duplicate(self):
        duplication = self.selected.clone()
        self.selected = duplication
        self.shapes.append(duplication)
