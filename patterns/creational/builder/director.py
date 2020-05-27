from patterns.creational.builder.builder import Builder


class Director:
    def __init__(self, concrete_builder: Builder):
        self.builder = concrete_builder

    def construct(self):
        self.builder.build_foo()
        self.builder.build_goo()
        return self.builder.get_result()