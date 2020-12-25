# File to maintain user data and login credentials
import csv, os, datetime

#TODO: Add account generation
#TODO: Add login validation
#TODO: Add account number generation

class User:
    def __init__(self):
        pass

    # Add new user
    def newUser(self):
        # Add new user data
        newUser = {'name':"", 'pin': 0, 'account_number': 0, 'account_balance': 0}
        newUser['name'] = input(print("Enter your name: "))
        newUser['pin'] = int(input(print("Enter a pin: ")))
        newUser['account_number'] = 111111111 #TODO: Generate account number
        newUser['account_balance'] = 0


        # Add user data to csv file
        with open('users.csv', 'a', newline='') as file:
            # names which data is sorted in csv file
            fieldnames = ['name', 'pin', 'account_number', 'account_balance']
            # writes to the file using the fieldnames
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writerow(
                {'name': newUser['name'], 'pin': newUser['pin'], 'account_number': newUser['account_number'],
                 'account_balance': newUser['account_balance']})

        with open('backlog.txt', 'a') as backlog:
            backlog.write(f"\nNew User created: Username: {newUser['name']}, account number: {newUser['account_number']}"
                          f" on " + str(datetime.datetime.today()))



    # Check to see if user has account
    def checkUserName(self, name):
        with open('users.csv', 'r') as file:
            csv_reader = csv.DictReader(file)

            # Cycle through csv file to check if name exist. Return True if exist, else False
            for line in file:
                namefind = line['name']
                if namefind == name:
                    return True

    # Processes users login
    def validateLogin(self):
        # User enter username + password
        print("Please sign-in using your login information.")
        name = input(print("Enter your name: "))
        user_pin = int(input(print("Enter your pin: ")))

        # Find user + password in csv file
        with open('users.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # Cycle the users list to find users password
            for line in csv_reader:
                name_find = line['name']

                if name_find == name:
                    name_found = line['name']
                    pin_found = line['pin']
                    account_number = line['account_number']

        # Compares information
        if str(name) == str(name_found) and str(user_pin) == str(pin_found):
            # login successful
            print(f"Login Successful. Welcome {name}.\nAccount number: " + str(account_number))
            login = True

            #open backlog to track
            with open('backlog.txt','a') as file:
                file.write("\n"+str(name) + " ("+str(account_number) + ") has successfully logged in at " + str(datetime.datetime.today()))

        # Login Failed
        else:
            login = False
            print("Invalid login. Please try again.")
            with open('backlog.txt', 'a') as file:
                file.write("\nUser know as " + name + " has attempted to log in but was unsuccessful at " + str(
                    datetime.datetime.today()))
        # login = True: success login. login = False: Invalid
        return login