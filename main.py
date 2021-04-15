from src.controllers.category_controller import CategoryController 

from src.controllers.product_controller import ProductController

import sys


"""
This class is the first called, it's responsible to get user input and 
share with controllers
"""


class Main:


    def __init__(self):
        self.category_controller = CategoryController()
        self.product_controller = ProductController()
        self.user_choice = None
        self.show_menu()

    def show_menu(self):
        while True:
            print("""\nO que você deseja fazer? Selecione uma das opções abaixo:
            1. Listar os produtos
            2. Cadastrar um produto
            3. Atualizar um produto
            4. Deletar um produto
            5. Listar as categorias
            6. Cadastrar uma categoria
            7. Atualizar uma categoria
            8. Deletar uma categoria
            9. Sair""")
            self.user_choice = input()
            self.process_choice()

    def process_choice(self):
        if self.user_choice == "1":
            self.product_controller.get_all_products()
        elif self.user_choice == "2":
            self.product_controller.create_new_product()
        elif self.user_choice == "3":
            self.product_controller.update_product()
        elif self.user_choice == "4":
            self.product_controller.delete_product()
        elif self.user_choice == "5":
            self.category_controller.get_all_categories()
        elif self.user_choice == "6":
            self.category_controller.create_new_category()
        elif self.user_choice == "7":
            self.category_controller.update_category()
        elif self.user_choice == "8":
            self.category_controller.delete_category()
        elif self.user_choice == "9":
            sys.exit(1)
        else:
            print("Opção inválida")
            self.show_menu()

Main()