import sys

from src.category.dao.category_dao import CategoryDAO
from src.product.dao.product_dao import ProductDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao
from src.category.model.category_model import Category
from src.product.model.product_model import Product

class Main:
    def __init__(self):
        self.category_dao = CategoryDAO()
        self.product_dao = ProductDAO()
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

    def get_user_input(self):
        print("""O que você deseja fazer? Selecione uma das opções abaixo:
        1. Listar os produtos
        2. Cadastrar um produto
        3. Listar as categorias
        4. Cadastrar uma categoria
        5. Sair
        6. Exluir""")
        choice = input()
        self.get_choice(choice)

    def get_choice(self, choice):
        if choice == "1":
            products = self.product_dao.read_all()
            for prod in products:
                data = f"{prod.id} - {prod.name} - {prod.description} - {prod.price}"
                print(data)
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
            self.product_id = self.product_dao.create(product)
            for selected_category in selected_categories:
                self.product_category_dao.insert_data_product_category(self.product_id, selected_category)
        elif choice == "3":
            categories = self.category_dao.read_all()
            for cat in categories:
                data = f"{cat.id} - {cat.name} - {cat.description}"
                print(data)
        elif choice == "4":
            category_name = input("Escreva o nome da categoria:")
            category_description = input("Escreva a descrição da categoria:")
            category = Category(category_name, category_description)
            self.category_id = self.category_dao.create(category)
        elif choice == "5":
            sys.exit(1)
        elif choice == "6":
            products = self.product_dao.read_all()
            for prod in products:
                data = f"{prod.id} - {prod.name} - {prod.description} - {prod.price}"
                print(data)
            print('Digite o produto que você deseja excluir:')
            choice = input()
            self.product_dao.delete(choice)
        else:
            print("Opção inválida")
            self.get_user_input()

Main()

