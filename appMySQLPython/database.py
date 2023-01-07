from flask import Flask, render_template, request, flash, redirect, url_for
from flask_cors import CORS
from flaskext.mysql import MySQL
import pymysql
# import mysql.connector
# from mysql.connector import Error

app = Flask(__name__)
CORS(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ionic'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


def get_db_connection():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        return cursor
    except Exception as error:
        print(error)

# def create_db_connection(host_name, user_name, user_password, db_name):
#     conn = None
#     try:
#         conn = mysql.connector.connect(host=host_name, user=user_name, password=user_password, database=db_name)
#         print("MySql Database connection successful")
#     except Error as error:
#         print(f'Error: {error}')
#     return conn
#
#
# def db_connection():
#     connection = create_db_connection('localhost', 'root', '', 'ionic')
#     return connection