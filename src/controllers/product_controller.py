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
        self.category_dao = CategoryDAO()
        self.product_category_dao = ProductCategoryDao()

    def create(self, name: str, description: str, price: int, categories: list = None):
        new_product = Product(name, description, price, categories)
        product_id = self.product_dao.create(new_product)
        self.__create_product_category(product_id, categories)

    def read(self):
        products = self.product_dao.read_all()
        return products

    def read_by_id(self, id: int):
        return self.product_dao.read_by_id(id)

    def update(self, id: int, name: str, description: str, price: int, categories: list = None):
        updated_product = Product(name, description, price, categories, id)
        if categories:
            self.__delete_product_category(id)
            self.__create_product_category(id, categories)
        self.product_dao.update(updated_product)

    def delete(self, id: int):
        self.__delete_product_category(id)
        self.product_dao.delete(id)

    def get_categories(self):
        categories = self.category_dao.read_all()
        return categories

    def __create_product_category(self, product_id: int, categories: int):
        for selected_category in categories:
            self.product_category_dao.create(product_id, selected_category)

    def __delete_product_category(self, product_id: int, category_id: int = None):
        if category_id:
            self.product_category_dao.delete_category_by_product_id(
                product_id, category_id)
        else:
            self.product_category_dao.delete(product_id)
