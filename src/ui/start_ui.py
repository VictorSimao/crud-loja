import sys
from src.ui.product_ui import ProductInput
from src.ui.category_ui import CategoryInput

class StartInput:
    
    def __init__(self):
        self.product_ui = ProductInput()
        self.category_ui = CategoryInput()

    def get_user_input(self):
        print("""\n O que você deseja fazer? Selecione uma das opções abaixo:
        1. Listar os produtos
        2. Cadastrar um produto
        3. Editar um produto
        4. Excluir um produto
        5. Listar as categorias
        6. Cadastrar uma categoria
        7. Editar uma categoria
        8. Excluir uma categoria
        9. Sair""")
        choice = input()
        self.get_choice(choice)

    def get_choice(self, choice):
        if choice == "1":
            self.product_ui.list_products()
        elif choice == "2":
            self.product_ui.create_product()
        elif choice == "3":
            pass
        elif choice == "4":
            self.product_ui.delete_product()
        elif choice == "5":
            self.category_ui.list_categories()
        elif choice == "6":
            self.category_ui.create_category()
        elif choice == "7":
            pass
        elif choice == "8":
            self.category_ui.delete_category()
        elif choice == "9":
            sys.exit(1)
        else:
            print("Opção inválida")
            self.get_user_input()