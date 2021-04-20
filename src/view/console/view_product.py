from src.controller.product_controller import ProductController
from src.controller.product_category_controller import ProductCategoryController
from src.controller.category_controller import CategoryController

class ViewProduct:
    def __init__(self):
        self.controller = ProductController()
        self.controller_prod_cat = ProductCategoryController()
        self.controller_category = CategoryController()

    def create(self):
        product = ''
        name = input("Escreva o nome do Produto:")
        description = input("Escreva a descrição :")
        price = float(input('Preço (Exemplo esperado: 1.00): '))
        selected_categories = []
        while True:
            print('\nCategorias: ')
            categories = self.controller_category.read()
            for cat in categories:
                data = f"{cat.id} - {cat.name} - {cat.description}"
                print(data)
            selected_categories.append(input("Informe o código de uma categoria: "))
            option = input("Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break
        print(selected_categories)
        product = self.controller.create(name, description, price, categories)
        for category in selected_categories:
            self.controller_prod_cat.create(product, category)
        return product

    def read(self):
        products = self.controller.read()
        categories = ''
        for prod in products:
            categories = self.controller.read_categories_by_id(prod.id)
            data = f"{prod.id} - {prod.name} - {prod.description} - {prod.price} - {categories}"
            print(data)

    def update(self):
        self.read()
        product_id = input('\nInforme o código do produto que você deseja alterar: ')
        product = self.controller.read_by_id(product_id)
        data = f"{product.id} - {product.name} - {product.description} - {product.price}"
        print(data)
        product.name = input("Novo nome: ")
        product.description = input("Nova descrição: ")
        product.price = input("Novo preço: ")
        print(product)
        self.controller.update(product)

    def delete(self):
        self.read()
        product_id = int(input("escolha uma produto que deseja deletar: "))
        self.controller.delete(product_id)