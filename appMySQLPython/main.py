from database import *
from datetime import date as dt
from flask import jsonify
import mysql.connector


@app.route('/')
def home():
    conn = get_db_connection()
    try:
        conn.execute("SELECT * FROM USUARIOS")
        users = tuple(conn)
        conn.close()
        return render_template('home.html', users=users)
    except Exception as erro:
        print(erro)


@app.route('/create', methods=('GET', 'POST'))
def create():
    print('a')
    if request.method == 'POST':
        nome = request.form['name']
        dtnascimento = request.form['dtnascimento']
        idade = request.form['age']
        if not nome or not dtnascimento:
            flash('Nome e idade são obrigatórios')
        else:
            conn = get_db_connection()
            conn.execute(f'INSERT INTO USUARIOS (NOME, DTNASCIMENTO, AGE) VALUES ({nome}, {dtnascimento}, {idade})')
            conn.commit()
            conn.close()
            return redirect(url_for('home'))
    return render_template('create.html')


def age(idade):
    age = idade - dt.today()
    return age


if __name__ == "__main__":
    app.run(debug=True)