from src.dao.dao import Dao
from src.model.product_model import Product


class ProductDAO(Dao):

    def create_table(self):
        self.execute_query("""
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(200) NOT NULL,
            price REAL NOT NULL
            );
        """)

    def create(self, product: Product):
        sql = """
        INSERT INTO product (name, description, price) VALUES (?, ?, ?)
        """
        parameters = (product.name, product.description, product.price)
        return self.insert_data(sql, parameters)

    def read_all(self):
        sql = """
        SELECT product.id, product.name, product.description, product.price, group_concat(category.name)
        FROM product LEFT JOIN product_category 
        ON product_id = product.id 
        LEFT JOIN category 
        ON category_id = category.id
        GROUP BY product.name, product.description, product.price ORDER BY product.id
        """
        list_products = []
        result = self.execute_query_select(sql)
        for item in result:
            product = Product(item[1], item[2], item[3], item[0], item[4])
            list_products.append(product)
        return list_products

    def read_by_id_product(self, product_id: int):
        sql = """ 
        SELECT * FROM product WHERE id = ? 
        """
        print(type(product_id))
        parameter = (product_id,)
        result = self.execute_query_select(sql, parameter)
        item = result[0]
        product = Product(item[1], item[2], item[3], item[0])
        return product

    def update(self, product: Product):
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
            DELETE FROM product WHERE id = ?
        """

        # Também pode ser usado dessa maneira -> parameter = tuple(id,)
        parameter = (id,)
        return self.execute_query(sql, parameter)
        