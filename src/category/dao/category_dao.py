from src.database.dao import Dao
from src.category.model.category_model import Category
from typing import List


class CategoryDAO(Dao):
    def create_table_category(self):
        self.execute_query("""
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(200) NOT NULL
        );
        """)

    def create(self, category: Category):
        sql = """
        INSERT INTO category ("name", "description") VALUES (?, ?);
        """
        parameters = (category.name, category.description)
        return self.insert_data(sql, parameters)

    def read_all(self) -> List[Category]:
        sql = """
        SELECT * FROM category
        """

        list_categories = []

        result = self.execute_query_select(sql)

        for item in result:
            category = Category(item[1], item[2], item[0])
            list_categories.append(category)

        return list_categories

    def read_by_id(self, category_id: int) -> Category:
        sql = """
        SELECT * FROM category WHERE id = ?
        """
        result = self.execute_query_select(sql, category_id)
        item = result[0]

        category = Category(item[1], item[2], item[0])
        return category

    def update(self, category: Category):
        sql = """
            UPDATE category
                SET
                    name = ?
                    ,description = ?
                WHERE id = ?
        """
        parameters = (category.name, category.description, category.id)

        return self.execute_query(sql, parameters)

    def delete(self, id: int):
        sql = """
            DELETE FROM category
                WHERE id = ?
        """
        parameters = (id)

        return self.execute_query(sql, parameters)
