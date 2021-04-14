import sys

from src.category.dao.category_dao import CategoryDAO
from src.product.dao.product_dao import ProductDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao
from src.category.model.category_model import Category
from src.product.model.product_model import Product

class Main:
    def __init__(self):
        self.category_dao = CategoryDAO()
        self.product_dao = ProductDAO()
        self.product_id = 0
        self.category_id = 0
        self.product_category_dao = ProductCategoryDao()
        self.controller()


    def controller(self):

        # self.category_dao.create_table_category()
        # self.product_dao.create_table_product()
        # self.product_category_dao.create_table_product_category()

        while True:
            self.get_user_input()
        # category = Category('categoryName','cate')
        # categories = [category]
        # print(category.name, type(category.name))
        # last_category = self.category_dao.insert_data_category(category)
        
        # self.product_category.insert_data_product_category(last_product,last_category)


    def get_user_input(self):
        print("""
        ---------------------------------
        Selecione uma das opções abaixo:
        ---------------------------------
        * PRODUTOS
        ---------------------------------
        1. Listar todos
        2. Cadastrar
        3. Excluir
        4. Editar
        ---------------------------------
        * CATEGORIAS
        ---------------------------------
        5. Listar todas
        6. Cadastrar
        7. Excluir
        8. Editar
        ---------------------------------
        * SISTEMA
        ---------------------------------
        9. Encerrar o sistema
        ---------------------------------
        Opção desejada: 
        """)
        choice = input()
        self.get_choice(choice)

    def get_choice(self, choice):

        if choice == "1":
            # self.product_dao.select_all_data_product()
            products = self.product_dao.read_all()
            for prod in products:
                data = f"{prod.id} - Produto: {prod.name} - Desc: {prod.description} - Preço: {prod.price} - Categorias: {prod.categories}"
                print(data)

        elif choice == "2":
            product_name = input("Escreva o nome do produto:")
            product_description = input("Escreva a descrição do produto:")
            product_price = input("Escreva o preço do produto:")
            selected_categories = []
            while True:
                categories = self.category_dao.read_all()
                for cat in categories:
                    data = f"{cat.id} - {cat.name} - {cat.description}"
                    print(data)
                print("Selecione uma das categorias abaixo:")
                selected_categories.append(input())
                option = input("Você deseja cadastrar mais uma categoria? (s/N)")
                if option == "s":
                    continue
                else:
                    break
                print(selected_categories)
            product = Product(product_name, product_description, product_price, selected_categories)
            self.product_id = self.product_dao.create(product)
            for selected_category in selected_categories:
                self.product_category_dao.create(self.product_id, selected_category)

        elif choice == "3":
            id_product = int(input("Código do produto para exclusão: "))
            self.product_dao.delete(id_product)

        elif choice == "4":
            return ''
            # editar produto
        
        elif choice == "5":
            categories = self.category_dao.read_all()
            for cat in categories:
                data = f"{cat.id} - {cat.name} - {cat.description}"
                print(data)

        elif choice == "6":
            category_name = input("Escreva o nome da categoria:")
            category_description = input("Escreva a descrição da categoria:")
            category = Category(category_name, category_description)
            self.category_id = self.category_dao.create(category)

        elif choice == "7":
            return ''
            # excluir categoria

        elif choice == "8":
            return ''
            # editar categoria

        elif choice == "9":
            sys.exit(1)
        else:
            print("Opção inválida")
            self.get_user_input()


Main()