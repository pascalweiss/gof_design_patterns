import unittest
from patterns.creational.factory_method.creator import *


class TestClient(unittest.TestCase):
    def test_italian_trees(self):
        tree_factory = ItalianTreeFactory()
        forest = [tree_factory.create_tree() for _ in range(1000)]
        for tree in forest:
            assert tree.get_name() in ["cork oak", "olive", "cypress"]

    def test_german_trees(self):
        tree_factory = GermanTreeFactory()
        forest = [tree_factory.create_tree() for _ in range(1000)]
        for tree in forest:
            assert tree.get_name() in ["pine", "beech", "spruce"]
