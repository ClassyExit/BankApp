import PySimpleGUI as sg
from bank import Bank

# User interface

MainScreenTheme = 'DarkBlue'


class gui(Bank):
	def __init__(self):
		Bank.__init__(self)

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
				break

			# Create new account
			elif event == 'Create Account':
				sg.PopupAutoClose("Redirecting...", auto_close_duration=1)

				window.close()
				# Create user
				self.createUser()

			#User has inputted both username and password
			else:
				input_username = values[0]
				input_password = values[1]
				# return input_username, input_password

				self.acc_number, self.log_status = Bank.login(self,input_username,input_password)

				if self.log_status == True:
					sg.Popup("Login successful!")
					window.close()

					# Run log in window
					self.loggedIn(self.acc_number)

				else:
					sg.Popup("Login Failed!")

	def createUser(self):
		""" Screen to create new user"""
		print("creating user now!")




	def loggedIn(self, accountNum):
		"""Screen for when the user has logged in"""

		pass

