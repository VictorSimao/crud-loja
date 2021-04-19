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

    def read_categories_by_id(self, product_id):
        product = self.dao.read_categories_by_id_product(product_id)
        return product

    def update(self, product):
        # model = Product()
        # self.dao.update_product(model)
        self.dao.update(product)

    def delete(self, product_id):
        self.dao.delete(product_id)