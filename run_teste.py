
from src.category.dao.category_dao import CategoryDAO
from src.product.dao.product_dao import ProductDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao


def controller():
    category = CategoryDAO()
    product = ProductDAO()
    product_category = ProductCategoryDao()


    category.create_table_category()
    product.create_table_product()
    product_category.create_table_product_category()

if __name__ == '__main__':
    controller()
