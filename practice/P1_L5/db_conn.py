import configparser
import sqlite3
from pathlib import Path


class Database:
    config = configparser.ConfigParser()
    config.read('config.ini')
    filepath = config('SQLite', 'filepath')

    DB_FILEPATH = Path().joinpath(filepath)
    DB_CONN = sqlite3.connect(DB_FILEPATH)

    def __init__(self):
        pass

    def create_table(self, statement) -> None:
        cursor = self.DB_CONN.cursor()
        # PRODUCT_TABLE_STATEMENT = """CREATE TABLE IF NOT EXISTS product (
        #     id INTEGER PRIMARY KEY AUTOINCREMENT,
        #     manufacturer VARCHAR(255) NOT NULL,
        #     brand VARCHAR(255) NOT NULL,
        #     barcode INTEGER(13) NOT NULL
        # );"""
        cursor.execute(statement)
        self.DB_CONN.commit()
        cursor.close()

    def close_connection(self) -> None:
        self.DB_CONN.close()
