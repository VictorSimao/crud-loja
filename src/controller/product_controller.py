from src.dao.product_dao import ProductDAO

from src.dao.product_category_dao import ProductCategoryDao

from src.model.product_model import Product

from src.model.product_category_model import ProductCategory


class ProductController:

    def __init__(self):
        self.product_dao = ProductDAO()
        self.product_category_dao = ProductCategoryDao()

    def create(self, product_name, product_description, product_price, selected_categories):
        product = Product(product_name, product_description, product_price, categories=selected_categories)
        self.product_id = self.product_dao.create(product)
        
        for selected_category in selected_categories:
            product_category = ProductCategory(self.product_id, selected_category)
            self.product_category_dao.create(product_category)


    def read(self):
        list_models = self.product_dao.read_all()
        return list_models


    def update(self, product_id, product_name, product_description, product_price, selected_categories):
        model = Product(product_name, product_description, product_price, id=product_id, categories=selected_categories)
        self.product_dao.update(model)


    def delete(self, id: int):
        self.product_dao.delete(id)
        self.product_category_dao.delete(id)