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

    def get_user_input(self):
        print("""O que você deseja fazer? Selecione uma das opções abaixo:
        1. Listar os produtos
        2. Cadastrar um produto
        3. Listar as categorias
        4. Cadastrar uma categoria
        5. Excluir Produtos
        6. Sair""")
        choice = input()
        self.get_choice(choice)

    def get_choice(self, choice):
        if choice == "1":
            Product.list_product(self)
        elif choice == "2":
            Product.register_product(self)
        elif choice == "3":
            Category.list_category(self)
        elif choice == "4":
            Category.register_category(self)
        elif choice == "5":
            Product.delected_produtcs(self)
        elif choice == "6":
            sys.exit(1)
        else:
            print("Opção inválida")
            self.get_user_input()

Main()