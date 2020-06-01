import random
from patterns.creational.factory_method.tree import *


# ---------------- Creator ---------------------

class TreeFactory:
    def create_tree(self):
        raise NotImplementedError


# ------------ ConcreteCreator -------------------

class ItalianTreeFactory(TreeFactory):
    def create_tree(self):
        return random.choice([lambda: CorkOak(), lambda: Olive(), lambda: Cypress()])()


class GermanTreeFactory(TreeFactory):
    def create_tree(self):
        return random.choice([lambda: Spruce(), lambda: Beech(), lambda: Pine()])()
esig