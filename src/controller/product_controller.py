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
        products = self.dao.read_all()
        return products

    def update(self, product):
        self.dao.update(product)

    def delete(self, product_id):
        self.dao.delete(product_id)