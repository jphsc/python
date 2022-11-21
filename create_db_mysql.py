import mysql.connector
from mysql.connector import errorcode

# Nome da base de dados do projeto
db_name = ('rest_api',)

# Cria conexão com o servidor
db_connection = mysql.connector.connect(host='127.0.0.1', user='root', password='')
cursor_createdb = db_connection.cursor()

# variáveis de validação de existência de base
arrayDatabases = []
thereDatabase = False

# Retorna bases existentes
cursor_createdb.execute("SHOW DATABASES")
for db in cursor_createdb:
    arrayDatabases.append(db)

databases = list(arrayDatabases)

if db_name in databases:
    thereDatabase = True
else:
    thereDatabase = False

# Converte nome da base de dados de tupla para string
db_name = ''.join(db_name)

# Se base não existe, cria base
if thereDatabase:
    print("A base já existe")
else:
    try:
        cursor_createdb.execute(f"CREATE DATABASE {db_name}")
        cursor_newdb = db_connection.cursor()
        print("Base criada")
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("User name or password is wrong")
        else:
            print(error)


# Cria conexão com a base criada ou já existente
db_connection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database=db_name)

# # caso queira excluir uma base
# try:
#     cc = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='AAA')
#     DD = cc.cursor()
#     DD.execute("DROP DATABASE AAA")
# except mysql.connector.Error as error:
#     print(error)