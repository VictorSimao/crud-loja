from src.dao.product_dao import ProductDAO

from src.dao.product_category_dao import ProductCategoryDao

from src.model.product_model import Product

from src.model.product_category_model import ProductCategory


class ProductController:

    def __init__(self):
        self.product_dao = ProductDAO()
        self.product_category_dao = ProductCategoryDao()

    def create(self, product_name, product_description, product_price, selected_categories):
        product = Product(product_name, product_description, product_price, selected_categories)
        self.product_id = self.product_dao.create(product)
        
        for selected_category in selected_categories:
            product_category = ProductCategory(self.product_id, selected_category)
            self.product_category_dao.create(product_category)

    def read(self):
        list_models = self.product_dao.read_all()
        return list_models

    def update(self):
        model = Product()
        self.product_dao.update_product(model)

    def delete(self):
        id = 0
        self.product_dao.delete_product(id)