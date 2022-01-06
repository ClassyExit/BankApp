import getpass              # https://docs.python.org/2/library/getpass.html
import sqlite3
# Manage existing users (account balance, withdrawl, deposit)

database_file = 'userDatabase.db'

class Bank:
	def __init__(self):
		self.sqlconnection = sqlite3.connect(database_file)
		self.c = self.sqlconnection.cursor()

	def login(self):
		# User credentialss
		print("LOGIN")
		u = input("Username: ")
		p = getpass.getpass("Passwords:")

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
			return acc[0] # return the account number
		else:
			print("Login failed!")


	def logout(self):

		#close out connection
		self.conn.close()
		print("You've logged out!")

		acc = None # reset the accout number to None
		return acc

	def deposit(self,accountNum,*args,**kwargs):
		# Deposit to balance
		if accountNum == None or 0:
			print("You need to log in!")
		else: # deposit funds

			currentBal = self.balanceView(accountNum) # get current balance

			while True:
				try:
					balance_request = float(input("Please enter your deposit: "))
				except balance_request < 0:
					print("Deposit must be greater than 0!")

				else:
					print("Request Authorized")

					newBalance = currentBal + balance_request

					self.c.execute("UPDATE users SET balance=:balance WHERE accountNum =:accountNum",
						{
							'accountNum':accountNum,
							'balance':newBalance
						})
					print(f"You're new balance is ${newBalance}")
					break

			self.sqlconnection.commit()

	def withdrawl(self):
		# Withdrawl from balance
		pass


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
		return currentBal[0]




