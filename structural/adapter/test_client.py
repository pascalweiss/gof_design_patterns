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
