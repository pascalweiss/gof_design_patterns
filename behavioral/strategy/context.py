class Context:
    def __init__(self, strategy, context_data):
        self.strategy = strategy
        self.context_data = context_data

    def run(self):
        return self.strategy.algorithm_interface(self.context_data)
