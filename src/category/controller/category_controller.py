from src.category.dao.category_dao import CategoryDAO
from src.category.model.category_model import Category
from src.product_category.dao.product_category_dao import ProductCategoryDao
from typing import List

class CategoryController:

    def __init__(self):
        self.category_dao = CategoryDAO()
        self.category_dao.create_table_category()
        self.product_category_dao = ProductCategoryDao()

    def get_categories(self)-> List[Category]:
       return self.category_dao.read_all()

    def create_category(self, category:Category):
        category_id = self.category_dao.create(category) 
           
    def update_category(self, category:Category):
        category_id = self.category_dao.update(category)
        self.product_category_dao.delete_category_id(category_id)

    def delete_category(self, id:int):
        self.product_category_dao.delete_product_id(id)
        self.category_dao.delete(id)
