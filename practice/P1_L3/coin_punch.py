
import configparser


class CoinPouch:
    config = configparser.ConfigParser()

    def __init__(self):
        self.config.read('config.ini')
        self.coins = self.config.getint('Coins', 'coin_pouch')

    def minus_coin(self):
        self.coins -= 1
        self.config.read('config.ini')
        self.config.set('Coins', 'coin_pouch', str(self.coins))
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    def view_coins(self):
        self.config.read('config.ini')
        self.coins = self.config.getint('Coins', 'coin_pouch')
        print(f"{self.coins} coins in pouch.")
        print()

    def return_coins(self, configCoin):
        self.coins = configCoin
