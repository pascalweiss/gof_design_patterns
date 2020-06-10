"""
- Pattern Name -
Singleton

- Intent -
"Ensure a class only has one instance, and provide a global point of access to it." (GoF - Design Patterns)
"""


import unittest
from creational.singleton.singleton import Singleton


class TestClient(unittest.TestCase):
    def test_single_initialization(self):
        singleton_one = Singleton.get_instance()
        singleton_two = Singleton.get_instance()

        # ensure, that the Singleton.__init__ was called only once
        assert(singleton_two.get_init_count() is 1)
        assert(singleton_one is singleton_two)
