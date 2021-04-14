from src.database.dao import Dao
from src.product.model.product_model import Product

class ProductDAO(Dao):

    def create_table_product(self):
        self.execute_query("""
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
        print("oi", id)
        return id

    def select_all_data_product(self):
        self.cursor.execute("""
        SELECT product.name, product.description, product.price, group_concat(category.name)
        FROM product JOIN product_category ON product_id = product.id JOIN category ON category_id = category.id
        GROUP BY product.name, product.description, product.price
        """)

        for product in self.cursor.fetchall():
            print(product)
        
    def select_data_product(self, product:Product):
        print(self.cursor.execute("""
        SELECT * FROM product WHERE id = ?
        """, product.id))
