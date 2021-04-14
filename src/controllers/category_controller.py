from src.daos.category_dao import CategoryDAO

from src.models.category_model import Category


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

    def create_new_product(self):
        self.category['name'] = input("\nEscreva o nome da categoria: ")
        self.category['description'] = input("\nEscreva a descrição do produto: ")

        self.get_categories()
        new_category = Category(
            self.category['name'], 
            self.category['category_description']
        )
        self.category['id'] = self.category_dao.create(new_category)
        
    def get_all_categories(self):
        categories = self.category_dao.read_all()
        print("\n")
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)
