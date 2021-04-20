from src.controller.product_controller import ProductController
from src.controller.product_category_controller import ProductCategoryController


class ViewProduct:
    def __init__(self):
        self.controller = ProductController()
        self.controller_prod_cat = ProductCategoryController()

    def create(self):
        name = input('Escreva o nome do produto: ')
        description = input('Escreva a descrição do produto: ')
        price = input('Informe o valor do produto: ')
        #chamar lista de categorias
        categories = input('Informe a categoria do produto: ')
        self.controller.create(name, description, price, categories)
    
    def read(self):
        produtcs = self.controller.read()
        for prod in produtcs:
            data = f"({prod.id} - {prod.name} - {prod.description} - {prod.price} - {prod.categories})"
            print(data)

    def update(self):
        self.read()
        product_id = input('Escolha um produto para editar: ')
        product = self.controller.read_by_id(product_id)
        data = f"{product.name} - {product.description} - {product.price}"
        print(data)
        product.name = input('Escreva o nome do produto: ')
        product.description = input('Escreva a descrição do produto:')
        product.price = input('Escreva o valor do produto: ')
        product.categories = input('Digite a nova categoria: ')        
        self.controller.update(product)

    def delete(self):
        self.read()
        product_id = int(input('Escolha o produto que deseja deletar: '))
        self.controller.delete(product_id)


        
    
    