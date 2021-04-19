from src.dao.product_dao import ProductDAO
from src.dao.product_category_dao import ProductCategoryDAO
from src.dao.category_dao import CategoryDAO
from src.model.product_model import Product
from src.model.category_model import Category

class ProductController:

    def __init__(self):
        self.product_dao = ProductDAO()
        self.product_category_dao = ProductCategoryDAO()
        self.category_dao = CategoryDAO()

    def create(self, name, description, price, categories_id):
        product = Product(name, description, price)

        product_id = self.product_dao.create(product)

        for category_id in categories_id:
            self.product_category_dao.create(product_id, category_id)
        return product_id

    def read(self):
        products = self.product_dao.read_all()

        products_categories = []

        for product in products:
            categories = self.category_dao.read_categories_by_product_id(product.id)
            prod = Product(product.name, product.description, product.price, categories = categories, id = product.id)
            products_categories.append(prod)

        return products_categories

    def read_by_id(self, product_id):
        product = self.product_dao.read_by_id_product(product_id)

        categories = self.category_dao.read_categories_by_product_id(product.id)
        product_categorie = Product(product.name, product.description, product.price, categories = categories, id = product.id)

        return product_categorie

    def update(self, product, categories_id):
        product_id = self.product_dao.update(product)

        self.product_category_dao.delete_by_product_id(product.id)

        for category_id in categories_id:
            self.product_category_dao.create(product.id, category_id)

        return product_id

    def delete(self, id):
        self.product_category_dao.delete(id)       
        self.product_dao.delete(id)