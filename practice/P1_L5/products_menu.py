import csv
import time
from menu import Menu
from db_conn import Database
from vending_machine import VendingMachine


class ProductsMenu(Menu):
    products = []
    buy_product_success = False
    database: Database

    def __init__(self) -> None:
        arr = []
        with open('products.csv') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                option = {'desc': row['brand'] + ', ' + row['price'] + ' coin(s)',
                          'action': lambda row=row: self.buyProduct(row)}
                arr.append(option)

        super().__init__(
            title='Products:',
            options=arr,
            submenu=True,
            prompt='Select product: ',
        )
        return None

    def buyProduct(self, row) -> None:
        print('Sihh...')
        print('Glunk Glunk! mm. taste like ' + row['brand'])
        print()
        vending_machine = VendingMachine()
        self.buy_product_success = True
        if vending_machine.buyProduct(row['price']):

            self.database = Database()
            INSERT_SALE_STATEMENT = '''INSERT INTO sale (commodity_brand, price, cost, created_at) 
                                        VALUES (?, ?, ?, ?);'''
            GET_COST_STATEMENT = 'SELECT cost FROM commodity WHERE brand = "' + \
                row['brand']+'"; '

            cost = self.database.execute(GET_COST_STATEMENT)
            timestamp = int(time.time())
            rs = self.database.executeWithParams(
                INSERT_SALE_STATEMENT, (row['brand'], row['price'], cost, timestamp))

            row['amount'] = str(int(row['amount']) - 1)
            products = []  # Danh sách sản phẩm
            with open('products.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for r in reader:
                    if r['brand'] == row['brand']:
                        products.append(row)
                    else:
                        products.append(r)
            with open('products.csv', 'w', newline='') as csvfile:
                fieldnames = products[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(products)
        return None

    def showMenu(self) -> None:
        print()
        while True:
            self.showOptions()
            choice = self.askChoice()
            if choice == 0:
                print()
                if self.submenu == True:
                    break
                else:
                    print('Program ending.')
                    break
            elif 1 <= choice <= len(self.options):
                index = choice - 1
                self.options[index]['action']()
                if self.buy_product_success:
                    self.buy_product_success = False
                    break
            else:
                print('Unknown option.')

        return None
