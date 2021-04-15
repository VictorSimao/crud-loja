from src.category.dao.category_dao import CategoryDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao
from src.category.model.category_model import Category

class CategoryInput:
    def __init__(self):
        self.category_dao = CategoryDAO()
        self.category_id = 0

    def list_categories(self):
        categories = self.category_dao.read_all()
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)
    
    def create_category(self):
        category_name = input("Escreva o nome da categoria:")
        category_description = input("Escreva a descrição da categoria:")
        category = Category(category_name, category_description)
        self.category_id = self.category_dao.create(category)

    def delete_category(self):
        category_to_delete = input("Informe o id da categoria a deletar:")
        categories = self.category_dao.delete(category_to_delete)

    def update_category(self):
        category_id = input("Informe o id da categoria a editar:")
        category_name = input("Digite um novo nome:")
        category_description = input("Digite uma nova descrição:")
        category_to_update = Category(category_name, category_description)
        updated_category = self.category_dao.update(category_to_update, category_id)