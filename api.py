import mysql.connector
from mysql.connector import errorcode
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
# import requests

app = Flask(__name__)
api = Api(app)

try:
    # db_connection = mysql.connector.connect(host="sql202.epizy.com", user="epiz_32641348", password="cHJc2poSCBs", database="epiz_32641348_ionic")
    db_connection = mysql.connector.connect(host="localhost", user="root", password="",
                                            database="appMySql")
    cursor = db_connection.cursor()
    print("Database connection made!")
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User name or password is wrong")
    else:
        print(error)

# # Parâmetros da requisição
# url = "http://localhost/apiAppMysql/api.php",
# params = { "requisicao": "listar", "nome": "", "limit": 15, "start": 0 }
# headers = {"Content-Type": "application/json", "Access-control-Allow-Origin": "*", ""}
#
# #requisição
# request = requests.get(url, params, headers)

def get(self):
    query = cursor.execute("SELECT * FROM USUARIOS")
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
    return jsonify(result)

class UserById(Resource):
    def get(self, id):
        conn = db_connection.connect()
        query = conn.execute("SELECT * FROM USUARIOS WHERE ID =%d " % int(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

api.add_resource(UserById, '/users/<id>')

if __name__ == '__main__':
    app.run()

res = get()
print(res)


# cursor.close()
# db_connection.commit()
# db_connection.close()