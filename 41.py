valor_divida = float(input("Digite o valor da dívida: R$ "))

parcelas_juros = [
    (1, 0),
    (3, 10),
    (6, 15),
    (9, 20),
    (12, 25)
]

print("\nValor da Dívida  Valor dos Juros  Quantidade de Parcelas  Valor da Parcela")


for parcelas, juros in parcelas_juros:
    
    valor_juros = valor_divida * (juros / 100)
    
    valor_total = valor_divida + valor_juros
    
    valor_parcela = valor_total / parcelas

    print(f"R$ {valor_total:10.2f}  R$ {valor_juros:10.2f}  {parcelas:^22}  R$ {valor_parcela:10.2f}")