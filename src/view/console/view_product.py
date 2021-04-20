from src.dao.category_dao import CategoryDAO
from src.controller.product_controller import ProductController
from src.controller.product_category_controller import ProductCategoryController


class ViewProduct:

    def __init__(self):
        self.controller = ProductController()
        self.controller_prod_cat = ProductCategoryController()
        self.category_dao = CategoryDAO()

    def __get_all_categories(self):
        categories = self.category_dao.read_all()
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)

    def __typed_categories(self):
        select_categories = []
        while True:
            print('Categorias: ')
            self.__get_all_categories()

            select_categories.append(
                input('Selecione uma das categorias listada: '))

            option = input('Gostaria de cadastrar uma nova categoria? (s/n)')
            if option == 's':
                continue

            break

        return select_categories

    def create(self):
        name = input("Escreva o nome do produto: ")
        description = input("Escreva a descrição do produto: ")
        price = input("Escreva o preço do produto: ")

        select_categories = self.__typed_categories()
        product = self.controller.create(name, description, price,
                                         select_categories)

        for selected in select_categories:
            self.controller_prod_cat.create(product, selected)

    def read(self):
        products = self.controller.read()
        prod_categories = self.controller_prod_cat.read()

        for pro in products:
            data = f"{pro.id} - {pro.name} - {pro.description}" \
                   f"  - {pro.price} - Categorias: {pro.categories}"
            print(data)
        return prod_categories
 
    def update(self):
        self.read()
        product_id = input('Selecione um produto que deseja alterar: ')
        name = input("Escreva o nome da categoria:")
        description = input("Escreva a descrição da categoria:")
        price = input('EScreva o novo preco')
        self.controller.update(product_id, name, description, price)

    def delete(self):
        self.read()
        id_product = int(input("Informe o produto que deseja deletar ?"))
        self.controller.delete(id_product)
        print(f'Produto com id {id_product} deletado ')
