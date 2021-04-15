from time import sleep
from typing import NoReturn, List
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

    def controller(self) -> NoReturn:

        self.category_dao.create_table_category()
        self.product_dao.create_table_product()
        self.product_category_dao.create_table_product_category()

        while True:
            self.main_menu()

    def main_menu(self) -> NoReturn:
        print("""
            Seja Bem Vindo ao menu de registro produtos !!!


            Selecione a opção desejada:

            1 - Menu de Produtos
            2 - Menu de Categorias
            3 - Sair 
        """)
        choice = input()
        if choice == '1':
            self.menu_product()
        elif choice == '2':
            self.menu_category()
        self.exit_menu(choice=choice, callback=self.main_menu)

    def menu_category(self) -> NoReturn:
        print("""O que você deseja fazer? Selecione uma das opções abaixo:
        1. Listar as categorias
        2. Cadastrar uma categoria
        3. Sair""")
        choice = input()
        self.main_menu_category(choice=choice)

    def menu_product(self) -> NoReturn:
        print("""O que você deseja fazer? Selecione uma das opções abaixo:
        1. Listar os produtos
        2. Cadastrar um produto
        3. Sair""")
        choice = input()
        self.main_menu_product(choice=choice)

    def show_categories(self) -> str:
        categories = self.category_dao.read_all()
        return [print(f"{cat.id} - {cat.name} - {cat.description}") for cat in categories]

    def menu_register_product(self) -> List:
        selected_categories = []
        print("Selecione uma das categorias abaixo:")
        self.show_categories()
        selected_categories.append(int(input()))
        option = input("Você deseja cadastrar mais uma categoria? (s/N): ")
        if option == "s":
            self.menu_register_product()
        return selected_categories

    def main_menu_category(self, choice) -> NoReturn:
        if choice == "1":
            self.show_categories()
        elif choice == "2":
            category_name = input("Escreva o nome da categoria:")
            category_description = input("Escreva a descrição da categoria:")
            category = Category(category_name, category_description)
            self.category_id = self.category_dao.create(category)
        self.exit_menu(choice=choice, callback=self.menu_category)

    def exit_menu(self, choice, callback) -> NoReturn:
        if choice == "3":
            sys.exit(1)
        elif int(choice) > 3 or type(int(choice)) != int:
            print("Opção inválida")
            sleep(2)
            callback()

    def show_products(self) -> str:
        products = self.product_dao.read_all()
        return [print(f"{product.id} - {product.name} - {product.description} - {product.price} - {product.categories}") for product in products]

    def register_product(self) -> NoReturn:
        product_name = input("Escreva o nome do produto:")
        product_description = input("Escreva a descrição do produto:")
        product_price = input("Escreva o preço do produto:")
        selected_categories = self.menu_register_product()
        categories = self.category_dao.read_by_id(selected_categories)
        product = Product(product_name, product_description,
                          product_price, categories)
        self.product_id = self.product_dao.update(product)
        for selected_category in selected_categories:
            self.product_category_dao.update(
                self.product_id, selected_category)

    def main_menu_product(self, choice) -> NoReturn:
        if choice == "1":
            self.show_products()
        elif choice == "2":
            product_name = input("Escreva o nome do produto:")
            product_description = input("Escreva a descrição do produto:")
            product_price = input("Escreva o preço do produto:")
            selected_categories = self.menu_register_product()
            categories = self.category_dao.read_by_id(selected_categories)
            product = Product(product_name, product_description,
                              product_price, categories)
            self.product_id = self.product_dao.create(product)
            for selected_category in selected_categories:
                self.product_category_dao.create(
                    self.product_id, selected_category)
        elif choice == '3':
            print("""
                Selecione o produto que deseja excluir !!
            """)
            self.show_products()
            product_id = input()
            self.product_dao.delete(product_id=product_id)
        elif choice == '4':
            print("""
                Selecione o Produuto que deseja atualizar !!
            """)
            self.show_products()
            product_id = input()
            product = self.product_dao.read_by_id(product_id=product_id)
            product.name = input
            self.product_dao.update(product)
        self.exit_menu(choice, callback=self.menu_product)


Main()
