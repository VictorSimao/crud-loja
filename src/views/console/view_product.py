from src.controller.product_controller import ProductController

class ViewProduct:

    def __init__(self):
        self.controller = ProductController()

    def create(self):
        #inputs
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
        #inputs
        self.controller.delete()

    def read_categories(self):
        categories = self.controller.read_categories()
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)