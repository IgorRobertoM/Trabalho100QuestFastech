class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        print(f"{self.nome} está latindo!")

meu_cachorro = Cachorro("Rex", 5)
meu_cachorro.latir()  
