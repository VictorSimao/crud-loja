from src.dao.product_category_dao import ProductCategoryDao
from src.model.product_category_model import ProductCategory

class ProductCategoryController:

    def __init__(self):
        self.dao = ProductCategoryDao()

    def create(self):
        model = Product()
        self.dao.create(model)

    def read(self):
        id = 0
        list_models = self.dao.read_categories_by_product_id(id)
        return list_models

    def delete(self, product_id:int, category_id:int=None):
        if category_id:
            self.dao.delete_category_by_product_id(product_id, category_id)
        else:
            self.dao.delete(product_id)