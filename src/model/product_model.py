class Product:
    def __init__(self, name, description, price, id=None, categories=[]):
        self.name = name
        self.description = description
        self.price = price
        self.id = id
        self.categories = categories

    def __str__(self):
        return f"{self.id} - {self.name} - {self.description} - {self.price} - {self.categories}"
