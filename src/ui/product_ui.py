from src.category.dao.category_dao import CategoryDAO
from src.product.dao.product_dao import ProductDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao
from src.product.model.product_model import Product

class ProductInput:
    def __init__(self):
        self.category_dao = CategoryDAO()
        self.product_dao = ProductDAO()
        self.product_id = 0
        self.product_category_dao = ProductCategoryDao()

    def list_products(self):
        products = self.product_dao.read_all()
        for prod in products:
            data = f"{prod.name} - {prod.description} - {prod.price} - {prod.categories}"
            print(data)

    def create_product(self):
            product_name = input("Escreva o nome do produto:")
            product_description = input("Escreva a descrição do produto:")
            product_price = input("Escreva o preço do produto:")
            selected_categories = []
            while True:
                print("Selecione uma das categorias abaixo:")
                self.category_dao.read_all()
                selected_categories.append(input())
                option = input("Você deseja cadastrar mais uma categoria? (s/N)")
                if option == "s":
                    continue
                else:
                    break
                print(selected_categories)
            product = Product(product_name, product_description, product_price, selected_categories)
            self.product_id = self.product_dao.create(product)
            for selected_category in selected_categories:
                self.product_category_dao.insert_data_product_category(self.product_id, selected_category)
    
    def delete_product(self):
        product_to_delete = input("Escolha um produto para deletar:")
        product = self.product_dao.delete(product_to_delete)

    def update_product(self):
        selected_categories = []
        product_id = input("Informe o id do produto a editar:")
        product_name = input("Digite um novo nome:")
        product_description = input("Digite uma nova descrição:")
        product_price = input("Digite um novo valor para o produto:")
        while True:
            print("Selecione uma das categorias abaixo:")
            self.category_dao.read_all()
            selected_categories.append(input())
            option = input("Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break
        product_to_update = Product(product_name, product_description, product_price, selected_categories)
        updated_product = self.product_dao.update(product_to_update, product_id)