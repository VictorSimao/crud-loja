from .database import Database

from typing import NoReturn


class Dao:

    def insert_data(self, sql: str, parameters: tuple) -> int:
        with Database() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, parameters)
            conn.commit()
            id = cursor.lastrowid
        return id

    # Só faz a query no banco de dados sem esperar nenhum retorno.
    def execute_query(self, sql: str, parameters: tuple = None) -> NoReturn:
        with Database() as conn:
            cursor = conn.cursor()
            if parameters:
                result = cursor.execute(sql, parameters)
            else:
                cursor.execute(sql)
            conn.commit()

    # Tem um retorno, ou seja vem uma informação da tabela.
    def execute_query_select(self, sql: str, parameters: tuple = None) -> tuple:
        with Database() as conn:
            cursor = conn.cursor()
            result = ()
            if parameters:
                result = cursor.execute(sql, parameters)
                result = cursor.fetchall()
            else:
                cursor.execute(sql)
                result = cursor.fetchall()
        return result
