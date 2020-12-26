# Bank App
import csv
from os import path
from manageUsers import User

# TODO:
# Setup main loop
# Setup bank accounts

class bankAccount:
    #Runs when class is called
    def __init__(self):
        pass

    def deposit(self, user_name, accountNum):
        # deposit function for the user
        pass


    def withdrawl(self, user_name, accountNum):
        # withdrawl function for the user
        pass

    def transaction(self, username, accountNum):
        # Add a backlog of all transactions that occur
        pass


# Initializes file
def fileCheck():
    # Checks to see if file exists
    if path.exists('users.csv') == True:
        pass
    elif path.exists('users.csv') == False:
        with open('users.csv', 'w', newline='') as f:
            f.seek(0)
            fieldnames = ['name', 'pin', 'account_number', 'account_balance']
            csv_file = csv.DictWriter(f, fieldnames)
            csv_file.writeheader()
            print("Users file created.")


def mainScreen():
    while True:
        x = int(input(print('Press 1 to login \nPress 2 to Create New Account')))
        if x == 1:
            # run login
            valid, name, accountNumber = User.validateLogin(self=User)

            # TODO: Sign into bank if valid == True

        elif x == 2:
            # Run new account creation
            User.newUser(self=User)

            
if __name__ == '__main__':
    fileCheck()

    while True:
        mainScreen()


