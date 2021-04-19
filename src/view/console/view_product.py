from src.controller.product_controller import ProductController
from src.controller.product_category_controller import ProductCategoryController

class View_Product:
    def __init__(self):
        self.controller = ProductController()
        self.controller_prod_cat = ProductCategoryController()

    def create(self):
        name = input("Escreva o nome da produto:")
        description = input("Escreva a descrição do produto:")
        price = input("Escreva o preço do  produto:")
        self.controller.create(name, description, price)

    def read(self):
        products = self.controller.read()
        for prod in products:
            data = f"{prod.id} - {prod.name} - {prod.description} - {prod.price}"
            print(data)

    def update(self):
        self.read()
        product_id = input("Escolha um produto para editar:")
        product = self.controller.read_by_id(product_id)
        data = f"{product.id} - {product.name} - {product.description} - {product.price}"
        print(data)
        product.name = input("Escreva o nome do produto:")
        product.description = input("Escreva a descrição do produto:")
        product.price = input("Escreva o preço do produto:")
        self.controller.update(product)

    def delete(self):
        self.read()
        product_id = int(input('escolha um produto que deseja deletar:'))
        self.controller.delete(product_id)