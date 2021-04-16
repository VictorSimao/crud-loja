from src.database.dao import Dao
from src.product.model.product_model import Product
from typing import List
from src.product_category.dao.product_category_dao import ProductCategoryDao

class ProductDAO(Dao):

    def create_table_product(self):
        # TODO: renomear para create_table
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
        sql = """
        SELECT product.id, product.name, product.description, product.price, group_concat(category.name)
        FROM product JOIN product_category ON product_id = product.id JOIN category ON category_id = category.id
        GROUP BY product.id, product.name, product.description, product.price
        """
        list_products = []
        
        result = self.execute_query_select(sql)

        for item in result:
            product = Product(item[1], item[2], item[3], item[4], item[0])
            list_products.append(product)

        return list_products

        
    def select_data_product(self, product:Product):
        # TODO: renomear para select_data
        print(self.cursor.execute("""
        SELECT * FROM product WHERE id = ?
        """, product.id))
        
    
    def read_by_id(self, id:int)-> Product:
        sql = """
        SELECT product.id, product.name, product.description, product.price, group_concat(category.name)
        FROM product JOIN product_category ON product_id = product.id JOIN category ON category_id = category.id
        WHERE product.id = ?
        GROUP BY product.id, product.name, product.description, product.price
        """
        # TODO: refatorar o id para (id,)
        parameter = id

        result = self.execute_query_select(sql, parameter)
        item = result[0]

        product = Product(item[1], item[2], item[3], item[4], item[0])

        return product


    def update(self, id:int, product:Product):
        sql = """
            UPDATE product
                SET
                    name = ?
                    ,description = ?
                    ,price = ?
                WHERE id = ?
        """
        parameters = (product.name, product.description, product.price, id)  

        return self.execute_query(sql, parameters)
    
    
    def delete(self, id:int):
        sql = """
            DELETE FROM product
                WHERE id = ?
        """
        parameters = (id,)     
        
        return self.execute_query(sql, parameters)