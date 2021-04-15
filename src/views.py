from src.category.dao.category_dao import CategoryDAO
from src.product.dao.product_dao import ProductDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao
from src.category.model.category_model import Category
from src.product.model.product_model import Product

class CategoryView():
    def __init__(self):
        self.category_dao = CategoryDAO()
        
        
    def show_categories(self):
        categories = self.category_dao.read_all()
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)
            

    def form_create_category(self):
        category_name = input("Escreva o nome da categoria:")
        category_description = input("Escreva a descrição da categoria:")
        category = Category(category_name, category_description)
        self.category_dao.create(category)
        
        
class ProductView():
    def __init__(self):
        self.product_dao = ProductDAO()
        self.product_category_dao = ProductCategoryDao()        
        self.category_dao = CategoryDAO()

        
    def show_products(self):
        products_bd = self.product_dao.read_all()
        for prod in products_bd:
            data = f"{prod.id} - {prod.name} - {prod.description} - {prod.price} - Categorias: {prod.categories}" 
            print(data)
            
    
    def show_categories(self):
        categories = self.category_dao.read_all()
        for cat in categories:
            data = f"{cat.id} - {cat.name}"
            print(data)
            
            
    def get_typed_categories(self):
        selected_categories = []
        while True:
            print("Categorias:")
            self.show_categories()
                
            selected_categories.append(input("Selecione uma das categorias acima: "))
            
            option = input("Você deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break
        
        return selected_categories
    
    def form_create_product(self):
        product_name = input("Escreva o nome do produto:")
        product_description = input("Escreva a descrição do produto:")
        product_price = input("Escreva o preço do produto:")
        
        selected_categories = self.get_typed_categories()
        product = Product(product_name, product_description, product_price, selected_categories)
        
        product_id = self.product_dao.create(product)
        
        for selected_category in selected_categories:
            self.product_category_dao.create(product_id, selected_category)
    
    
    def form_update_product(self):
        self.show_products()
        
        product_id_typed = input("Informe o id do produto a ser atualizado:")
        product_for_update = self.product_dao.read_by_id(product_id_typed)
        
        product_name = input("Escreva o nome novo do produto:")
        product_description = input("Escreva a descrição nova do produto:")
        product_price = input("Escreva o preço novo do produto:")
        
        product = Product(product_name, product_description, product_price, product_for_update.categories)
        
        self.product_dao.update(product_id_typed, product)
        
    
    def form_delete_product(self):
        self.show_products()
        
        product_id_typed = str(input("Informe o id do produto a ser deletado:"))
        
        self.product_category_dao.delete(product_id_typed)
        self.product_dao.delete(product_id_typed)