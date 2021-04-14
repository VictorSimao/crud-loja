from src.category.dao.category_dao import CategoryDAO
from src.product.dao.product_dao import ProductDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao
from src.ui.start_ui import StartInput

class Main:
    def __init__(self):
        self.start_ui = StartInput()
        self.category_dao = CategoryDAO()
        self.product_dao = ProductDAO()
        self.product_category_dao = ProductCategoryDao()
        self.controller()

    def controller(self):

        # create db if they don't exist
        self.category_dao.create_table_category()
        self.product_dao.create_table_product()
        self.product_category_dao.create_table_product_category()

        while True:
            self.start_ui.get_user_input()

Main()