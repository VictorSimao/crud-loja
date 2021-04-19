from src.controller.product_controller import ProductController
from src.controller.product_category_controller import ProductCategoryController
from src.controller.category_controller import CategoryController

from src.model.product_model import Product

class ViewProduct:
    def __init__(self):
        self.controller = ProductController()
        self.controller_category = CategoryController()
        self.controller_prod_cat = ProductCategoryController()

    def __get_selected_categories(self):
        selected_categories = []

        while True:
            print("Selecione uma das categorias abaixo:")
            categories = self.controller_category.read()
            for cat in categories:
                data = f"{cat.id} - {cat.name} - {cat.description}"
                print(data)
            selected_categories.append(input())
            
            option = input("Você deseja cadastrar mais uma categoria? (s/N)")
            
            if option == "s":
                continue
            else:
                break
        
        return selected_categories

    def create(self):
        product_name = input("Escreva o nome do produto:")
        product_description = input("Escreva a descrição do produto:")
        product_price = input("Escreva o preço do produto:")
        selected_categories = self.__get_selected_categories()
        
        self.controller.create(product_name, product_description, product_price, selected_categories)

    def read(self):
        products = self.controller.read()
        
        for prod in products:
            products_categories = self.controller_prod_cat.read_by_id(prod.id)
            list_categories = []
            
            for prod_cat in products_categories:
                category = self.controller_category.read_by_id(prod_cat.category_id)
                list_categories.append(category)
                
            prod.categories = list_categories
            print(prod)

    def update(self):
        # inputs
        # get by id
        # inputs
        self.controller.update()

    def delete(self):
        self.read()
        id = input("Informe o id do produto que deseja deletar?")
        self.controller.delete(id)
