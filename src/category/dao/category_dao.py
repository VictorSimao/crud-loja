from src.database.database import Database
from src.category.model.category_model import Category


class CategoryDAO(Database):
    def create_table_category(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(200) NOT NULL
        );
        """)

    def insert_data_category(self, category:Category):
        self.cursor.execute("""
        INSERT INTO category ("name", "description") VALUES (?, ?);
        """, (category.name,category.description))
        self.commit()
        id = self.cursor.lastrowid
        self.close()
        return id

    def select_all_data_category(self):
        self.cursor.execute("""
        SELECT * FROM category
        """)

        for category in self.cursor.fetchall():
            print(category)

    def select_data_category(self, category:Category):
        print(self.cursor.execute("""
        SELECT * FROM category WHERE id = ?
        """, category.id))

    def close(self):
        self.close()