

# ------------------- Interface --------------------------

class Strategy:

    def algorithm_interface(self, context_data):
        raise NotImplementedError


# -------------- Concrete Strategies ---------------------

class ConcreteStrategyA(Strategy):
    def algorithm_interface(self, context_data):
        return "applied strategy a in context: " + context_data


class ConcreteStrategyB(Strategy):
    def algorithm_interface(self, context_data):
        return "applied strategy b in context: " + context_data
