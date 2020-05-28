from patterns.structural.facade.domain import Product
from patterns.structural.facade.services import *


class IFacade:
    def place_order(self, product_id):
        raise NotImplementedError


class OrderFacade(IFacade):
    def place_order(self, product_id):
        order_successful = False
        product = Product(product_id)
        if InventoryService.is_available(product):
            payment_successful = PaymentService.make_payment(product)
            if payment_successful:
                ShippingService.ship(product)
                order_successful = True
                print("Order for product {} successful".format(product.uid))
        return order_successful
