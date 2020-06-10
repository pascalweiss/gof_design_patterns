from creational.prototype.prototype import Circle


def get_circles(shapes):
    return [s for s in shapes if isinstance(s, Circle)]