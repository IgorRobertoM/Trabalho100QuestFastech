class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

meu_cachorro = Cachorro("Rex", 5)
print("Nome:", meu_cachorro.nome)
print("Idade:", meu_cachorro.idade)