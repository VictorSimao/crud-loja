from src.model.product_model import Product
from src.dao.product_dao import ProductDAO

class ProductController:

    def __init__(self):
        self.dao = ProductDAO()

    def create(self, name, description, price, categories):
        product = Product(name, description, price, categories=[])
        product_id = self.dao.create(product)
        return product_id

    def read(self):
        list_models = self.dao.read_all()
        return list_models
    
    def read_by_id(self, product_id):
        product = self.dao.read_by_id(product_id)
        return product

    def update(self):
        model = Product()
        self.dao.update_product(model)

    def delete(self, product_id):
        self.dao.delete(product_id)