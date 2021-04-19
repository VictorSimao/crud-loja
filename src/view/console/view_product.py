from src.controller.product_controller import ProductController
from src.controller.product_category_controller import ProductCategoryController
from src.controller.category_controller import CategoryController

class ViewProduct:
    def __init__(self):
        self.controller = ProductController()
        self.controller_prod_cat = ProductCategoryController()
        self.controller_cat = CategoryController()

    def create(self):
        name = input("Escreva o nome do produto:")
        description = input("Escreva a descrição do produto:")
        price = input("Escreva o preço do produto:")
        selected_categories = []
        while True:
            print("Selecione uma das categorias abaixo:")
            categories = self.controller_cat.read()
            for cat in categories:
                data = f"{cat.id} - {cat.name} - {cat.description}"
                print(data)
            selected_categories.append(input())
            option = input("Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break

        product = self.controller.create(name, description, price, selected_categories)
        for category in selected_categories:
            print(category)
            self.controller_prod_cat.create(product, category)

    def read(self):
        products = self.controller.read()
        for prod in products:
            prod_cat = self.controller_prod_cat.read(prod.id)
            data = f"{prod.id} - {prod.name} - {prod.description} - {prod.price} - {prod_cat}"
            print(data)

    def update(self):
        self.read()
        product_id = input("Escolha um produto para editar:")
        product = self.controller.read_by_id(product_id)
        product.name = input("Escreva um novo nome para o produto:")
        product.description = input("Escreve uma nova descrição:")
        product.price = input("Digite um novo valor:")
        self.controller.update(product)

    def delete(self):
        self.read()
        product_id = int(input('Escolha um produto que deseja deletar:'))
        self.controller.delete(product_id)