from src.product_category.dao.product_category_dao import ProductCategoryDao
from typing import NoReturn


class ProductCategoryController(ProductCategoryDao):
    def create_controller(self, product_id, selected_categories) -> NoReturn:
        for selected_category in selected_categories:
            self.create(product_id, int(selected_category))
