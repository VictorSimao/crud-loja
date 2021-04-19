from src.controller.category_controller import CategoryController
from src.controller.product_controller import ProductController
from src.controller.product_category_controller import ProductCategoryController


class ViewProduct:
    def __init__(self):
        self.controller = ProductController()
        self.controller_prod_cat = ProductCategoryController()
        self.controller_category = CategoryController()

    def create(self):
        name = input("Escreva o nome do produto: ")
        description = input("Escreva a descrição do produto: ")
        price = input("Escreva o preço do produto: ")
        self.controller.create(name, description, price)

    def read(self):
        products = self.controller.read()
        for product in products:
            list_categories_by_product_id = self.controller_prod_cat.read_by_product_id(product.id)
            product.categories = [self.controller_category.read_by_id(prod_cat.category_id).name for prod_cat in list_categories_by_product_id]
            data = f"{product.id} - {product.name} - {product.description} - {product.price} - {product.categories}"
            print(data)

    def update(self):
        self.read()
        product_id = input("Escolha um produto para editar:")
        product = self.controller.read_by_id(product_id)
        data = f"{product.id} - {product.name} - {product.description} - {product.price} - {product.categories}"
        print(data)
        product.name = input("Escreva o nome do produto: ")
        product.description = input("Escreva a descrição do produto: ")
        product.price = input("Escreva o preço do produto: ")
        self.controller.update(product)

    def delete(self):
        self.read()
        product_id = input("Escolha um produto para deletar:")
        self.controller.delete(product_id)
