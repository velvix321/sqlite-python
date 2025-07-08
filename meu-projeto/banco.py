import sqlite3 

conexao = sqlite3.connect("meubanco.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")
conexao.commit()


def salvar_usuarios(nome, idade):
        cursor.execute("INSERT INTO usuarios (nome, idade) values (?, ?)", (nome, idade)) 
        conexao.commit()

def lista_usuarios():
        cursor.execute("select * from usuarios")
        return cursor.fetchall()
