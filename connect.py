import mysql.connector
from mysql.connector import errorcode

try:
	db_connection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='appMySql')
	# db_connection = mysql.connector.connect(host, user, password)
	print("Database connection made!")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database doesn't exist")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("User name or password is wrong")
	else:
		print(error)
else:
	db_connection.close()

'''
#O mesmo que o de cima só que sem o erro
from mysql.connector import (connection)
db_connection = connection.MySQLConnection(host='127.0.0.1', user='root', password='', database='bd')
db_connection.close()
'''