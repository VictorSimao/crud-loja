from src.dao.category_dao import CategoryDAO
from src.dao.product_category_dao import ProductCategoryDao
from src.dao.product_dao import ProductDAO

def init_db():
    category_DAO = CategoryDAO()
    category_DAO.create_table()
    
    product_DAO = ProductDAO()
    product_DAO.create_table()
    
    product_category_Dao = ProductCategoryDao()
    product_category_Dao.create_table()
    
    