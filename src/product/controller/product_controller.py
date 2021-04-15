from src.product.dao.product_dao import ProductDAO
from src.product.model.product_model import Product
from typing import NoReturn


class ProductController(ProductDAO):
    def create_controller(self):
        return self.create(Product(input('Nome: '), input('Descrição: '), input('Valor: ')))

    def read_controller(self) -> NoReturn:
        products = self.read_all()
        print("\n\n=============== Produtos =================")
        print("ID - NOME - PREÇO - DESCRIÇÃO - CATEGORIAS")
        for prod in products:
            data = f"{prod.id} - {prod.name} - {prod.price} - {prod.description} - {prod.categories}"
            print(data)

    def update_controller(self):
        id = input('Id: ')
        self.update(Product(input('Nome: '), input('Descrição: '), input('Price: '), id))
        return id

    def delete_controller(self):
        id = int(input('Id Produto: '))
        self.delete((id,))
        return id