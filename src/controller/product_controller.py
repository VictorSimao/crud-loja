from src.dao.product_dao import ProductDAO
from src.model.product_model import Product

class ProductController:

    def __init__(self):
        self.dao = ProductDAO()

    def create(self):
        model = Product()
        self.dao.create_product(model)

    def read(self):
        list_models = self.dao.read_all_products()
        return list_models

    def update(self):
        model = Product()
        self.dao.update_product(model)

    def delete(self):
        id = 0
        self.dao.delete_product(id)