import sqlite3
from pathlib import Path

class Database:
    DB_FILEPATH = Path().joinpath('dev.db')
    DB_CONN = sqlite3.connect(DB_FILEPATH)

    def __init__(self):
        pass

    def create_table(self) -> None:
        cursor = self.DB_CONN.cursor()
        PRODUCT_TABLE_STATEMENT = """CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            manufacturer VARCHAR(255) NOT NULL,
            brand VARCHAR(255) NOT NULL,
            barcode INTEGER(13) NOT NULL
        );"""
        cursor.execute(PRODUCT_TABLE_STATEMENT)
        self.DB_CONN.commit()
        cursor.close()

    def close_connection(self) -> None:
        self.DB_CONN.close()

