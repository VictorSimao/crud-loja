from src.product.dao.product_dao import ProductDAO
from src.product.model.product_model import Product
from typing import NoReturn


class ProductController:
    def __init__(self):
        self.product_dao = ProductDAO()

    def create_product(self):
        return self.product_dao.create(Product(input('Nome: '), input('Descrição: '), input('Valor: ')))

    def read_product(self) -> NoReturn:
        products = self.product_dao.read_all()
        print("\n\n=============== Produtos =================")
        print("ID - NOME - PREÇO - DESCRIÇÃO - CATEGORIAS")
        for prod in products:
            data = f"{prod.id} - {prod.name} - {prod.price} - {prod.description} - {prod.categories}"
            print(data)

    def update_product(self):
        id = input('Id: ')
        self.product_dao.update(Product(input('Nome: '), input(
            'Descrição: '), input('Price: '), id))
        return id

    def delete_product(self):
        id = int(input('Id Produto: '))
        self.product_dao.delete((id,))
        return id
