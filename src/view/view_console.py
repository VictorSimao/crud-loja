import sys

from src.controller.product_controller import ProductController
from src.controller.category_controller import CategoryController
from src.controller.product_category_controller import ProductCategoryController

modules = {
    '1': 'Produtos',
    '2': 'Categorias',
    '0': 'Sair'
}
crud_option = {
    '1' : 'Listar',
    '2' : 'Cadastrar',
    '3' : 'Atualizar',
    '4' : 'Deletar',
    '0' : 'Voltar'
}

class ViewConsole:

    def __init__(self):
        self.product_controller = ProductController()
        self.category_controller = CategoryController()
        self.product_category_controller = ProductCategoryController()

    def execute(self):
        self.print_menu()
        choice = self.get_choice_modules()
        self.get_modules(choice)

    def print_menu(self):
        print("="*20, "Bem vindos ao olist !", "="*20)
        print("\tO que você deseja fazer? Selecione uma das opções abaixo:")
        for c,v in modules.items():
            print(f"{c} - {v}")

    def get_choice_modules(self):
        choice = input()
        return choice

    def get_modules(self, choice:str):
        if choice == "0":
            sys.exit(1)
        if choice in modules.keys():
            print(f"{'='*20} Modulo de {modules[choice]} {'='*20}")
            for c,v in crud_option.items():
                print(f"{c} - {v}")
        else:
            print('Digitou errado tatu')