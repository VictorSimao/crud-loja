from src.database.database import Database
from src.product.model.product_model import Product

class ProductDAO(Database):

    def create_table_product(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(200) NOT NULL,
            price REAL NOT NULL
            );
        """)

    def insert_data_product(self, product:Product):
        self.cursor.execute("""
        INSERT INTO product (name, description, price) VALUES (?, ?, ?)
        """, (product.name, product.description, product.price))
        self.commit()
        id = self.cursor.lastrowid
        self.close()
        return id