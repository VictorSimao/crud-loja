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

    def create(self, product_id, category_id):
        sql = """
        INSERT INTO product_category (product_id, category_id) VALUES (?, ?)
        """
        parameters = (product_id, category_id)
        return self.insert_data(sql, parameters)

    def update(self, product_id, category_id, new_category_id):
        sql = """
            UPDATE product_category
                SET
                    category_id = ?
                WHERE product_id = ? AND category_id = ?
        """
        parameters = (new_category_id, product_id, category_id)

        return self.execute_query(sql, parameters)

    def delete(self, id: int):
        sql = """
            DELETE FROM product_category
                WHERE product_id = ?
        """
        parameters = (id)

        return self.execute_query(sql, parameters)
