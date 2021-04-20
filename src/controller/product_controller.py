from src.dao.product_dao import ProductDAO
from src.dao.product_category_dao import ProductCategoryDao
from src.model.product_model import Product

class ProductController:

    def __init__(self):
        self.dao = ProductDAO()
        self.product_category_dao = ProductCategoryDao()


    def create(self, name, description, price, categories):
        product = Product(name, description, price, categories)
        product_id = self.dao.create(product)
        return product_id

    def read(self):
        list_models = self.dao.read_all()
        return list_models

    def read_by_id(self, product_id):
        product = self.dao.read_by_id(product_id)
        return product     

    def update(self, product, categories):
        product_id = self.dao.update(product)

        self.product_category_dao.delete_category_by_product_id(product.id)

        for category in categories:
            self.product_category_dao.create(product.id, category)

        return product_id

    def delete(self, product_id):
        self.dao.delete(product_id)