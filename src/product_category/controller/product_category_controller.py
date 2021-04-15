from src.product_category.dao.product_category_dao import ProductCategoryDao
from typing import NoReturn


class ProductCategoryController(ProductCategoryDao):
    def create_controller(self, product_id: int) -> NoReturn:
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
                self.create(product_id, selected_category)
            except:
                pass

    def update_controller(self, product_id: int):
        id = int(product_id)
        self.delete((id,))
        self.create_controller(product_id)

    def delete_controller(self, id: int):
        self.delete((id,))
