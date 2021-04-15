from ..model.category_model import Category
from ..dao.category_dao import CategoryDAO
from typing import NoReturn


class CategoryController(CategoryDAO):
    def create_controller(self):
        return self.create(Category(input('Nome: '), input('Descrição: ')))

    def read_controller(self) -> NoReturn:
        categories = self.read_all()
        print("\n\n=============== Categorias =================")
        print("ID - NOME - DESCRIÇÃO")
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)

    def update_controller(self) -> NoReturn:
        return self.update(Category(input('Nome: '), input('Descrição: '), input('Id: ')))

    def delete_controller(self):
        print('Qual categoria desejar deletar: ')
        return self.delete((input(),))
