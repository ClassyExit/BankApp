import getpass              # https://docs.python.org/2/library/getpass.html
import sqlite3
from customErrors import *
# Manage existing users (account balance, withdrawl, deposit)

database_file = 'userDatabase.db'

class Bank:
	def __init__(self):
		# Connect to database
		self.sqlconnection = sqlite3.connect(database_file)
		self.c = self.sqlconnection.cursor()

	def login(self, username, password):
		"""Allow user to log into their account"""

		# User credentials
		u = username
		p = password

		query = f"SELECT * FROM users WHERE username=? AND password=?"
		self.c.execute(query,(u,p))
		result = self.c.fetchone()

		if(result):
			print("Login successful!")
			# find the users account Number
			self.c.execute("SELECT accountNum FROM users WHERE username = :username and password = :password",
						{
						'username':u,
						'password':p
						})

			acc = self.c.fetchone()
			return acc[0], True # return the account number
		else:
			print("Login failed!")
			return None, False


	def logout(self):
		"""Allow user to log out from their account"""
		self.conn.close() #close out connection
		print("You've logged out!")

		acc = None # reset the accout number
		return acc

	def deposit(self,accountNum,depositAmount,*args,**kwargs):
		"""Allow the user to deposit funds into their accounts"""

		if accountNum == None or 0:
			print("You need to log in!")
		else: # deposit funds

			currentBal = self.balanceView(accountNum) # get current balance

			while True:
				try:
					balance_request = float(depositAmount)

					if balance_request < 0:
						raise ValueTooSmallError

				except ValueError:
					print("Must be a valid number!")
					return 'Must be a valid number!'

				except ValueTooSmallError as VTSE:
					err = VTSE.Err_01()
					return err


				else:
					print("Request Authorized")

					newBalance = round(currentBal + balance_request,2)

					self.c.execute("UPDATE users SET balance=:balance WHERE accountNum =:accountNum",
						{
							'accountNum':accountNum,
							'balance':newBalance
						})

					print(f"Your new balance is ${newBalance}")

					self.sqlconnection.commit()
					return True



	def withdrawl(self,accountNum,withdrawlAmount,*args,**kwargs):
		"""Allow user to withdraw from their account"""

		if accountNum == None or 0:
			print("You need to log in!")
		else: # withdraw funds
			currentBal = self.balanceView(accountNum) # get current balance

			while True:
				try:
					withdrawl_request = float(withdrawlAmount)

					if withdrawl_request < 0:
						raise ValueTooSmallError
					if withdrawl_request > currentBal:
						raise ValueTooBigError

				except ValueError:
					err = 'Must be a valid number!'
					return err
				except ValueTooBigError as VTBE:
					err = VTBE.Err_01()
					return err
				except ValueTooSmallError as VTSE:
					err = VTSE.Err_01()
					return err

				else:
					print("Withdrawl successful")

					newBalance = round(currentBal - withdrawl_request,2)

					self.c.execute("UPDATE users SET balance=:balance WHERE accountNum =:accountNum",
						{
							'accountNum':accountNum,
							'balance':newBalance
						})

					print(f"Your new balance is ${newBalance}")
					self.sqlconnection.commit()
					return True


	def balanceView(self, accountNum,*args,**kwargs):
		"""Allow user to see their account balance"""
		if ("username" and "password") in kwargs:
			self.c.execute("SELECT balance FROM users WHERE username = :username and password = :password",
						{
						'username':kwargs["username"],
						'password':kwargs["password"]
						})

		else:
			self.c.execute("SELECT balance FROM users WHERE accountNum = :accountNum", {'accountNum':accountNum})

		currentBal = self.c.fetchone()
		return round(currentBal[0],2)




