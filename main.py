import sys

from src.category.dao.category_dao import CategoryDAO
from src.product.dao.product_dao import ProductDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao
from src.views import CategoryView, ProductView

class Main:
    def __init__(self):
        self.category_view = CategoryView()
        self.product_view = ProductView()

        self.controller()


    def controller(self):

        CategoryDAO().create_table_category()
        ProductDAO().create_table_product()
        ProductCategoryDao().create_table_product_category()

        while True:
            self.get_user_input()


    def show_menu(self):
        print("""O que você deseja fazer?
        1. Listar os produtos
        2. Cadastrar um produto
        3. Listar as categorias
        4. Cadastrar uma categoria
        5. Sair""")


    def get_user_input(self):
        self.show_menu()
        choice = input("Selecione uma das opções acima:")
        self.get_choice(choice)


    def get_choice(self, choice):
        if choice == "1":
            self.product_view.show_products()
            
        elif choice == "2":
            self.product_view.form_create_product()    
                
        elif choice == "3":
            self.category_view.show_categories()
                
        elif choice == "4":
            self.category_view.form_create_category()
            
        elif choice == "5":
            sys.exit(1)
            
        else:
            print("Opção inválida")
            self.get_user_input()


Main()