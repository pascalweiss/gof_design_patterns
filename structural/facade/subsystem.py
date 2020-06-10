

# --- Domain ---

class Product:
    name = None

    def __init__(self, uid):
        self.uid = uid

# --- Services ---


class PaymentService:
    @staticmethod
    def make_payment(product):
        print("PaymentService makes payment for product.py {}".format(product.uid))
        return True


class InventoryService:
    @staticmethod
    def is_available(product):
        print("InventoryService checks availability for product.py {}".format(product.uid))
        return True


class ShippingService:
    @staticmethod
    def ship(product):
        print("ShippingService ships product.py {}".format(product.uid))
        pass
