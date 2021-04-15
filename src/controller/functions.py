import sys
from src.category.dao.category_dao import CategoryDAO
from src.product.dao.product_dao import ProductDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao
from src.category.model.category_model import Category
from src.product.model.product_model import Product


# Need refactor functions of category and functions of product.
class Functions():


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
    

    def show_options(self):
        print("""O que você deseja fazer? Selecione uma das opções abaixo:
            A. Listar os produtos
            B. Cadastrar um produto
            C. Editar um produto
            D. Deletar um produto

            E. Listar as categorias
            F. Cadastrar uma categoria
            G. Editar uma categoria
            H. Deletar uma categoria

            I. Fechar o programa""")
        choice = input()
        return choice


    def show_all_products(self):
        """Show on console all products register in database"""
        products = self.product_dao.read_all()
        for pro in products:
            data = f"{pro.id} - {pro.name} - {pro.description} - {pro.price} "
            print(data)
    

    def create_product(self):
        product_name = input("Escreva o nome do produto:")
        product_description = input("Escreva a descrição do produto:")
        product_price = input("Escreva o preço do produto:")
        selected_categories = []
        while True:
            print("Selecione uma das categorias abaixo:")

            categories = self.category_dao.read_all()
            for cat in categories:
                data = f"{cat.id} - {cat.name} - {cat.description}"
                print(data)


            selected_categories.append(input())
            option = input(" Você deseja cadastrar mais uma categoria? (s/N) ")
            
            
            if option == "s":
                continue
            else:
                break

        product = Product(product_name, product_description, 
                          product_price, selected_categories)
        
        
        self.product_id = self.product_dao.create(product)
        for selected_category in selected_categories:
            self.product_category_dao.create(self.product_id, selected_category)

        
    def edit_product(self):
        pass     


    def delete_product(self):
        print("Produtos: ")

        products = self.product_dao.read_all()
        for pro in products:
            data = f"{pro.id} - {pro.name} - {pro.description} - {pro.price}"
            print(data)
        
        option = input("Qual produto você quer deletar? ")

        self.product_dao.delete(option)
    

    def show_all_categories(self):
        categories = self.category_dao.read_all()
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)


    def create_category(self):
        category_name = input("Escreva o nome da categoria:")
        category_description = input("Escreva a descrição da categoria:")
        category = Category(category_name, category_description)
        self.category_id = self.category_dao.create(category)


    def edit_category(self):
        pass


    def delete_category(self):
        print("Categorias: ")
            
        categories = self.category_dao.read_all()
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)
            
        option = input("Qual categoria você quer deletar? ")
        
        self.category_dao.delete(option)      

    

    
