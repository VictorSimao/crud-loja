from src.database.dao import Dao
from src.product.model.product_model import Product
from typing import List


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

    def create(self, product:Product):
        sql = """
        INSERT INTO product (name, description, price) VALUES (?, ?, ?)
        """
        parameters =  (product.name, product.description, product.price)
        return self.insert_data(sql, parameters)


    def read_all(self)-> List[Product]:
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
