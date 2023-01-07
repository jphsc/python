from config_bytebank import *
# from flask import jsonify
from flask import flash, request, render_template
import pymysql
import datetime

def obterTransferencias():
    try:
        conn = get_db_connection()
        conn.execute("SELECT * FROM TRANSFERENCIAS")
        transferencias = tuple(conn)
        conn.close()
        for transferencia in transferencias:
            print(transferencia)
        print('sucesso obter')
        return transferencias
    except Exception as e:
        print(e)

# exemplo de inclusão
# def create():
#     print('a')
#     if request.method == 'POST':
#         nome = request.form['name']
#         dtnascimento = request.form['dtnascimento']
#         idade = request.form['age']
#         if not nome or not dtnascimento:
#             flash('Nome e idade são obrigatórios')
#         else:
#             conn = get_db_connection()
#             conn.execute(f'INSERT INTO USUARIOS (NOME, DTNASCIMENTO, AGE) VALUES ({nome}, {dtnascimento}, {idade})')
#             conn.commit()
#             conn.close()
#             return redirect(url_for('home'))
#     return render_template('create.html')

def incluirTransferencia(data, valor, destino):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # queryInsert = "INSERT INTO TRANSFERENCIAS (DATA, VALOR, DESTINO) VALUES (%s, %.2f, %s)"
        # argumentos = (data, valor, destino)
        # cursor.execute(queryInsert, argumentos)
        cursor.execute(f"INSERT INTO TRANSFERENCIAS (DATA, VALOR, DESTINO) VALUES ({data}, {valor}, {destino})") #, (data, valor, destino))
        conn.commit()
        return print('sucesso ao incluir')
    except Exception as e:
        conn.rollback()
        print(f'Erro: {e}')
    finally:
        conn.close()

data = ('2023-01-11')
valor = '100.00'
destino = '1111-2'

incluirTransferencia(data, valor, destino)
# obterTransferencias()

if __name__ == "__main__":
    app.run(debug=True)