from configparser import ConfigParser
import configparser
import sqlite3
from pathlib import Path


class Database:
    config = configparser.ConfigParser()
    config.read('config.ini')
    filepath = config.get('SQLite', 'filepath')

    DB_FILEPATH = Path().joinpath(filepath)
    DB_CONN = sqlite3.connect(DB_FILEPATH)

    def __init__(self) -> None:

        return None

    def execute(self, statement) -> None:
        cursor = self.DB_CONN.cursor()
        result = cursor.execute(statement).fetchone()[0]
        self.DB_CONN.commit()
        cursor.close()
        return result

    def executeWithParams(self, statement, params) -> None:
        cursor = self.DB_CONN.cursor()
        cursor.execute(statement, params)
        result = cursor.fetchone()
        self.DB_CONN.commit()
        cursor.close()
        if result is not None:
            return result[0]
        else:
            return None

    def close_connection(self) -> None:
        self.DB_CONN.close()
