from src.daos.dao import Dao

from src.models.product_model import Product
from src.models.category_model import Category


"""
This class makes a communication between product controller data and
set the queries to save product table on database.
"""


class ProductDAO(Dao):

    def __init__(self):
        self.create_table()

    def create_table(self):
        self.execute_query("""
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(200) NOT NULL,
            price REAL NOT NULL
            );
        """)

    def create(self, product):
        sql = """
        INSERT INTO product (name, description, price) VALUES (?, ?, ?)
        """
        parameters = (product.name, product.description, product.price)
        return self.insert_data(sql, parameters)

    def read_all(self):
        sql = """
        SELECT
            p.id
            ,p.name
            ,p.description
            ,p.price
            ,pc.product_id
            ,c.id
            ,c.name
            ,c.description
        FROM product as p
        LEFT JOIN product_category as pc
        ON pc.product_id = p.id
        LEFT JOIN category as c
        ON pc.category_id = c.id
        """

        result = Dao().execute_query_select(sql)
        products = [p[:4] for p in result]
        categories = [c[4:] for c in result]
        list_products = []
        for prod in set(products):
            prod_cats = [Category(c[2], c[3], c[1]) for c in categories if c[0] == prod[0]]
            product = Product(prod[1], prod[2], prod[3], prod_cats, prod[0])
            list_products.append(product)

        return list_products

    def read_by_id(self, id: int):
        sql = """
        SELECT product.id, product.name, product.description, product.price,
        group_concat(category.id ||';'|| category.name ||';'|| category.description)
        FROM product LEFT JOIN product_category ON product_id = product.id
        LEFT JOIN category ON category_id = category.id
        WHERE product.id = ?
        GROUP BY product.name, product.description, product.price
        ORDER BY product.id
        """
        parameter = (id, )
        categories = []
        result = self.execute_query_select(sql, parameter)
        item = result[0]
        if item[4]:
            categories = [c.split(';') for c in item[4].split(',')]
            categories = [Category(category[1], category[2], category[0])
                          for category in categories]
        product = Product(item[1], item[2], item[3], categories, item[0])
        return product

    def update(self, product):
        sql = """
            UPDATE product
                SET
                    name = ?
                    ,description = ?
                    ,price = ?
                WHERE id = ?
        """
        parameters = (product.name, product.description,
                      product.price, product.id)

        return self.execute_query(sql, parameters)

    def delete(self, id: int):
        sql = """
            DELETE FROM product
                WHERE id = ?
        """
        parameters = (id, )

        return self.execute_query(sql, parameters)
