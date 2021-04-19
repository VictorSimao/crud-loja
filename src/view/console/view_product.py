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
        print(product)
        for category in selected_categories:
            print(category)
            self.controller_prod_cat.create(product, category)
        return product

    def read(self):
        products = self.controller.read()
        for prod in products:
            data = f"{prod.id} - {prod.name} - {prod.description} - {prod.price} - {prod.categories}"
            print(data)

    def update(self):
        #inputs
        #get by id
        #inputs
        self.controller.update()

    def delete(self):
        self.read()
        product_id = int(input("escolha uma produto que deseja deletar: "))
        self.controller.delete(product_id)