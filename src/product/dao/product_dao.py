from src.database.dao import Dao
from src.product.model.product_model import Product
from typing import NoReturn
import sqlite3


class ProductDAO(Dao):

    def create_table_product(self) -> NoReturn:
        self.execute_query("""
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(200) NOT NULL,
            price REAL NOT NULL
            );
        """)

    def create(self, product: Product) -> sqlite3:
        sql = """
        INSERT INTO product (name, description, price) VALUES (?, ?, ?)
        """
        parameters = (product.name, product.description, product.price)
        return self.insert_data(sql=sql, parameters=parameters)

    def read_all(self) -> NoReturn:
        sql = """
        SELECT product.id, product.name, product.description, product.price, group_concat(category.name)
        FROM product JOIN product_category ON product_id = product.id JOIN category ON category_id = category.id
        GROUP BY product.name, product.description, product.price ORDER BY product.id
        """
        list_products = []
        result = self.execute_query_select(sql)
        [list_products.append(
            Product(item[1], item[2], item[3], item[4], item[0])) for item in result]
        return list_products

    def read_by_id(self, product_id: int) -> Product:
        sql = """
            SELECT * FROM product WHERE id = ?
        """
        result = self.execute_query_select(sql=sql, parameters=[product_id])
        item = result[0]
        product = Product(item[1], item[2], item[3], item[0])
        return product

    def update(self, product: Product) -> sqlite3:
        sql = """
            UPDATE product
            SET 
            name= ?, 
            description= ?, 
            price= ?,
            WHERE ID = ?
        """

        parameters = (product.name,
                      product.description, product.price,
                      product.id
                      )

        return self.execute_query(sql=sql, parameters=parameters)

    def delete(self, product_id: int) -> sqlite3:
        sql = """
            DELETE FROM product WHERE ID = ? 
        """

        return self.execute_query(sql=sql, parameters=product_id)
