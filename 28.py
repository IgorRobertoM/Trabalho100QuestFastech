qtd_cds = int(input("Digite a quantidade de CDs: "))

if qtd_cds <= 0:
    print("Número inválido. Digite um valor maior que zero.")
else:
    total = 0

    for i in range(qtd_cds):
        valor = float(input(f"Digite o valor do CD {i+1}: "))
        total += valor

    media = total / qtd_cds
    print(f"O valor total investido foi: R$ {total:.2f}")
    print(f"O valor médio gasto por CD foi: R$ {media:.2f}")