from src.controller.category_controller import CategoryController


class View_Category:
    def __init__(self):
        self.controller = CategoryController()

    def create(self):
        name = input("Escreva o nome da categoria:")
        description = input("Escreva a descrição da categoria:")
        self.controller.create(name, description)

    def read(self):
        categories = self.controller.read()
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)

    def update(self):
        self.read()
        category_id = input("Escolha uma categoria para editar:")
        category = self.controller.read_by_id(category_id)
        data = f"{category.id} - {category.name} - {category.description}"
        print(data)
        category.name = input("Escreva o nome da categoria:")
        category.description = input("Escreva a descrição da categoria:")
        self.controller.update(category)

    def delete(self):
        self.read()
        category_id = int(input('escolha uma categoria que deseja deletar:'))
        self.controller.delete(category_id)