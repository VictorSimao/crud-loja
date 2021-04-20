from typing import List

from src.dao.dao import Dao
from src.model.category_model import Category


class CategoryDAO(Dao):
    def create_table(self):
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

    def read_by_id(self, product_id: int) -> Category:
        sql = """
        SELECT * FROM category WHERE id = ?
        """
        parameter = (product_id,)
        result = self.execute_query_select(sql, parameter)
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

    def delete(self, product_id: int):
        sql = """
            DELETE FROM category
                WHERE id = ?
        """
        parameters = (product_id,)
        return self.execute_query(sql, parameters)
