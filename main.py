from userDatabase import Database
from bank import Bank
from gui import gui




if __name__ == '__main__':

	u = Database()
	b = Bank()
	g = gui()

	# Shows current user in database in console
	u.displayData()

	g.MainScreen()



