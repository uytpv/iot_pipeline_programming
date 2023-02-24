from pathlib import Path
import sqlite3

DB_FILEPATH = Path().joinpath('dev.db')

DB_CONN = sqlite3.connect(DB_FILEPATH)

DB_CONN.close()