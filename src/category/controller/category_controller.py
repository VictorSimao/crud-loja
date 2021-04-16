from src.category.model.category_model import Category
from src.category.dao.category_dao import CategoryDAO


class CategoryController:

    def __init__(self):
        self.category_dao = CategoryDAO()

    def create_category(self):

        category_name = input("Escreva o nome da categoria:")
        category_description = input("Escreva a descrição da categoria:")
        category = Category(category_name, category_description)
        self.category_id = self.category_dao.create(category)