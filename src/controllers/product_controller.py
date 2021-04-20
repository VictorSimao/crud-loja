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
        self.product = {
            'id': 0,
            'name': '',
            'description': '',
            'price': 0.0,
            'categories': []
        }

    def create(self, name, description, price, categories):
        product = Product(name, description, price, categories)
        product_id = self.product_dao.create(product)
        return product_id

    def read(self):
        products = self.product_dao.read_all()
        return products

    def read_by_id(self, id:int):
        return self.product_dao.read_by_id(id)

    def update(self, product_id, name, description, price, categories):

        updated_product = Product(
            name,
            description,
            price,
            categories,
            product_id
        )

        if categories:
            self.__create_product_category(product)

        self.product_dao.update(updated_product)

    def delete(self, id:int):
        self.product_dao.delete(id)

    def get_categories(self):
        categories = self.category_dao.read_all()
        return categories

    def __create_product_category(self, product:dict):
        for selected_category in product['categories']:
            self.product_category_dao.create(
                product['id'], selected_category)