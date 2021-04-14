from src.daos.product_dao import ProductDAO
from src.daos.category_dao import CategoryDAO
from src.daos.product_category_dao import ProductCategoryDao

from src.models.product_model import Product
from src.utils.utils import format_print

class ProductController:
    def __init__(self):
        self.product_dao = ProductDAO()
        self.category_dao = CategoryDAO()
        self.product_category_dao = ProductCategoryDao()
        self.product = {
            'id': 0,
            'name': '',
            'description': '',
            'price': 0.0,
            'categories': []
        }
        self.create_products_table()

    def create_products_table(self):
        self.product_dao.create_table_product()
        self.product_category_dao.create_table_product_category()

    def create_new_product(self):
        self.product['name'] = input("\nEscreva o nome do produto: ")
        self.product['description'] = input("\nEscreva a descrição do produto: ")
        self.product['price'] = input("\nEscreva o preço do produto: ")

        self.get_categories()
        new_product = Product(
            self.product['name'], 
            self.product['description'], 
            self.product['price'],
            self.product['categories']
        )
        self.product['id'] = self.product_dao.create(new_product)
        self.create_product_category()

    def get_all_products(self):
        products = self.product_dao.read_all()
        format_print(products)

    def get_categories(self):
        while True:
            print("\nSelecione uma das categorias abaixo:\n")
            categories = self.category_dao.read_all()
            format_print(categories)

            selected_category = input()
            self.product['categories'].append(selected_category)
            option = input("\nVocê deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break

    def create_product_category(self):
        for selected_category in self.product['categories']:
            self.product_category_dao.create(self.product['id'], selected_category)
