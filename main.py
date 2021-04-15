import sys

from src.category.view.category_view import CategoryView
from src.product.view.product_view import ProductView

class Main:
    def __init__(self):
        self.category_view = CategoryView()
        self.product_view = ProductView()
        self.controller()


    def controller(self):

        while True:
            self.get_user_input()


    def get_user_input(self):
        print("""O que você deseja fazer? Selecione uma das opções abaixo:
        1. Listar os produtos
        2. Cadastrar um produto
        3. Atualizar um produto
        4. Deletar um produto
        5. Listar as categorias
        6. Cadastrar uma categoria
        7. Atualizar um produto
        8. Deletar um produto
        9. Sair""")
        choice = input()
        self.get_choice(choice)
  

    def get_choice(self, choice):
        if choice == "1":
            self.product_view.list_products()
        elif choice == "2":
            self.product_view.create_product()
        elif choice == "3":
            self.product_view.update_product()
        elif choice == "4":
            self.product_view.delete_product()
        elif choice == "5":
            self.category_view.list_categories()
        elif choice == "6":
            self.category_view.create_category()
        elif choice == "7":
            self.category_view.update_category()
        elif choice == "8":
            self.category_view.delete_category()
        elif choice == "9":
            sys.exit(1)
        else:
            print("Opção inválida")
            self.get_user_input()


Main()