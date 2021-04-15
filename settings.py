from src.category.dao.category_dao import CategoryDAO
from src.product.dao.product_dao import ProductDAO
from src.product_category.dao.product_category_dao import ProductCategoryDao

def init_bd():
    CategoryDAO().create_table_category()
    ProductDAO().create_table_product()
    ProductCategoryDao().create_table_product_category()
    

# Database name
DATABASE_NAME = 'database.db'