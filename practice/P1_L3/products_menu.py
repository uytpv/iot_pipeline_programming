import csv
from menu import Menu


class ProductsMenu(Menu):
    products = []

    def __init__(self) -> None:
        super().__init__(
            title='Products:',
            options=[],
            submenu=True,
            prompt='Select product: ',
        )
        return None
