from src.product_category.dao.product_category_dao import ProductCategoryDao
from typing import NoReturn


class ProductCategoryController:
    def __init__(self):
        self.product_category_dao = ProductCategoryDao()

    def create_prod_cat(self, product_id: int) -> NoReturn:
        selected_categories = []
        while True:
            print("Selecione uma das categorias acima:")
            selected_categories.append(input('Id: '))
            option = input(
                "Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break
        for selected_category in selected_categories:
            try:
                self.product_category_dao.create(product_id, selected_category)
            except:
                pass

    def update_prod_cat(self, product_id: int):
        id = int(product_id)
        self.product_category_dao.delete((id,))
        self.product_category_dao.create_prod_cat(product_id)

    def delete_prod_cat(self, id: int):
        self.product_category_dao.delete((id,))
