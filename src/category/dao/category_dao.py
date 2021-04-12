from src.database.database import Database


class CategoryDAO(Database):
    def create_table_category(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(200) NOT NULL
        );
        """)

    def insert_data_category(self, name, description):
        self.cursor.execute("""
        INSERT INTO category (name, description) VALUES (?, ?)
        """, (name, description))
        self.commit()
        return self.cursor.lastrowid
