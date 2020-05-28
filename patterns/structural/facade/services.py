

class PaymentService:
    @staticmethod
    def make_payment(product):
        print("PaymentService makes payment for product {}".format(product.uid))
        return True


class InventoryService:
    @staticmethod
    def is_available(product):
        print("InventoryService checks availability for product {}".format(product.uid))
        return True


class ShippingService:
    @staticmethod
    def ship(product):
        print("ShippingService ships product {}".format(product.uid))
        pass
