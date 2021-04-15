import sys

from src.category.dao.category_dao import CategoryDAO
from src.product.dao.product_dao import ProductDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao
from src.category.model.category_model import Category
from src.product.model.product_model import Product


class CategoryView():
    def __init__(self):
        self.category_dao = CategoryDAO()
        
        
    def show_categories(self):
        categories = self.category_dao.read_all()
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)
            

    def form_category(self):
        category_name = input("Escreva o nome da categoria:")
        category_description = input("Escreva a descrição da categoria:")
        category = Category(category_name, category_description)
        self.category_dao.create(category)
        
        
class ProductView():
    def __init__(self):
        self.product_dao = ProductDAO()
        self.product_category_dao = ProductCategoryDao()        
        
        
    def show_products(self):
        products_bd = self.product_dao.read_all()
        for prod in products_bd:
            data = f"{prod.id} - {prod.name} - {prod.description} - {prod.price} - Categorias: {prod.categories}" 
            print(data)
            
            
    def get_typed_categories(self):
        selected_categories = []
        while True:
            print("Categorias:")
            self.show_categories()
                
            selected_categories.append(input("Selecione uma das categorias acima: "))
            
            option = input("Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break
        
        return selected_categories

class Main:
    def __init__(self):
        # self.category_dao = CategoryDAO()
        self.product_dao = ProductDAO()
        self.product_category_dao = ProductCategoryDao()
        
        self.category_view = CategoryView()
        self.product_view = ProductView()

        self.controller()


    def controller(self):

        CategoryDAO().create_table_category()
        self.product_dao.create_table_product()
        self.product_category_dao.create_table_product_category()

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
            product_name = input("Escreva o nome do produto:")
            product_description = input("Escreva a descrição do produto:")
            product_price = input("Escreva o preço do produto:")
            
            selected_categories = self.product_view.get_typed_categories()
            product = Product(product_name, product_description, product_price, selected_categories)
            
            product_id = self.product_dao.create(product)
            
            for selected_category in selected_categories:
                self.product_category_dao.create(product_id, selected_category)
                
                
        elif choice == "3":
            self.category_view.show_categories()
                
                
        elif choice == "4":
            self.category_view.form_category()
            
            
        elif choice == "5":
            sys.exit(1)
            
            
        else:
            print("Opção inválida")
            self.get_user_input()


Main()