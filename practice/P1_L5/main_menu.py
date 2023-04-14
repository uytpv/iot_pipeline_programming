from menu import Menu
from coin_punch import CoinPouch
from vending_machine_menu import VendingManchineMenu


class MainMenu(Menu):
    coin_pouch = CoinPouch()
    vending_machine_menu: VendingManchineMenu

    def __init__(self) -> None:
        super().__init__(
            options=[
                {'desc': 'View coins in pouch', 'action': self.showMyCoinPouch},
                {'desc': 'Go to vending machine',
                    'action': self.showVendingMachineMenu},
            ]
        )
        self.vending_machine_menu = VendingManchineMenu()
        return None

    def showVendingMachineMenu(self) -> None:
        self.vending_machine_menu.showMenu()
        return None

    def showMyCoinPouch(self) -> None:
        self.coin_pouch.view_coins()
        return None
