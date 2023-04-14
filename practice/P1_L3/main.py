
import configparser
from main_menu import MainMenu


class Main:
    print('Program starting.')
    # config = configparser.ConfigParser()

    def __init__(self) -> None:
        # 1- init
        # self.config.read('config.ini')
        # self.config.set('Coins', 'inserted_coins', '0')
        # self.config.set('Coins', 'coin_pouch', '12')
        # with open('config.ini', 'w') as configfile:
        #     self.config.write(configfile)
        main_menu = MainMenu()

        # 2- run
        main_menu.showMenu()

        # 3- clean
        return None


if __name__ == '__main__':
    app = Main()
