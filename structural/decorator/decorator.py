from structural.decorator.component import Beverage


# --- Decorator ---

class AddonBeverage(Beverage):
    def __init__(self, b: Beverage):
        self.beverage = b

    def cost(self):
        raise NotImplementedError


# --- ConcreteDecorator ---

class Soy(AddonBeverage):
    def cost(self):
        return self.beverage.cost() + 1


class Caramel(AddonBeverage):
    def cost(self):
        return self.beverage.cost() + 2
