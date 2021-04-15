from src.daos.category_dao import CategoryDAO

from src.models.category_model import Category

from src.utils.utils import format_print

"""
This class serves to control the data between user inputs and category DAO
"""


class CategoryController:
    

    def __init__(self):
        self.category_dao = CategoryDAO()
        self.category = {
            'id': 0,
            'name': '',
            'description': '',
            'products': []
        }
        self.create_category_table()

    def create_category_table(self):
        self.category_dao.create_table_category()

    def create_new_category(self):
        self.category['name'] = input("\nEscreva o nome da categoria: ")
        self.category['description'] = input("\nEscreva a descrição do produto: ")

        new_category = Category(
            self.category['name'], 
            self.category['description']
        )
        self.category['id'] = self.category_dao.create(new_category)
        
    def get_all_categories(self):
        categories = self.category_dao.read_all()
        format_print(categories)

    def update_category(self):
        self.category['id'] = input("Qual o id da categoria a ser atualizada? ")
        self.category['name'] = input("Qual o novo nome da categoria? ")
        self.category['description'] = input("Qual a nova descrição da categoria? ")

        updated_category = Category(
            self.category['name'], 
            self.category['description'], 
            self.category['id'] 
        )

        self.category_dao.update(updated_category)
    
    def delete_category(self):
        self.category['id'] = input("Qual o id da categoria a ser removida? ")
        self.category_dao.delete(self.category['id'])
