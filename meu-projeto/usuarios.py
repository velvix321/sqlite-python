from banco import salvar_usuarios, lista_usuarios

class usuarios():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def salvar(self):
        salvar_usuarios(self.nome, self.idade)
    
u = usuarios('nair', 26)
u.salvar()

usuarios = lista_usuarios()
for u in usuarios:
    print(u)