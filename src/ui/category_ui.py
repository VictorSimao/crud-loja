from src.category.dao.category_dao import CategoryDAO
from src.product.dao.product_dao import ProductDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao
from src.category.model.category_model import Category
from src.product.model.product_model import Product

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