import csv
from menu import Menu
from coin_punch import CoinPouch
from product import Product
from products_menu import ProductsMenu
from vending_machine import VendingMachine


class VendingManchineMenu(Menu):
    vending_manchine = VendingMachine()
    coin_pouch = CoinPouch()
    products_menu: ProductsMenu
    products = []

    def __init__(self) -> None:
        super().__init__(
            options=[
                {'desc': 'Insert coin', 'action': self.insertCoin},
                {'desc': 'View inserted coins',
                    'action': self.vending_manchine.view_coins},
                # show list of product
                {'desc': 'View products', 'action': self.showProductList},
                {'desc': 'Buy product', 'action': self.showProductsMenu},  # ?buyProduct
                {'desc': 'Return coins', 'action': self.vending_manchine.return_coins},
            ],
            submenu=True
        )
        self.products_menu = ProductsMenu()
        return None

    def showProductsMenu(self) -> None:
        self.products_menu.showMenu()
        return None

    def showProductList(self) -> None:
        with open('products.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.products.append(row)
        print()
        print("Products in vending machine:")
        print("| opt | qty |     brand     |price|")
        print("|-----|-----|---------------|-----|")
        for product in self.products:
            spaces = 15 - len(product['brand'])
            print(
                f"|{product['option']}    |{product['amount']}    |{product['brand']}{' ' * spaces}|{product['price']}    |")
        print()

    def insertCoin(self)->None:
        self.vending_manchine.insert_coin()
        self.coin_pouch.minus_coin()