from src.daos.category_dao import CategoryDAO

from src.models.category_model import Category


"""
This class serves to control the data between user inputs and category DAO
"""


class CategoryController:

    def __init__(self):
        self.category_dao = CategoryDAO()

    def create(self, category):
        new_category = Category(
            category['name'],
            category['description']
        )
        category['id'] = self.category_dao.create(new_category)
        return category['id']

    def read(self):
        categories = self.category_dao.read_all()
        return categories

    def read_by_id(self, id):
        return self.category_dao.read_by_id(id)

    def update(self, category):

        updated_category = Category(
            category['name'],
            category['description'],
            category['id']
        )

        self.category_dao.update(updated_category)

    def delete(self, id):
        self.category_dao.delete(id)
