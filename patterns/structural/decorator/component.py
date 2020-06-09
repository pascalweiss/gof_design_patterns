

# --- Component ---

class Beverage:
    def cost(self):
        raise NotImplementedError


# --- Concrete Component ---

class Espresso(Beverage):
    def cost(self):
        return 1


class Decaf(Beverage):
    def cost(self):
        return 2
