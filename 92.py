class ContaBancaria:
    def __init__(self, numero_conta):
        self.numero_conta = numero_conta
        self.saldo = 0.0 

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Erro: saldo insuficiente para o saque.")

conta = ContaBancaria("12345-6")
conta.depositar(200)
conta.sacar(50)
conta.sacar(200)  
print(f"Saldo atual: R${conta.saldo:.2f}")