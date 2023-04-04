
class CoinPouch:
    def __init__(self, configCoin):
        self.coins = configCoin
    
    def minus_coin(self):
        self.coins -= 1

    def view_coins(self):
        print(f"{self.coins} coin(s) in coin pouch.")

    def return_coins(self, configCoin):
        self.coins = configCoin