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
==============================
--------- M E N U ------------
==============================
1. Listar os produtos
2. Cadastrar um produto
3. Atualizar um produto
4. Deletar um produto
5. Listar as categorias
6. Cadastrar uma categoria
7. Atualizar uma categoria
8. Deletar uma categoria
x. Sair
Opção: """)
            choice = input()
            self.get_choice(choice)

    def get_choice(self, choice):
        if choice == "1":  # Listar Produtos
            self.product_controller.read_product()
        elif choice == "2":  # Cadastrar Produto
            product_id = self.product_controller.create_product()
            self.category_controller.read_category()
            self.product_category_controller.create_prod_cat(product_id)
        elif choice == "3":  # Atualizar Produto
            self.product_controller.read_product()
            product_id = self.product_controller.update_product()
            self.category_controller.read_category()
            self.product_category_controller.update_prod_cat(product_id)
        elif choice == "4":  # Deletar Produto
            self.product_controller.read_product()
            product_id = self.product_controller.delete_product()
            self.product_category_controller.delete_prod_cat(product_id)
        elif choice == "5":  # Listar Categorias
            self.category_controller.read_category()
        elif choice == "6":  # Cadastrar Categoria
            self.category_controller.create_category()
        elif choice == "7":  # Atualizar Categoria
            self.category_controller.read_category()
            self.category_controller.update_category()
        elif choice == "8":  # Deletar Categoria
            self.category_controller.read_category()
            self.category_controller.delete_category()
        elif choice == "x":
            sys.exit(1)
        else:
            print("Opção inválida")
            self.menu()


Main()
