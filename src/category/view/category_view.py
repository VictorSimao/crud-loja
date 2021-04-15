from src.category.controller.category_controller import CategoryController
from src.category.model.category_model import Category

class CategoryView:

    def __init__(self):
        self.category_controller = CategoryController()

    def list_categories(self):
        categories = self.category_controller.get_categories()
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)

    def create_category(self):
        category_name = input("Escreva o nome da categoria:")
        category_description = input("Escreva a descrição da categoria:")
        category = Category(category_name, category_description)
        category_id = self.category_controller.create_category(category)   

    def update_category(self):
        self.list_categories()
        category_id = input("Escolha o ID da categoria que deseja atualizar:")
        category_name = input("Escreva o novo nome da categoria:")
        category_description = input("Escreva a nova descrição da categoria:")
        category = Category(category_name, category_description, category_id)
        self.category_controller.update_category(category)
    
    def delete_category(self):
        self.list_categories()
        category_id = input("Escolha o ID da categoria que deseja deletar:")
        self.category_controller.delete_category(category_id)