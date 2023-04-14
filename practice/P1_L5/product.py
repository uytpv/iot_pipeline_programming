import csv


class Product:
    products = []
    def __init__(self, option, amount, brand, price) -> None:
        self.option = option
        self.amount = amount
        self.brand = brand
        self.price = price