from src.controller.product_controller import ProductController
from src.controller.product_category_controller import ProductCategoryController

class ViewProduct:
    def __init__(self):
        self.controller = ProductController()
        self.controller_prod_cat = ProductCategoryController()

    def create(self):
        #inputs
        self.controller.create()

    def read(self):
        self.controller.read()
        #return list

    def update(self):
        #inputs
        #get by id
        #inputs
        self.controller.update()

    def delete(self):
        #inputs
        self.controller.delete()
        