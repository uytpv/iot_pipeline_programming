import simpleaudio as sa

class VendingMachine:
    def __init__(self):
        self.coins = 0
    
    def insert_coin(self):
        self.coins += 1
        self.play_sound("./insert_coin.wav")
    
    def view_coins(self):
        print(f"{self.coins} coin(s) in vending machine.")
    
    def return_coins(self):
        self.coins = 0
        self.play_sound("coin_land.wav")
    
    def play_sound(self, filename):
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()
