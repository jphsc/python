import mysql.connector
from mysql.connector import errorcode

# host = 'localhost'
# user = 'root'
# password = ''
try:
    db_connection = mysql.connector.connect(host='127.0.0.1', user='root', password='')
    cursor = db_connection.cursor()
    print("Database connection made!")
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User name or password is wrong")
    else:
        print(error)

db_name = ''


cursor.close()
db_connection.commit()
db_connection.close()