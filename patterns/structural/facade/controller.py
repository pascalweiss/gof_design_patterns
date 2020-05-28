from patterns.structural.facade.facade import OrderFacade


class Controller:
    def __init__(self, facade: OrderFacade):
        self.facade = facade

    def order_product(self, product_id):
        print("controller receives order request")
        success = self.facade.place_order(product_id)
        return success
