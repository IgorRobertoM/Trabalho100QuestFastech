preco_pao = float(input("Digite o preço do pão: R$ "))

print("\nPanificadora Pão de Ontem - Tabela de preços")
for i in range(1, 51):
    valor = i * preco_pao
    print(f"{i} - R$ {valor:.2f}")