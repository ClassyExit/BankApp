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
		pass
		#close out connection
		# self.conn.close()

	def deposit(self,accountNum,*args,**kwargs):
		# Deposit to balance
		pass

		#GENERAL TEMPLATE
		# with conn:
		#   # do stuff

		#   self.sqlconnection.commit()

	def withdrawl(self):
		# Withdrawl from balance
		pass


	def balanceView(self):
		# view current balance
		pass

	def transaction(self):
		# record transaction details
		pass
