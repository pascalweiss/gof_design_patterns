import unittest

from patterns.structural.facade.facade import OrderFacade


class Controller:
    def __init__(self, facade: OrderFacade):
        self.facade = facade

    def order_product(self, product_id):
        print("controller receives order request")
        success = self.facade.place_order(product_id)
        return success


class TestClient(unittest.TestCase):

    def setUp(self) -> None:
        facade = OrderFacade()
        # inject the facade in controller
        self.controller = Controller(facade)

    def test_order(self):
        success = self.controller.order_product(42)
        assert success
