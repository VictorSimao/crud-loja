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
        #inputs
        #get by id
        #inputs
        self.controller.update()

    def delete(self):
        #inputs
        self.controller.delete()