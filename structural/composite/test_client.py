"""
- Pattern Name -
Composite

- Intent -
"Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat
individual objects and compositions of objects uniformly." (GoF - Design Patterns)
"""

import unittest
from structural.composite.composite import *


class TestClient(unittest.TestCase):
    def test(self):
        clothes = Composite("Clothes")
        shirts = Composite("Shirts")
        green_shirt = Leaf("Green Shirt", 29.99)
        red_shirt = Leaf("Red Shirt", 25.99)
        pants = Composite("Pants")
        jeans = Leaf("Jeans", 69.99)
        chino = Leaf("Chino", 79.99)

        clothes.add(shirts).add(pants)
        shirts.add(green_shirt).add(red_shirt)
        pants.add(jeans).add(chino)
