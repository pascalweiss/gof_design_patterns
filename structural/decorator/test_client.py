import unittest
from hamcrest import equal_to, assert_that
from structural.decorator.component import Espresso, Decaf
from structural.decorator.decorator import Caramel, Soy


class TestClient(unittest.TestCase):
    def test_soy_caramel_espresso(self):
        espresso = Espresso()
        caramel_espresso = Caramel(espresso)
        soy_caramel_espresso = Soy(caramel_espresso)

        assert_that(soy_caramel_espresso.cost(), equal_to(4))

    def test_soy_decaf(self):
        decaf = Decaf()
        soy_decaf = Soy(decaf)

        assert_that(soy_decaf.cost(), equal_to(3))
