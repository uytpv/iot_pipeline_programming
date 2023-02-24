from pathlib import Path
import sqlite3
DB_FILEPATH = Path().joinpath('dev.db')
DB_CONN = sqlite3.connect(DB_FILEPATH)

class Main:
    def __init__(self) -> None:
        self.createTable()
        return None

    def createTable(self) -> None:
        cursor = DB_CONN.cursor()
        PRODUCT_TABLE_STATEMENT = """CREATE TABLE product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            manufacturer VARCHAR(255) NOT NULL,
            brand VARCHAR(255) NOT NULL,
            barcode INTEGER(13) NOT NULL
        );"""
        cursor.execute(PRODUCT_TABLE_STATEMENT)
        DB_CONN.commit()
        DB_CONN.close()
        return None

if __name__ == "__main__":
    app = Main()