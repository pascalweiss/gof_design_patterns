import unittest
from hamcrest import assert_that, equal_to
from patterns.creational.builder.builder import BuilderRed, BuilderGreen
from patterns.creational.builder.director import Director


class TestClient(unittest.TestCase):

    def test_red_product(self):
        director = Director(BuilderRed())
        product = director.construct()
        assert_that(product.foo, equal_to("Red foo"))
        assert_that(product.goo, equal_to("Red goo"))

    def test_green_product(self):
        director = Director(BuilderGreen())
        product = director.construct()
        assert_that(product.foo, equal_to("Green foo"))
        assert_that(product.goo, equal_to("Green goo"))
