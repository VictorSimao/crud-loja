from src.category.dao.category_dao import CategoryDAO
from src.product.dao.product_dao import ProductDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao
from src.category.model.category_model import Category
from src.product.model.product_model import Product


def controller():
    category_dao = CategoryDAO()
    product_dao = ProductDAO()
    product_category = ProductCategoryDao()


    category_dao.create_table_category()
    product_dao.create_table_product()
    product_category.create_table_product_category()

    category = Category('categoryName','cate')
    categories = [category]
    product = Product('OutroTeste','Teste', 20.00, categories)
    print(category.name, type(category.name))
    last_category = category_dao.insert_data_category(category)
    last_product = product_dao.insert_data_product(product)
    
    # product_category.insert_data_product_category(last_product,last_category)

if __name__ == '__main__':
    controller()

