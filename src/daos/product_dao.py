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
       SELECT product.id, product.name, product.description, product.price,
       group_concat(category.id),group_concat(category.name), group_concat(category.description)
       FROM product LEFT JOIN product_category ON product_id = product.id LEFT JOIN category ON category_id = category.id
       GROUP BY product.name, product.description, product.price
       ORDER BY product.id
        """
        list_products = []
        result = self.execute_query_select(sql)

        for item in result:
            cat_id = item[4].split(",") 
            cat_name = item[5].split(",")
            cat_description = item[6].split(",")
            list_cat = []
            for pos in range(len(cat_id)):
                category = Category(cat_name[pos], cat_description[pos],
                                    cat_id[pos])
                list_cat.append(category)
                print(category.name)

            product = Product(
                name=item[1],
                description=item[2],
                price=item[3],
                categories=list_cat,
                id=item[0]
            )
            list_products.append(product)
        return list_products 
                






        # list_products = []
        # list_category = []

        # result = self.execute_query_select(sql)

        # for i in result:
        #     category = Category(id=i[4], name=i[5], description=i[6])
        #     list_category.append(category)

        # for item in result:
        #     product = Product(item[1], item[2], item[3], list_category,
        #                       item[0])
        #     list_products.append(product)
        # print(list_products)
        # return list_products

    def read_by_id(self, id: int):
        sql = """
        SELECT product.id, product.name, product.description, product.price,
        group_concat(category.id), group_concat(category.name)
        FROM product JOIN product_category ON product_id = product.id
        JOIN category ON category_id = category.id
        WHERE product.id = ?
        GROUP BY product.name, product.description, product.price
        ORDER BY product.id
        """
        parameter = (id, )

        result = self.execute_query_select(sql, parameter)
        item = result[0]

        product = Product(item[1], item[2], item[3], item[4], item[0])
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
