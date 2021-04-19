from ..model.category_model import Category
from ..dao.category_dao import CategoryDAO
from typing import NoReturn


class CategoryController:
    def __init__(self):
        self.category_dao = CategoryDAO()

    def create_category(self):
        return self.category_dao.create(Category(input('Nome: '), input('Descrição: ')))

    def read_category(self) -> NoReturn:
        categories = self.category_dao.read_all()
        print("\n\n=============== Categorias =================")
        print("ID - NOME - DESCRIÇÃO")
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)

    def update_category(self) -> NoReturn:
        return self.category_dao.update(Category(input('Nome: '), input('Descrição: '), input('Id: ')))

    def delete_category(self):
        print('Qual categoria desejar deletar: ')
        return self.category_dao.delete((input(),))
