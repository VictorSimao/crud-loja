from src.database.database import Database


class ProductCategoryDao(Database):
    def create_table_product_category(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS product_category (
            product_id INTEGER,
            category_id INTEGER,
            FOREIGN KEY(product_id) REFERENCES product(id),
            FOREIGN KEY(category_id) REFERENCES category(id),
            PRIMARY KEY(product_id, category_id)            
            );
        """)
        
    def insert_data_product_category(self, product_id, category_id):
        self.cursor.execute("""
        INSERT INTO product_category (product_id, category_id) VALUES (?, ?)
        """, (product_id, category_id))
        self.commit()

