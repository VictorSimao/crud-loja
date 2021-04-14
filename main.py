import sys

from src.category.controller.category_controller import CategoryController
from src.product.controller.product_controller import ProductController
from src.product_category.controller.product_category_controller import ProductCategoryController


class Main:
    def __init__(self):
        self.category_controller = CategoryController()
        self.product_controller = ProductController()
        self.product_category_controller = ProductCategoryController()
        self.menu()

    def menu(self):
        while True:
            print("""
            =========================================================

            O que você deseja fazer? Selecione uma das opções abaixo:
            1. Listar os produtos
            2. Cadastrar um produto
            3. Listar as categorias
            4. Cadastrar uma categoria
            5. Sair
            
            """)
            choice = input()
            self.get_choice(choice)

    def get_choice(self, choice):
        if choice == "1":
            self.product_controller.read_controller()
        elif choice == "2":
            product = self.product_controller.create_controller()
            self.category_controller.read_controller()
            selected_categories = self.product_controller.add_category()
            self.product_category_controller.create_controller(
                product, selected_categories)
        elif choice == "3":
            self.category_controller.read_controller()
        elif choice == "4":
            categorytest = self.category_controller.create_controller()
        elif choice == "5":
            sys.exit(1)
        else:
            print("Opção inválida")
            self.menu()


Main()
