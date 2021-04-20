from src.model.category_model import Category
from src.dao.category_dao import CategoryDAO


class CategoryController:

    def __init__(self):
        self.dao = CategoryDAO()

    def create(self, name, description):
        category = Category(name, description)
        category_id = self.dao.create(category)
        return category_id

    def read(self):
        categories = self.dao.read_all()
        return categories  
     
    def read_by_id(self, category_id):
        category = self.dao.read_by_id(category_id)
        return category               

    def update(self, category):        
        self.dao.update(category)

    def delete(self, category_id):
        self.dao.delete(category_id)
