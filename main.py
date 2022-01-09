from userDatabase import Database
from bank import Bank
from gui import gui

import sqlite3



if __name__ == '__main__':

	u = Database()
	b = Bank()
	g = gui()

	# Shows current user in console
	u.displayData()

	g.MainScreen()



