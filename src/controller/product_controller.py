from src.dao.product_dao import ProductDAO
from src.model.product_model import Product

class ProductController:

    def __init__(self):
        self.dao = ProductDAO()

    def create(self, name, description, price, categories):
        product = Product(name, description, price, categories)
        product_id = self.dao.create(product)
        return product_id

    def read(self):
        list_models = self.dao.read_all()
        return list_models

    def update(self):
        model = Product()
        self.dao.update_product(model)

    def delete(self):
        id = 0
        self.dao.delete_product(id)