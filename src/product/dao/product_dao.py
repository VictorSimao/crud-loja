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

    def create(self, product:Product):
        sql = ("""
        INSERT INTO product (name, description, price) VALUES (?, ?, ?)
        """)
        parameters = (product.name, product.description, product.price)
        return self.insert_data(sql, parameters)

    # def select_all_data_product(self):
    #     self.cursor.execute("""
    #     SELECT product.name, product.description, product.price, group_concat(category.name)
    #     FROM product JOIN product_category ON product_id = product.id JOIN category ON category_id = category.id
    #     GROUP BY product.name, product.description, product.price
    #     """)

    #     for product in self.cursor.fetchall():
    #         print(product)

    def read_all_products_with_category(self):
        sql = ("""
        SELECT product.name, product.description, product.price, group_concat(category.name)
        FROM product JOIN product_category ON product_id = product.id JOIN category ON category_id = category.id
        GROUP BY product.name, product.description, product.price """)
        list_products_with_category = []
        result = self.execute_query_select(sql)
        for item in result:
            products = Product(item[1], item[2],item[3], item[4], item[0])
            list_products_with_category.append(products)
        return list_products_with_category

    def read_by_id(self, id: int) -> Product:
        sql = ("""
        SELECT * FROM product WHERE id = ?
        """)
        parameter = id
        result = self.execute_query_select(sql, parameter)
        item =  result[0]
        product = Product(item[1], item[2],item[3], item[4], item[0])
        return product
    
         
    def select_data_product(self, product:Product):
        print(self.cursor.execute("""
        SELECT * FROM product WHERE id = ?
        """, product.id))
