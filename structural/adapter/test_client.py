"""
- Pattern Name -
Adapter

- Intent -
"Convert the interface of a class into another interface clients expect. Adapter lets
classes work together that couldn't otherwise because of incompatible interfaces." (GoF - Design Patterns)

- Also Known As -
Wrapper

- Example -
The user has to apply the function target_invoker put can't change it. It requires an argument of type
InvokerTarget. But the target that the user actually wants use is of type UserTarget. The problem is, that
UserTarget is not compatible with target_invoker.
"""

import unittest
from hamcrest import equal_to, assert_that
from structural.adapter.adapter import InvokerTargetAdapter
from structural.adapter.target import InvokerTarget


def target_invoker(target: InvokerTarget):
    return target.request()


class TestClient(unittest.TestCase):

    def test(self):
        target = InvokerTargetAdapter()
        assert_that(target_invoker(target), equal_to("Response by UserTarget"))
