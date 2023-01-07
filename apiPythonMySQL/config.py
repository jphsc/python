from app import app
from flaskext.mysql import MySQL
# import mysql.connector

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ionic'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


# db_connection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='rest_api')
# cursor = db_connection.cursor()
#
# arrayDatabases = []
#
# cursor.execute("SHOW DATABASES")
# for db in cursor:
#     arrayDatabases.append(db)
#
# databases = list(arrayDatabases)
# print(databases)