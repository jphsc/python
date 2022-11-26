import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'  # a chave secreta deve ser uma string aleatória longa


def get_db_connection():
    try:
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row  # o retorno do banco será igual a um dicionário em python
        return conn
    except Exception as erro:
        print(erro)


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute(f'SELECT * FROM POSTS WHERE ID = {post_id}').fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title or not content:
            flash('Title and content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO POSTS (title, content) VALUES (?, ?)', (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('POST', 'GET'))
def edit(id):
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title or not content:
            flash('Title and content is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE POSTS SET TITLE = ?, CONTENT = ? WHERE ID = ?', (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute(f'DELETE FROM POSTS WHERE ID = {id}')
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))


@app.route('/teste')
def teste():
    return render_template('teste.html')


# Verifica se o arquivo app.py está sendo executado pelo terminal e, caso positivo, iniciamos o servidor do Flask
if __name__ == "__main__":
    app.run()
