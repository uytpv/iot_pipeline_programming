import random
import simpleaudio as sa

class Main:
    def __init__(self):
        self.heads_count = 0
        self.tails_count = 0
        self.coin_sound = sa.WaveObject.from_wave_file('./coin_flip.wav')

        print('Program starting.')
        while True:
            choice = input('Flip coin(y/n)?: ')
            if (choice == 'y') or (choice == 'Y'):
                self.flip_coin()
            elif (choice == 'n') or (choice == 'N'):
                break
            else:
                print('Type \'y\' or \'n\', then enter.')
                print()
        print('Final results')
        print('- heads: ' + str(self.heads_count))
        print('- tails: ' + str(self.tails_count))
        print('Program ending.')

    def flip_coin(self):
        flip_result = random.choice([True, False])
        if flip_result:
            self.heads_count += 1
            print('Heads!')
            print()
        else:
            self.tails_count += 1
            print('Tails!')
            print()
        self.coin_sound.play()

        

if __name__ == '__main__':
    app = Main()

