from coin_punch import CoinPouch
from  vending_machine import VendingMachine

class Main:
    coin_pouch = CoinPouch()
    vending_machine = VendingMachine()
    
    print("Program starting.")
    
    while True:
        print("Options:")
        print("1) Insert coin")
        print("2) View coins in pouch")
        print("3) View coins in machine")
        print("4) Return coins")
        print("0) Exit")
        choice = input("Your choice: ")
        
        if choice == "1":
            vending_machine.insert_coin()
            coin_pouch.minus_coin()
        elif choice == "2":
            coin_pouch.view_coins()
        elif choice == "3":
            vending_machine.view_coins()
        elif choice == "4":
            vending_machine.return_coins()
            coin_pouch.return_coins()
        elif choice == "0":
            print()
            print("Program ending.")
            break
        else:
            print("Unknown option.")
        
        print()


if __name__ == "__main__":
     app = Main()
