class Product:
    def __init__(self, product_id, name, price, description):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description


class CreateBodyProduct:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description


class UpdateBodyProduct:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
