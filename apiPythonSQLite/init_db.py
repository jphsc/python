# importa o sqlite
import sqlite3

# cria o arquivo de banco no diretório informado (nesse caso, na mesma pasta do app.py)
connection = sqlite3.connect('database.db')

# busca a função open, executa o script do parâmetro e renomeia para f a utilização desse método
with open('schema.sql') as f:
    connection.executescript(f.read())

# cria um curso para utilizar métodos do sqlite
cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

# aplica as execuções
connection.commit()
# encerra a conexão
connection.close()