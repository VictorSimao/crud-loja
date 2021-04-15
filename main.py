import sys

from src.views import CategoryView, ProductView
from settings import init_bd

class Main:
    def __init__(self):
        self.category_view = CategoryView()
        self.product_view = ProductView()


    def run(self):
        while True:
            self._show_menu()
            choice = input("Selecione uma das opções acima:")
            self._get_choice(choice)
            

    def _show_menu(self):
        print("""O que você deseja fazer?
        1. Listar os produtos
        2. Cadastrar um produto
        3. Atualizar um produto
        4. Remover um produto
        5. Listar as categorias
        6. Cadastrar uma categoria
        7. Sair""")


    def _get_choice(self, choice: int):
        if choice == "1":
            self.product_view.show_products()
            
        elif choice == "2":
            self.product_view.form_create_product()    
                
        elif choice == "3":
            self.product_view.form_update_product()

        elif choice == "4":
            self.product_view.form_delete_product()

        elif choice == "5":
            self.category_view.show_categories()
                
        elif choice == "6":
            self.category_view.form_create_category()
            
        elif choice == "7":
            sys.exit(1)
            
        else:
            print("Opção inválida")
            self.get_user_input()


if __name__ == '__main__':
    init_bd()
    stage = Main()
    stage.run()
    