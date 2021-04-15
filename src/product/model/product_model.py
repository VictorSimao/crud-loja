from typing import List
from src.category.model.category_model import Category

class Product:
    def __init__(self, name, description, price, categories:List[Category] = [], id = None):
        self.name = name
        self.description = description
        self.price = price
        self.categories = categories
        self.id = id
        
        