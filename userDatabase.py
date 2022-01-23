# Store user data into database
import sqlite3
import os, os.path
import random
import getpass



database_file = 'userDatabase.db'

class Database:
    def __init__(self):
        #initialize the database
        if os.path.exists(database_file) == False:
            #establish connection with database
            sqlconnection = sqlite3.connect(database_file)

            c = sqlconnection.cursor()

            c.execute("""CREATE TABLE users (
                    username text,
                    accountNum integer,
                    password text,
                    balance real
                    )""")

            sqlconnection.commit()
            sqlconnection.close()
            print("Database created!")

    def displayData(self):
        """Displays the current users in the terminal"""
        
        sqlconnection = sqlite3.connect(database_file)
        c = sqlconnection.cursor()

        c.execute("SELECT * FROM users")
        print(c.fetchall())

        sqlconnection.close()

    def addUser(self,username,accountNum,password,balance):
        """Add a user to the database file"""
        sqlconnection = sqlite3.connect(database_file)
        c = sqlconnection.cursor()

        c.execute("""INSERT INTO users VALUES (:username,:accountNum,:password,:balance)""",
                    {'username':username,
                    'accountNum':accountNum,
                    'password':password,
                    'balance':balance
                    })

        sqlconnection.commit()
        sqlconnection.close()
        print("User added!")

    def removeUser(self,username,password):
        """Removes user from the database file"""
        
        u = username
        p = password

        sqlconnection = sqlite3.connect(database_file)
        c = sqlconnection.cursor()

        query = f"SELECT * FROM users WHERE username=? AND password=?"
        c.execute(query,(u,p))
        result = c.fetchone()
        if(result):
            c.execute("DELETE from users WHERE username = :username and password = :password",
                        {
                        'username':u,
                        'password':p
                        })
            valid = True
        else:
            valid = False

        sqlconnection.commit()
        sqlconnection.close()

        return valid

    def findUser(self, username, password):
        """Finds if a user exists in the database"""
        
        sqlconnection = sqlite3.connect(database_file)
        c = sqlconnection.cursor()

        c.execute("SELECT * FROM users WHERE username = :username AND password = :password", {'username':username, 'password':password})

        result = c.fetchone()

        return bool(result)


    def accNumber(self):
        """Generates a random 9-digit account number"""
        return random.randint(000000000,999999999)


    def createUser(self, username, password,*args,**kwargs):
        """Creates a new user and adds to the database file"""

        self.username = username
        self.password = password
        self.accountNum = self.accNumber()
        self.balance = 0.0

        self.addUser(self.username,self.accountNum,self.password,self.balance)

    def getUserInfo(self, accountNum):
        """Retrieve user data from database file"""
        
        sqlconnection = sqlite3.connect(database_file)
        c = sqlconnection.cursor()

        c.execute("SELECT username, balance FROM users WHERE accountNum = :accountNum", {'accountNum':accountNum})

        result = c.fetchone()

        username = result[0]
        balance = result[1]

        return username, balance






