import getpass              # https://docs.python.org/2/library/getpass.html
import sqlite3
from customErrors import *
# Manage existing users (account balance, withdrawl, deposit)

database_file = 'userDatabase.db'

class Bank:
	def __init__(self):
		self.sqlconnection = sqlite3.connect(database_file)
		self.c = self.sqlconnection.cursor()

	def login(self, username, password):
		""" Return account number and login status"""

		# User credentials
		u = username
		p = password

		query = f"SELECT * FROM users WHERE username=? AND password=?"
		self.c.execute(query,(u,p))
		result = self.c.fetchone()

		if(result):
			print("Login successful!")
			# return the accountNum
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

		self.conn.close() #close out connection
		print("You've logged out!")

		acc = None # reset the accout number
		return acc

	def deposit(self,accountNum,*args,**kwargs):
		# Deposit to balance
		if accountNum == None or 0:
			print("You need to log in!")
		else: # deposit funds

			currentBal = self.balanceView(accountNum) # get current balance

			while True:
				try:
					balance_request = float(input("Please enter your deposit amount: "))

					if balance_request < 0:
						raise ValueTooSmallError

				except ValueError:
					print("Must be a valid number!")
				except ValueTooSmallError as VTSE:
					VTSE.Err_01()

				else:
					print("Request Authorized")

					newBalance = round(currentBal + balance_request,2)

					self.c.execute("UPDATE users SET balance=:balance WHERE accountNum =:accountNum",
						{
							'accountNum':accountNum,
							'balance':newBalance
						})
					print(f"Your new balance is ${newBalance}")
					break

			self.sqlconnection.commit()

	def withdrawl(self,accountNum,*args,**kwargs):
		# Withdrawl from balance
		if accountNum == None or 0:
			print("You need to log in!")
		else: # withdraw funds
			currentBal = self.balanceView(accountNum) # get current balance

			while True:
				try:
					withdrawl_request = float(input("Please enter your withdrawl amount: "))

					if withdrawl_request < 0:
						raise ValueTooSmallError
					if withdrawl_request > currentBal:
						raise ValueTooBigError

				except ValueError:
					print("Must be a valid number!")
				except ValueTooBigError as VTBE:
					VTBE.Err_01()
				except ValueTooSmallError as VTSE:
					VTSE.Err_01()

				else:
					print("Withdrawl successful")

					newBalance = round(currentBal - withdrawl_request,2)

					self.c.execute("UPDATE users SET balance=:balance WHERE accountNum =:accountNum",
						{
							'accountNum':accountNum,
							'balance':newBalance
						})

					print(f"Your new balance is ${newBalance}")
					break

			self.sqlconnection.commit()



	def balanceView(self, accountNum,*args,**kwargs):
		# view current balance
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




