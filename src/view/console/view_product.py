from src.controller.product_controller import ProductController
from src.controller.product_category_controller import ProductCategoryController

class ViewProduct:
    def __init__(self):
        self.controller = ProductController()
        self.controller_prod_cat = ProductCategoryController()

    def create(self):
        # create
        self.controller.create()

    def read(self):
        products = self.controller.read()
        for prod in products:
            data = f"{prod.id} - {prod.name} - {prod.description} - {prod.price}"
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