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
        categories = []
        while True:
            print("Selecione uma das categorias abaixo:")
            categories = self.controller_cat.read()
            for cat in categories:
                data = f"{cat.id} - {cat.name} - {cat.description}"
                print(data)
            categories.append(input())
            option = input("Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break
            print(categories)

        product = self.controller.create(name, description, price, categories)
        for category in categories:
            self.controller_prod_cat.create(product, category.id)

    def read(self):
        products = self.controller.read()
        for prod in products:
            data = f"{prod.id} - {prod.name} - {prod.description} - {prod.price}"
            print(data)

    def update(self):
        #inputs
        #get by id
        #inputs
        self.controller.update()

    def delete(self):
        #inputs
        self.controller.delete()