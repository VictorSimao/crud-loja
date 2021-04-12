from src.database.database import Database

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

    def insert_data_product(self, name, description, price):
        self.cursor.execute("""
        INSERT INTO product (name, description, price) VALUES (?, ?, ?)
        """, (name, description, price))
        self.commit()
        return self.cursor.lastrowid
