import configparser
import simpleaudio as sa


class VendingMachine:
    config = configparser.ConfigParser()

    def __init__(self):
        self.config.read('config.ini')
        self.coins = self.config.getint('Coins', 'inserted_coins')

    def insert_coin(self):
        self.coins += 1
        self.config.read('config.ini')
        self.config.set('Coins', 'inserted_coins', str(self.coins))
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
        self.play_sound('./insert_coin.wav')
        print()

    def view_coins(self):
        self.config.read('config.ini')
        self.coins = self.config.getint('Coins', 'inserted_coins')
        print(f'{self.coins} coin(s) in vending machine.')
        print()

    def return_coins(self):
        self.config.read('config.ini')

        c_coin_pouch = self.config.getint('Coins', 'coin_pouch')
        c_coin_inserted = self.config.getint('Coins', 'inserted_coins')

        self.config.set('Coins', 'coin_pouch', str(c_coin_pouch + self.coins))
        self.config.set('Coins', 'inserted_coins',
                        str(c_coin_inserted - self.coins))

        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
        self.play_sound('./coin_land.wav')
        print()

    def play_sound(self, filename):
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()
