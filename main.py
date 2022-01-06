from userDatabase import *
from bank import *





if __name__ == '__main__':

	u = Database()
	b = Bank()

	conn = sqlite3.connect('userDatabase.db')
	c = conn.cursor()


	u.displayData()
	acc = 517597896
	print(f"ACC:{acc}")

	# c.execute("UPDATE users SET balance = :balance WHERE username = :username", {'username':'Alex', 'balance':1000})
	conn.commit()
	username = 'Alex'
	password = '1234'

	# print(b.balanceView(acc))
	print(b.balanceView(acc,username=username,password=password))
	# a = b.balanceView(acc,username=username,password=password)
	# new = a + 2
	# c.execute("UPDATE users SET balance = :balance WHERE username = :username", {'username':'Alex', 'balance':new})
	# conn.commit()

	b.deposit(acc)

	print(b.balanceView(acc,username=username,password=password))




