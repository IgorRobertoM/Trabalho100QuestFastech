class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def set_idade(self, nova_idade):
        self._idade = nova_idade

p = Pessoa("Ana", 30)

print("Nome:", p.get_nome())
print("Idade:", p.get_idade())

p.set_nome("Carla")
p.set_idade(35)

print("Novo nome:", p.get_nome())
print("Nova idade:", p.get_idade())