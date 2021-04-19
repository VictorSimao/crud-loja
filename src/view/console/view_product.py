from src.controller.product_controller import ProductController
from src.controller.product_category_controller import ProductCategoryController
from src.controller.category_controller import CategoryController


class View_Product:
    def __init__(self):
        self.controller = ProductController()
        self.controller_prod_cat = ProductCategoryController()
        self.category_controller = CategoryController()

    def selected_categories(self):
        selected_categories = []
        while True:
            print("Selecione uma das categorias abaixo: ")
            categories = self.category_controller.read()
            for cat in categories:
                data = f"{cat.id} - {cat.name} - {cat.description}"
                print(data)
            selected_categories.append(input())
            option = input("Você deseja cadastrar mais uma categoria? (s/N): ")
            if option == "s":
                continue
            else:
                break
        return selected_categories

    def create(self):
        # inputs
        name = input("Escreva o nome do produto:")
        description = input("Escreva a descrição do produto:")
        price = float(input("Escreva o preço do produto: "))
        product = self.controller.create(name, description, price)
        selected_categories = self.selected_categories()
        for selected_category in selected_categories:
            self.controller_prod_cat.create(
                category_id=int(selected_category), product_id=product
            )


    def read(self):
        [print(product) for product in self.controller.read()]
        # return list

    def update(self):
        self.read()
        product_id = input("Selecione um produto que deseja alterar: ")
        product = self.controller.read_by_id(product_id)
        data = f"{product.id} - {product.name} - {product.description} - {product.price}"
        print(data)
        product.name = input("Escreva o nome do produto:")
        product.description = input("Escreva a descrição do produto:")
        product.price = float(input("Escreva o preço do produto: "))
        self.controller.update(product)

    def delete(self):
        self.read()
        product_id = int(input("Selecione o produto que deseja excluir: "))
        self.controller.delete(product_id)
