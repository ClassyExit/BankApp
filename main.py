from userDatabase import Database
from bank import Bank
from gui import gui




if __name__ == '__main__':

	u = Database()
	b = Bank()
	g = gui()


	u.displayData()
	# acc = 517597896
	# print(f"ACC:{acc}")

	# username = 'Alex'
	# password = '1234'

	# print(b.balanceView(acc,username=username,password=password))

	# b.deposit(acc)

	# print(b.balanceView(acc,username=username,password=password))

	# b.withdrawl(acc)

	# print(b.balanceView(acc,username=username,password=password))
	g = gui()


	# u,p = g.mainScreen()
	g.MainScreen()




