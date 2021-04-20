from src.controller.product_controller import ProductController
from src.controller.product_category_controller import ProductCategoryController
from src.view.console.view_category import ViewCategory

class ViewProduct:
    def __init__(self):
        self.controller = ProductController()
        self.controller_prod_cat = ProductCategoryController()
        self.category = ViewCategory()

    def create(self):
        name = input("Escreva o nome do produto:")
        description = input("Escreva a descrição do produto:")
        price = input("Escreva o preço do produto:")


        categories = []
        while True:
            print("Escolha uma das categorias abaixo: ")
            self.category.read()
            categories.append(input())
            option = input("Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                    continue
            else:
                break

        self.controller.create(name, description, price, categories)


        product = self.controller.create(name, description, price, categories)
        for category in categories:
            print(category)
            self.controller_prod_cat.create(product, category)


    def read(self):
        products = self.controller.read()
        for prod in products:
            data = f"{prod.id} - {prod.name} - {prod.description} - {prod.price} - {prod.categories}"
            print(data)

    def update(self):
        self.read()
        product_id = input("Escolha um produto para editar: ")
        product = self.controller.read_by_id(product_id)
        data = f"{product.id} - {product.name} - {product.description} - {product.price}"
        print(data)
        product.name = input("Escreva o novo nome: ")
        product.description = input("Escreva a nova descrição: ")
        product.price = float(input("Digite o novo valor: "))
        self.controller.update(product)


    def delete(self):
        self.read()
        product_id = int(input('Escolha o produto que deseja deletar: '))
        self.controller.delete(product_id)