from src.dao.category_dao import CategoryDAO
from src.dao.product_dao import Product
from src.controller.product_controller import ProductController
from src.controller.product_category_controller import ProductCategoryController


class ViewProduct:
    def __init__(self):
        self.controller = ProductController()
        self.controller_prod_cat = ProductCategoryController()
        self.category_dao = CategoryDAO()

    def get_all_categories(self):
        categories = self.category_dao.read_all()
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)

    def get_all_products(self):
        products = self.product_dao.read_all()
        for pro in products:
            data = f"{pro.id} - {pro.name} - {pro.description}" \
                   f"  - {pro.price} - Categorias: {pro.categories}"
            print(data)

    def typed_categories(self):
        select_categories = []
        while True:
            print('Categorias: ')
            self.get_all_categories()

            select_categories.append(
                input('Selecione uma das categorias listada: '))

            option = input('Gostaria de cadastrar uma nova categoria? (s/n)')
            if option == 's':
                continue

            break

        return select_categories

    def create(self):
        name = input("Escreva o nome do produto: ")
        description = input("Escreva a descrição do produto: ")
        price = input("Escreva o preço do produto: ")         
        select_categories = self.typed_categories()

        product = self.controller.create(name, description, price,
                                         select_categories)

        for selected in select_categories:
            self.controller_prod_cat.create(product, selected)

    def read(self):
        products = self.controller.read()
        prod_categories = self.controller_prod_cat.read()

        for pro in products:
            data = f"{pro.id} - {pro.name} - {pro.description}" \
                   f"  - {pro.price} - Categorias: {pro.categories}"
            print(data)
        return prod_categories
        
    def update(self):
        # inputs
        # get by id
        # inputs
        self.controller.update()

    def delete(self):
        #inputs
        self.controller.delete()