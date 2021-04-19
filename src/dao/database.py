import sqlite3

class Database:

    def __enter__(self):
        self.conn = sqlite3.connect('database.db')
        return self.conn

    def __exit__(self, type, value, traceback):
        self.conn.close()
