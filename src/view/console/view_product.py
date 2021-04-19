from src.controller.product_controller import ProductController
from src.controller.category_controller import CategoryController


class ViewProduct:


    def __init__(self):
        self.product_controller = ProductController()
        self.category_controller = CategoryController()

    def create(self):
        name = input("Escreva o nome do produto:")
        description = input("Escreva a descrição do produto:")
        price = input("Escreva o preço do produto:")

        categories_id = self.get_categories()
                
        self.product_controller.create(name, description, price, categories_id)


    def read(self):
        products = self.product_controller.read()
        for product in products:
            data = f"{product.id} - {product.name} - {product.description} - {product.price}"
            print(data)
            print("Categorias:")
            for category in product.categories:
                data = f"{category.id} - {category.name} - {category.description}"
                print(data)
            print("\n")

    def read_by_id(self, id):
        product = self.product_controller.read_by_id(id)
        data = f"{product.id} - {product.name} - {product.description} - {product.price}"
        print(data)
        print("\n Categorias:")
        for category in product.categories:
            data = f"{category.id} - {category.name} - {category.description}"
            print(data)
        return product

    def get_categories(self):
        categories_id = []
        while True:
            print("Selecione uma das categorias abaixo:")
            categories = self.category_controller.read()
            for category in categories:
                data = f"{category.id} - {category.name} - {category.description}"
                print(data)
            categories_id.append(input())
            option = input("Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break
        return categories_id

    def update(self):
        self.read()
        product_id = input("Escolha um produto para editar:")
        product = self.read_by_id(product_id)
        product.name = input("Escreva o nome do produto:")
        product.description = input("Escreva a descrição do produto:")
        product.price = input("Escreva o preço do produto:")
        categories_id = self.get_categories()
        self.product_controller.update(product, categories_id)

    def delete(self):
        self.read()
        product_id = input("Escolha o ID do produto que deseja deletar:")
        self.product_controller.delete(product_id)
