from typing import Tuple
from db_conn import Database

class MenuProduct:
    def __init__(self):
        self.db = Database()
        self.db.create_table()

    def run_menu(self) -> None:
        while True:
            print("Options:")
            print("1) Add product")
            print("2) Show products")
            print("0) Exit")
            choice = int(input("Choice: "))
            if choice == 1:
                self.insert_data()
            elif choice == 2:
                self.show_products()
            elif choice == 0:
                print("Program ends.")
                self.db.close_connection()
                break
            else:
                print("Unknown option.")
            print("")

    def insert_data(self) -> None:
        cursor = self.db.DB_CONN.cursor()
        PRODUCT_INSERT_STATEMENT = """
        INSERT INTO product (manufacturer, brand, barcode) VALUES (?,?,?)
        """
        data = self.create_product_obj()
        cursor.execute(PRODUCT_INSERT_STATEMENT, data)
        self.db.DB_CONN.commit()
        cursor.close()

    def create_product_obj(self) -> Tuple[str,str,int]:
        print("Insert product details")
        manufacturer = input("Manufacturer: ")
        brand = input("Brand: ")
        barcode = int(input("Barcode: "))
        prod_obj = (manufacturer, brand, barcode,)
        return prod_obj

    def show_products(self) -> None:
        cursor = self.db.DB_CONN.cursor()
        GET_ALL_PRODUCT_STATEMENT = "SELECT * FROM product"
        cursor.execute(GET_ALL_PRODUCT_STATEMENT)
        products = cursor.fetchall()
        self.db.DB_CONN.commit()
        cursor.close()
        print("Products: ")
        for prod in products:
            print(f"Product: {prod[0]} - Manufacturer: {prod[1]}, Brand: {prod[2]}, Barcode: {prod[3]}")
