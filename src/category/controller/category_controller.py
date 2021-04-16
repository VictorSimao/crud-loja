from src.category.model.category_model import Category
from src.database.dao import Dao
from src.category.dao.category_dao import CategoryDAO

class CategoryController:
    def __init__(self):
        self.category_dao = CategoryDAO()
        
    def cadastar_category(self):
        category_name = input("Digite o nome da categoria: ")
        category_description = input("Digite a descrição da categoria: ")
        category = Category(category_name, category_description)
        self.category_dao.create(category)

        



        



