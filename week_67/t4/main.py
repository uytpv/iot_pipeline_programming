from typing import Tuple
from pathlib import Path
import sqlite3
DB_FILEPATH = Path().joinpath('dev.db')
DB_CONN = sqlite3.connect(DB_FILEPATH)

class Main:
    def __init__(self) -> None:
        print("Program starts.")
        self.createTable()

        while True:
            print("Options:")
            print("1) Add product")
            print("2) Show products")
            print("0) Exit")
            choice = int(input("Choice: "))
            if choice == 1:
                self.insertData()
            elif choice == 2:
                self.showProducts()
            elif choice == 0:
                break
            else:
                print("Unknown option.")
            print("")

        DB_CONN.close()
        print("Program ends.")
        return None

    def createTable(self) -> None:
        cursor = DB_CONN.cursor()
        PRODUCT_TABLE_STATEMENT = """CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            manufacturer VARCHAR(255) NOT NULL,
            brand VARCHAR(255) NOT NULL,
            barcode INTEGER(13) NOT NULL
        );"""
        cursor.execute(PRODUCT_TABLE_STATEMENT)
        DB_CONN.commit()
        cursor.close()
        return None
    
    def insertData(self)-> None:
        cursor = DB_CONN.cursor()
        PRODUCT_INSERT_STATEMENT = """
        INSERT INTO product (manufacturer, brand, barcode) VALUES (?,?,?)
        """
        data = self.createProductObj()
        cursor.execute(PRODUCT_INSERT_STATEMENT, data)
        DB_CONN.commit()
        cursor.close()
        return None
    
    def createProductObj(self)->Tuple[str,str,int]:
        print("Insert product details")
        manufacturer = input("Manufacturer: ")
        brand = input("Brand: ")
        barcode = int(input("Barcode: "))
        prod_obj = (manufacturer, brand, barcode,)
        return prod_obj
    
    def showProducts(self)-> None:
        cursor = DB_CONN.cursor()
        GET_ALL_PRODUCT_STATEMENT = "SELECT * FROM product"
        cursor.execute(GET_ALL_PRODUCT_STATEMENT)
        products = cursor.fetchall()
        DB_CONN.commit()
        cursor.close()
        print("Products: ")
        for prod in products:
            print(f"Product: {prod[0]} - Manufacturer: {prod[1]}, Brand: {prod[2]}, Barcode: {prod[3]}")
        return None

if __name__ == "__main__":
    app = Main()