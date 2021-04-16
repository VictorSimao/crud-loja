
class Product:
    def __init__(self, name, description, price, id=None, categories=[]):
        self.name = name
        self.description = description
        self.price = price
        self.id = id
        self.categories = categories

    def list_product(self):
        products = self.product_dao.read_all_products()
        for prod in products:
            data = f"{prod.id} - {prod.name} - {prod.description} - {prod.price}"
            print(data)

    def register_product(self):
        product_name = input("Escreva o nome do produto:")
        product_description = input("Escreva a descrição do produto:")
        product_price = input("Escreva o preço do produto:")
        selected_categories = []
        while True:
            print("Selecione uma das categorias abaixo:")
            categories = self.category_dao.read_all()
            for cat in categories:
                data = f"{cat.id} - {cat.name} - {cat.description}"
                print(data)
            selected_categories.append(input())
            option = input(
                "Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break
            print(selected_categories)
        product = Product(product_name, product_description,
                          product_price, selected_categories)
        self.product_id = self.product_dao.create_product(product)
        for selected_category in selected_categories:
            self.product_category_dao.insert_data_product_category(
                self.product_id, selected_category)

    def delected_produtcs(self):
        print('Digite o numero do produto que deseja excluir: ')
        Product.list_product(self)
        delete = int(input())
        self.product_dao.delete_product(delete)