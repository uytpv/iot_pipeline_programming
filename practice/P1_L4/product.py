import csv


class Product:
    def __init__(self):
        self.products = []
        with open('products.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.products.append(row)

    def save_products(self):
        with open('products.csv',  'w',    newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[
                                    'option',  'amount', 'brand', 'price'])
            writer.writeheader()
            writer.writerows(self.products)

    def view_products(self):
        print("Products in vending machine:")
        print("| opt | qty | brand | price |")
        print("|-----|-----|-------|-------|")
        for product in self.products:
            print(
                f"| {product['option']} | {product['amount']} | {product['brand']} | {product['price']} |")

    def is_product_available(self, option):
        option_index = int(option) - 1
        if option_index < 0 or option_index >= len(self.products):
            print("Unknown option, try again!")
            return False
        product = self.products[option_index]
        if int(product['amount']) == 0:
            print("Product is sold out!")
            return False
        return True
