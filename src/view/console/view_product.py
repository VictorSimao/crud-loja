from src.controller.product_controller import ProductController
from src.controller.product_category_controller import ProductCategoryController


class ViewProduct:
    def __init__(self):
        self.controller = ProductController()
        self.controller_prod_cat = ProductCategoryController()

    def create(self):
        product_name = input("Escreva o nome do produto:")
        product_description = input("Escreva a descrição do produto:")
        product_price = input("Escreva o preço do produto:")
        selected_categories = []
        while True:
            print("Selecione uma das categorias abaixo:")
            categories = self.category_dao.read_all()
            for cat in categories:
                data = f"{cat.id} - {cat.name} - {cat.description}"
                print(data)
            selected_categories.append(input())
            option = input("Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break
            print(selected_categories)

        product = Product(product_name, product_description, product_price, selected_categories)
        self.product_id = self.product_dao.create_product(product)
        for selected_category in selected_categories:
            self.product_category_dao.insert_data_product_category(self.product_id, selected_category)

        self.controller.create()

    def read(self):
        products = self.controller.read()
        
        for prod in products:
            products_categories = self.product_category_dao.read_categories_by_product_id(prod.id,)
            list_categories = []
            for prod_cat in products_categories:
                category = self.category_dao.read_by_id(prod_cat.category_id)
                list_categories.append(category)
            prod.categories = list_categories
            print(prod)

    def update(self):
        # inputs
        # get by id
        # inputs
        self.controller.update()

    def delete(self):
        # inputs
        self.controller.delete()
