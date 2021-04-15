class Product:
    def __init__(self, name, description, price, id=None, categories=[]):
        self.name = name
        self.description = description
        self.price = price
        self.id = id 
        self.categories = categories