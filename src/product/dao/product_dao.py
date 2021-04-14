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
        parameters = (product.name, product.description, product.price)
        return self.insert_data(sql, parameters)

    def read_all(self) -> List[Product]:
        sql = """ 
        SELECT * FROM product
        """

        list_products = []

        result = self.execute_query_select(sql)

        for item in result:
            product = Product(item[1], item[2], item[3], item[0])
            list_products.append(product)
        
        return list_products

    def read_by_id(self, id:int) -> Product:
        sql = """
        SELECT * FROM product WHERE id = ?
        """
        parameter = id

        result = self.execute_query_select(sql, parameter)
        item = result[0]

        product = Product(item[1], item[2], item[3], item[4], item[0])
        return product

    def update(self, product:Product):
        sql = """
            UPDATE product
                SET
                    name = ?
                    ,description = ?
                    ,price = ?
                    ,categories = ?
                WHERE id = ?
        """
        parameters = (product.name, product.description, product.price, product.categories, product.id)

        return self.execute_query(sql, parameters)

    def delete(self, id:int):
        sql = """
            DELETE FROM product
                WHERE id = ?
        """

        parameters = (id,)

        return self.execute_query(sql, parameters)

    # def select_all_data_product(self):
    #     self.cursor.execute("""
    #     SELECT product.name, product.description, product.price, group_concat(category.name)
    #     FROM product JOIN product_category ON product_id = product.id JOIN category ON category_id = category.id
    #     GROUP BY product.name, product.description, product.price
    #     """)

    #     for product in self.cursor.fetchall():
    #         print(product)
        
