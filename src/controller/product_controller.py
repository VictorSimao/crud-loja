from src.dao.product_dao import ProductDAO
from src.model.product_model import Product

class ProductController:

    def __init__(self):
        self.dao = ProductDAO()

    def create(self):
        # model = Product()
        # self.dao.create_product(model)
        product = Product(name, description, price)
        product_id = self.dao.create(product)

    def read(self):
        # list_models = self.dao.read_all_products()
        # return list_models
        products = self.dao.read_all()
        return products

    def read_by_id(self, product_id):
        Product = self.dao.read_by_id(product_id)
        return Product

    def update(self, product):
        # model = Product()
        # self.dao.update_product(model)
        self.dao.update(product)

    def delete(self, product_id):
        # id = 0
        # self.dao.delete_product(id)
        self.dao.delete(product_id)