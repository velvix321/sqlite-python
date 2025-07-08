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


def salvar_usuario(usuario):
        cursor.execute("insert into usuarios(nome, idade) values (?, ?)", (usuario.nome, usuario.idade)) 
        conexao.commit()

def lista_usuarios():
        cursor.execute("select * from usuarios")
        retu
conexao.close()
