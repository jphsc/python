import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key' # a chave secreta deve ser uma string aleatória longa

def get_db_connection():
    try:
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row # o retorno do banco será igual a um dicionário em python
        return conn
    except Exception as erro:
        print(erro)

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute("SELECT * FROM POSTS WHERE ID = ?", (post_id)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def index():
    conn = get_db_connection()
    # cursor = conn.cursor()
    posts = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    return render_template('create.html')

@app.route('/teste')
def teste():
    return render_template('teste.html')

# Verifica se o arquivo app.py está sendo executado pelo terminal e, caso positivo, iniciamos o servidor do Flask
if __name__ == "__main__":
    app.run()