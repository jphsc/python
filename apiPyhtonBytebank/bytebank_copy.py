from config_bytebank import *
# from flask import jsonify
from flask import flash, request, render_template
import pymysql

def obterTransferencias():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM TRANSFERENCIAS")
        transferencias = tuple(cursor)
        for transferencia in transferencias:
            print(transferencia)
        print('sucesso obter')
        return transferencias
    except Exception as e:
        print(e)
    finally:
        conn.close()


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

data = '2023-01-11'
valor = '100.00'
destino = '1111-2'

# incluirTransferencia(data, valor, destino)
# obterTransferencias()

@app.route('/')
def home():
    incluirTransferencia(data, valor, destino)
    lista = tuple(lista)
    return lista


if __name__ == "__main__":
    app.run(debug=True)