class Product:
    def __init__(self, name, description, price, id=None, categories=None):
        self.name = name
        self.description = description
        self.price = price
        self.categories = categories
        self.id = id
