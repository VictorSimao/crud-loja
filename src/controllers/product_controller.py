from src.daos.product_dao import ProductDAO

from src.daos.category_dao import CategoryDAO

from src.daos.product_category_dao import ProductCategoryDao

from src.models.product_model import Product


"""
This class serves to control the data between user inputs and all the other 
DAOs.
"""


class ProductController:

    def __init__(self):
        self.product_dao = ProductDAO()

    def create(self, name, description, price, categories):
        product = Product(name, description, price, categories)
        product_id = self.product_dao.create(product)
        return product_id
        
    def read(self):
        list_models = self.product_dao.read_all()
        return list_models

    def read_by_id(self, product_id):
        product = self.product_dao.read_by_id(product_id)
        return product

    def update(self, product):
        self.product_dao.update(product)

    def delete(self, product_id):
        self.product_dao.delete(product_id)
