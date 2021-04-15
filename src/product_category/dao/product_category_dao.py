from src.database.dao import Dao


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

        return self.insert_data(sql, parameters)
        
    def delete_product_id(self, product_id):
        sql = """
            DELETE FROM product_category
                WHERE product_id = ?
        """
        parameters = (product_id,)     
        
        return self.execute_query(sql, parameters)

    def delete_category_id(self, category_id):
        sql = """
            DELETE FROM product_category
                WHERE category_id = ?
        """
        parameters = (category_id,)     
        
        return self.execute_query(sql, parameters)
        
