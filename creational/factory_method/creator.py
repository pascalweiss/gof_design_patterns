import random
from creational.factory_method.product import *


# --- Creator ---

class TreeFactory:
    def create_tree(self):
        raise NotImplementedError


# --- Concrete Creator ---

class ItalianTreeFactory(TreeFactory):
    def create_tree(self):
        return random.choice([lambda: CorkOak(), lambda: Olive(), lambda: Cypress()])()


class GermanTreeFactory(TreeFactory):
    def create_tree(self):
        return random.choice([lambda: Spruce(), lambda: Beech(), lambda: Pine()])()