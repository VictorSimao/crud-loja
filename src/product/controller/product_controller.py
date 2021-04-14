from src.product.dao.product_dao import ProductDAO
from src.product.model.product_model import Product
from typing import NoReturn


class ProductController(ProductDAO):
    def create_controller(self) -> NoReturn:
        return self.create(Product(input('Nome: '), input('Descrição: '), input('Valor: ')))

    def read_controller(self) -> NoReturn:
        products = self.read_all()
        for prod in products:
            data = f"{prod.name} - {prod.price} - {prod.description} - {prod.categories}"
            print(data)

    def add_category(self) -> list:
        selected_categories = []
        while True:
            print("Selecione uma das categorias acima:")
            selected_categories.append(input())
            option = input(
                "Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break
        return selected_categories
