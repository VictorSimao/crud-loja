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

    def read_all_category(self):

        categories = self.category_dao.read_all()
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)

    def update_category(self):

        self.read_all_category()
        category_id = input("Escolha uma categoria para editar:")
        category = self.category_dao.read_by_id(category_id)
        data = f"{category.id} - {category.name} - {category.description}"
        print(data)
        category_name = input("Escreva o nome da categoria:")
        category.name = category_name
        category_description = input("Escreva a descrição da categoria:")
        category.description = category_description
        self.category_dao.update(category)
