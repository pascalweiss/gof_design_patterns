"""
- Pattern Name -
Strategy

- Intent -
"Define a family of algorithms, encapsulate each one, and make them interchange-
able. Strategy lets the algorithm vary independently from clients that use it." (GoF - Design Patterns)

- Also Known As -
Policy
"""

import unittest
from hamcrest import equal_to, assert_that
from patterns.behavioral.strategy.context import Context
from patterns.behavioral.strategy.strategy import ConcreteStrategyA, ConcreteStrategyB


class TestClient(unittest.TestCase):
    def test_a(self):
        strategy = ConcreteStrategyA()
        context = Context(strategy, "my context")
        assert_that(context.run(), equal_to("applied strategy a in context: my context"))

    def test_b(self):
        strategy = ConcreteStrategyB()
        context = Context(strategy, "my context")
        assert_that(context.run(), equal_to("applied strategy b in context: my context"))

