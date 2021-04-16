import sys

from src.category.dao.category_dao import CategoryDAO
from src.category.controller.category_controller import CategoryController
from src.product.dao.product_dao import ProductDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao
from src.category.model.category_model import Category
from src.product.model.product_model import Product


class Main:
    def __init__(self):
        self.category_dao = CategoryDAO()
        self.product_dao = ProductDAO()
        self.category_controller = CategoryController()
        self.product_id = 0
        self.category_id = 0
        self.product_category_dao = ProductCategoryDao()
        self.controller()

    def controller(self):

        self.category_dao.create_table_category()
        self.product_dao.create_table_product()
        self.product_category_dao.create_table_product_category()

        while True:
            self.get_user_input()
        # category = Category('categoryName','cate')
        # categories = [category]
        # print(category.name, type(category.name))
        # last_category = self.category_dao.insert_data_category(category)

        # self.product_category.insert_data_product_category(last_product,last_category)

    def get_product_category(self):
        products = self.product_dao.read_all_products()

        for prod in products:
            products_categories = self.product_category_dao.read_categories_by_product_id(prod.id,)
            list_categories = []
            for prod_cat in products_categories:
                category = self.category_dao.read_by_id(prod_cat.category_id)
                list_categories.append(category)
            prod.categories = list_categories
            print(prod)

    def get_user_input(self):
        print("""O que você deseja fazer? Selecione uma das opções abaixo:
        1. Listar os produtos
        2. Cadastrar um produto
        3. Listar as categorias
        4. Cadastrar uma categoria
        5. Sair""")
        choice = input()
        self.get_choice(choice)

    def get_choice(self, choice):
        if choice == "1":
            self.get_product_category()
        elif choice == "2":
            product_name = input("Escreva o nome do produto:")
            product_description = input("Escreva a descrição do produto:")
            product_price = input("Escreva o preço do produto:")
            selected_categories = []
            while True:
                print("Selecione uma das categorias abaixo:")
                categories = self.category_dao.read_all()
                for cat in categories:
                    data = f"{cat.id} - {cat.name} - {cat.description}"
                    print(data)
                selected_categories.append(input())
                option = input("Você deseja cadastrar mais uma categoria? (s/N)")
                if option == "s":
                    continue
                else:
                    break
                print(selected_categories)

            product = Product(product_name, product_description, product_price, selected_categories)
            self.product_id = self.product_dao.create_product(product)
            for selected_category in selected_categories:
                self.product_category_dao.insert_data_product_category(self.product_id, selected_category)

        elif choice == "3":
            categories = self.category_dao.read_all()
            for cat in categories:
                data = f"{cat.id} - {cat.name} - {cat.description}"
                print(data)
        elif choice == "4":
            self.category_controller.create_category()
        elif choice == "5":
            sys.exit(1)
        else:
            print("Opção inválida")
            self.get_user_input()


Main()
