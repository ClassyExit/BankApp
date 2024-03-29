import PySimpleGUI as sg
from bank import Bank
from userDatabase import Database

# User interface

MainScreenTheme = 'DarkBlue'
CreateUserTheme = 'DarkBlue'
LoginTheme = 'DarkBlue'

class gui(Bank, Database):
	def __init__(self):
		Bank.__init__(self)
		Database.__init__(self)

	def MainScreen(self):
		"""Login screen. Ask for login information"""
		sg.theme(MainScreenTheme) # Theme (background)

		# Stuff inside window
		layout = [	[sg.Text("Welcome To MyBank")],
					[sg.Text("Username: "),sg.InputText()],
					[sg.Text("Password: "),sg.InputText()],
					[sg.Button("Login"), sg.Button("Create Account")],
					[sg.Button("Exit")]
				]
		# Create the window
		window = sg.Window('Main Screen', layout)

		while True:
			event, values = window.read()

			# Close/Exit window
			if event == sg.WIN_CLOSED or event == 'Exit': # If user exits or closes window
				window.close()
				break

			# Create new account
			elif event == 'Create Account':
				sg.PopupAutoClose("Redirecting...", auto_close_duration=1)

				window.close()
				# Create user
				self.createUsergui()

			#User has inputted both username and password
			else:
				input_username = values[0]
				input_password = values[1]
				# return input_username, input_password

				self.acc_number, self.log_status = Bank.login(self,input_username,input_password)

				if self.log_status == True:
					sg.PopupAutoClose("Login successful!", auto_close_duration=1)
					window.close()

					# Run log in window
					self.loggedIn(self.acc_number)

				else:
					sg.Popup("Login Failed!")

	def createUsergui(self):
		""" Screen to create new user"""
		sg.theme(CreateUserTheme)

		layout = [	[sg.Text("Create Account")],
					[sg.Text("Enter username: "),sg.InputText('',key='username')],
					[sg.Text("Enter password: "),sg.InputText('',key='password')],
					[sg.Button("Create")],
					[sg.Button("Exit")]
				]

		window = sg.Window('NewUser', layout)


		while True:
			event, values = window.read()

			try:
				input_username = values['username']
				input_password = values['password']


				# find if user exists
				user_exist = Database.findUser(self,input_username, input_password)


				# Close/Exit window
				if event == sg.WIN_CLOSED or event == 'Exit': # If user exits or closes window
					window.close()
					self.MainScreen()

				# User exists
				elif user_exist:
					sg.Popup("Account exists!", keep_on_top=True)

				else: # Add user to database

					try:
						Database.createUser(self,input_username,input_password)

					except Exception:
						sg.Popup("There is an Error. Please try again")

					else:
						sg.Popup("Account created! You may log in now.")
						window.close()
						self.MainScreen()
			except TypeError:
				# No input
				break


	def loggedIn(self, accountNum):
		"""Screen for when the user has logged in"""

		accNum = accountNum
		username, balance = Database.getUserInfo(self, accNum)

		sg.theme(LoginTheme)

		layout = [	[sg.Text(f"Welcome {username}")],
					[sg.Text(f"Account Number: {accNum}")],
					[sg.Text(f"Current Balance: ${balance}")],
					[sg.Text("Deposit Amount: "),sg.InputText('',size=(10,1),key='DepositAmount'), sg.Button("Deposit")],
					[sg.Text("Withdrawl Amount: "),sg.InputText('',size=(10,1), key='WithdrawAmount'), sg.Button("Withdraw")],
					[sg.Button("Delete Account")],
					[sg.Button("Logout")]
				]

		window = sg.Window('Account', layout, size=(500,500))

		while True:
			event, values = window.read()

			# If logout or window is closed return to mainscreen
			if event == sg.WIN_CLOSED or event == 'Logout': # If user exits or closes window
				window.close()
				return self.MainScreen()

			# User depositing funds
			if event == 'Deposit':
				# Get deposit amount
				dAmount = values['DepositAmount']
				status = Bank.deposit(self,accNum,dAmount)

				if status == True:
					sg.PopupAutoClose(f"Deposit of ${dAmount} successful!", auto_close_duration=3, title='Transaction')
					window.close()
					return self.loggedIn(accNum)
				else:
					# problem
					sg.PopupAutoClose(f"{status}", auto_close_duration=2, title="Error")

			# User withdrawling funds
			if event == 'Withdraw':
				# Get withdraw amount
				wAmount = values['WithdrawAmount']
				status = Bank.withdrawl(self,accNum,wAmount)

				if status == True:
					sg.PopupAutoClose(f"Withdraw of ${wAmount} successful!", auto_close_duration=3, title='Transaction')
					window.close()
					return self.loggedIn(accNum)
				else:
					# problem
					sg.PopupAutoClose(f"{status}", auto_close_duration=2, title="Error")

			# User is deleting their accounts
			if event == 'Delete Account':
				window.close() # close current window

				layout_delete = [	[sg.Text("Enter your credentials to delete your account")],
									[sg.Text("Enter username: "),sg.InputText('',key='username')],
									[sg.Text("Enter passsword: "),sg.InputText('',key='password')],
									[sg.Button("Confirm Delete")],
									[sg.Button("Back")]
								]


				window = sg.Window('Delete', layout_delete, size=(500,500))

				while True:
					event, values = window.read()

					if event == 'Back' or event == sg.WIN_CLOSED:
						# return to account info screen
						window.close()
						return self.loggedIn(accNum)

					if event == "Confirm Delete":
						u = values['username']
						p = values['password']

						# Confirm the account details
						status = Database.removeUser(self,u,p)

						if status == True:
							# User deleted
							sg.PopupAutoClose("Account Deleted!", auto_close_duration=1)
							window.close()
							return self.MainScreen()
						else:
							sg.PopupAutoClose("Error! Invalid Credentials!", auto_close_duration=1)





