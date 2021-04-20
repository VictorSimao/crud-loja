from typing import List

from src.dao.dao import Dao
from src.model.product_category_model import ProductCategory


class ProductCategoryDao(Dao):
    def create_table(self):
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
        parameters = (product_id, category_id)
        id = self.insert_data(sql, parameters)
        return id

    def read_categories_by_product_id(self, product_id) -> List[ProductCategory]:
        sql = """
        SELECT * FROM product_category 
        WHERE product_id = ?  
        """
        list_product_category = []
        parameter = (product_id,)
        result = self.execute_query_select(sql, parameter)
        for item in result:
            prod_cat_model = ProductCategory(item[0], item[1])
            list_product_category.append(prod_cat_model)
        return list_product_category

    def delete(self, product_id: int):
        sql = """
        DELETE FROM product_category WHERE product_id = ?    
        """
        parameter = (product_id,)
        return self.execute_query(sql, parameter)

    def delete_category_by_product_id(self, product_id: int, category_id: int):
        sql = """
        DELETE FROM product_category 
        WHERE product_id = ? 
        AND category_id = ?     
        """
        parameters = (product_id, category_id)
        return self.execute_query(sql, parameters)
