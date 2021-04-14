from src.database.dao import Dao
from src.category.model.category_model import Category
from typing import List

class ProductCategoryDao(Dao):
    def create_table_product_category(self):
        self.execute_query("""
        CREATE TABLE IF NOT EXISTS product_category (
            product_id INTEGER,
            category_id INTEGER,
            FOREIGN KEY(product_id) REFERENCES product(id),
            FOREIGN KEY(category_id) REFERENCES category(id),
            PRIMARY KEY(product_id, category_id)            
            );
        """)
        
    def create(self, product_id, category_id) -> int:
        sql = """
        INSERT INTO product_category (product_id, category_id) VALUES (?, ?)
        """
        parameters =  (product_id, category_id)

        id = self.insert_data(sql, parameters)
        return id
    
    
    def read_categories_by_product_id(self, id:int) -> List[Category]:
        sql = """
        SELECT * FROM product_category WHERE product_id = ?
        """
        parameter = id
        list_categories = []

        result = self.execute_query_select(sql, parameter)
        for item in result:
            print(item[0], item[1])
            # category = Category(item[1], item[2], item[0])
            # list_categories.append(category)

        return list_categories