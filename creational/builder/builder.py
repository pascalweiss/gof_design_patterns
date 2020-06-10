from creational.builder.product import Product


# --- Abstract ---

class Builder:
    def __init__(self):
        self.product = Product()

    def build_foo(self):
        raise NotImplementedError

    def build_goo(self):
        raise NotImplementedError

    def get_result(self):
        return self.product


# --- Concrete Builders ---

class BuilderRed(Builder):
    def build_foo(self):
        self.product.set_foo("Red foo")

    def build_goo(self):
        self.product.set_goo("Red goo")


class BuilderGreen(Builder):
    def build_foo(self):
        self.product.set_foo("Green foo")

    def build_goo(self):
        self.product.set_goo("Green goo")
