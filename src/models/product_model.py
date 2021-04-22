"""
This class converts an object to Product type.
"""


class Product:

    def __init__(self, name:str, description:str, price:float, categories:list=None, id:int=None):
        self.name = name
        self.description = description
        self.price = price
        self.categories = categories
        self.id = id

    def __str__(self):
        return f"{self.id} - {self.name} - {self.description} - {self.price} - {[str(cat) for cat in self.categories]}"