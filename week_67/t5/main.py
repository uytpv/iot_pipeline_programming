from db_conn import Database
from menu_product import MenuProduct
class Main:
    def __init__(self) -> None:
        print("Program starts.")
        self.menu = MenuProduct()
        self.menu.run_menu()

if __name__ == "__main__":
    app = Main()