from src.controller.product_controller import ProductController
from src.controller.product_category_controller import ProductCategoryController
from src.controller.category_controller import CategoryController
from src.model.product_model import Product


class ViewProduct:
    def __init__(self):
        self.controller = ProductController()
        self.controller_prod_cat = ProductCategoryController()
        self.controller_category = CategoryController()

    def create(self):
        name = str(input("Escreva o nome do produto:"))
        description = str(input("Escreva a descrição do produto:"))
        price = float(input("Escreva o preço do produto:"))
        selected_category = []
        while True:
            print("Selecione uma das categorias abaixo")
            categories = self.controller_category.read()
            for cat in categories:
                data = f"{cat.id} - {cat.name} - {cat.description}"
                print(data)
            selected_category.append(input("Digite o número da categoria:"))
            option = input("Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break
        product = self.controller.create(name, description, price, categories)
        for categories in selected_category:
            print(categories)
            self.controller_prod_cat.create(product, categories)

    def read(self):
        products = self.controller.read()
        for prod in products:
            data = f"{prod.id} - {prod.name} - {prod.description} - {prod.price} - {prod.categories}"
            print(data)

    def update(self):
        self.read()
        product_id = int(input("Escolha qual produto deseja alterar:"))
        product = self.controller.read_by_id(product_id)
        data = f"{product.id} - {product.name} - {product.description} - {product.price}"
        print(data)
        product.name = str(input("Escreva o nome do produto:"))
        product.description = str(input("Escreva a descrição do produto:"))
        product.price = float(input("Escreva o preço do produto:"))
        self.controller.update(product)

    def delete(self):
        self.read()
        product_id = int(input("Escolha qual produto deseja deletar: "))
        self.controller.delete(product_id)
