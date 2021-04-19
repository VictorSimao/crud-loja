from src.dao.product_dao import ProductDAO
from src.model.product_model import Product


class ProductController:

    def __init__(self):
        self.dao = ProductDAO()

    def create(self, name, description, price):
        model = Product(name, description, price)
        return self.dao.create(model)

    def read(self):
        list_models = self.dao.read()
        return list_models
    

    def read_by_id(self, product_id: int):
        return self.dao.read_by_id(product_id)

    def update(self, product):
        self.dao.update(product)

    def delete(self, product_id):
        self.dao.delete(product_id)
