import sys
from main_menu import MainMenu
from db_conn import Database


class Main:

    database: Database
    print('Program starting.')

    def __init__(self) -> None:
        # 1- init
        # 0-
        if len(sys.argv) == 5 and (sys.argv[1] == '-u' or sys.argv[1] == '--username') and (sys.argv[3] == '-p' or sys.argv[3] == '--password'):
            # authenticate user
            username = sys.argv[2]
            password = sys.argv[4]
            if self.authenticateUser(username, password):
                # show sales data
                self.showSaleData()

                print()
                print('Program ending.')
            else:
                print("Authentication failed. Please try again.")
        else:
            main_menu = MainMenu()
            # 2- run
            main_menu.showMenu()
            # 3- clean
        return None

    def authenticateUser(self, username: str, password: str) -> bool:
        # check if the username and password match the admin credentials
        if username == "admin" and password == "1234":
            return True
        else:
            return False

    def showSaleData(self) -> None:
        self.database = Database()
        MONEY_COLLECTED_STATEMENT = '''SELECT SUM(price) FROM sale;'''
        OPERATING_COSTS_STATEMENT = '''SELECT SUM(cost) FROM sale;'''
        money_colected = self.database.execute(MONEY_COLLECTED_STATEMENT)
        operating_costs = self.database.execute(OPERATING_COSTS_STATEMENT)
        print('Money collected: ' + str(money_colected))
        print('Operating costs: ' + str(operating_costs))
        print('Profit: ' + str(money_colected - operating_costs))
        return None


if __name__ == '__main__':
    app = Main()
