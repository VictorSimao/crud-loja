from src.category.dao.category_dao import CategoryDAO
from src.product.dao.product_dao import ProductDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao
from src.category.model.category_model import Category
from src.product.model.product_model import Product
from typing import List

class ProductController:

    def __init__(self):
        self.category_dao = CategoryDAO()
        self.product_dao = ProductDAO()
        self.product_category_dao = ProductCategoryDao()
        self.product_dao.create_table_product()
        self.product_category_dao.create_table_product_category()

    def get_products(self) -> List[Product]:
        products = self.product_dao.read_all()
        products_list = []
        for product in products:
            product_categories = self.category_dao.read_categories_by_prod_id(product.id)
            product.categories = product_categories
            products_list.append(product)
        return products_list
    
    def create_product(self, product:Product, categories_id:List[int]):
        self.product_id = self.product_dao.create(product)
        for category_id in categories_id:
            self.product_category_dao.create(self.product_id, category_id)

    def update_product(self, product:Product, categories_id:List[int]):
        self.product_dao.update(product)
        self.product_category_dao.delete_product_id(product.id)
        for category_id in categories_id:
            self.product_category_dao.create(product.id, category_id)

    def delete_product(self, id:int):
        self.product_category_dao.delete_product_id(id)
        self.product_dao.delete(id)
