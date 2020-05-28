import unittest

from patterns.structural.facade.controller import Controller
from patterns.structural.facade.facade import OrderFacade


class TestClient(unittest.TestCase):

    def setUp(self) -> None:
        facade = OrderFacade()
        # inject the facade in controller
        self.controller = Controller(facade)

    def test_order(self):
        success = self.controller.order_product(42)
        assert success
