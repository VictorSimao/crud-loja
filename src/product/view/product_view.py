from src.category.controller.category_controller import CategoryController
from src.product.controller.product_controller import ProductController
from src.category.model.category_model import Category
from src.product.model.product_model import Product

class ProductView:
    

    def __init__(self):
        self.product_controller = ProductController()
        self.category_controller = CategoryController()

    def list_products(self):
        products = self.product_controller.get_products()
        for prod in products:
            prod_data = f"{prod.id} - {prod.name} - {prod.description} - {prod.price}"
            print(prod_data)
            print("Categorias:")
            for prod_cat in prod.categories:
                prod_cat_data = f"          {prod_cat.id} - {prod_cat.name} - {prod_cat.description}"
                print(prod_cat_data)
            print("\n")   

    def create_product(self):
        product_name = input("Escreva o nome do produto:")
        product_description = input("Escreva a descrição do produto:")
        product_price = input("Escreva o preço do produto:")
        selected_categories = []
        while True:
            print("Selecione uma das categorias abaixo:")
            choice_categories = self.category_controller.get_categories()
            for cat in choice_categories:
                data = f"{cat.id} - {cat.name} - {cat.description}"
                print(data)
            selected_categories.append(input())
            option = input("Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break
            print(selected_categories)
        product = Product(product_name, product_description, product_price)
        product_id = self.product_controller.create_product(product, selected_categories)

    def update_product(self):
        self.list_products()
        product_id = input("Escolha o ID do produto que deseja alterar:")
        product_name = input("Escreva o novo nome do produto:")
        product_description = input("Escreva a nova descrição do produto:")
        product_price = input("Escreva o novo preço do produto:")
        selected_categories = []
        while True:
            print("Selecione uma das categorias abaixo:")
            choice_categories = self.category_controller.get_categories()
            for cat in choice_categories:
                data = f"{cat.id} - {cat.name} - {cat.description}"
                print(data)
            selected_categories.append(input())
            option = input("Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break
            print(selected_categories)
        product = Product(product_name, product_description, product_price, [], product_id)
        self.product_controller.update_product(product, selected_categories)

    def delete_product(self):
        self.list_products()
        product_id = input("Escolha o ID do produto que deseja deletar:")
        self.product_controller.delete_product(product_id)