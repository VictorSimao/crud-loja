from ..model.category_model import Category
from ..dao.category_dao import CategoryDAO
from typing import NoReturn


class CategoryController(CategoryDAO):
    def create_controller(self) -> NoReturn:
        return self.create(Category(input('Nome: '), input('Descrição: ')))

    def read_controller(self) -> NoReturn:
        categories = self.read_all()
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)
