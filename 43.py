print("===== Cardápio =====")
print("100 - Cachorro Quente - R$ 1,20")
print("101 - Bauru Simples   - R$ 1,30")
print("102 - Bauru com Ovo   - R$ 1,50")
print("103 - Hambúrguer      - R$ 1,20")
print("104 - Cheeseburguer   - R$ 1,30")
print("105 - Refrigerante    - R$ 1,00")
print("Digite 0 para encerrar o pedido.\n")

cardapio = {
    100: 1.20,
    101: 1.30,
    102: 1.50,
    103: 1.20,
    104: 1.30,
    105: 1.00
}

total = 0

while True:
    codigo = int(input("Digite o código do item (ou 0 para encerrar): "))

    if codigo == 0:
        break

    if codigo in cardapio:
        quantidade = int(input("Digite a quantidade: "))
        preco = cardapio[codigo]
        valor = preco * quantidade
        print(f"Item: {codigo} | Quantidade: {quantidade} | Valor: R$ {valor:.2f}")
        total += valor
    else:
        print("Código inválido. Tente novamente.")

print(f"\nTotal a pagar: R$ {total:.2f}")
print("Obrigado pela compra!")