mais_alto = 0
codigo_mais_alto = 0
mais_baixo = 0
codigo_mais_baixo = 0
mais_gordo = 0
codigo_mais_gordo = 0
mais_magro = 0
codigo_mais_magro = 0

soma_altura = 0
soma_peso = 0
qtd_clientes = 0

while True:
    codigo = int(input("Código do cliente (0 para encerrar): "))
    if codigo == 0:
        break

    altura = float(input("Altura (m): "))
    peso = float(input("Peso (kg): "))

    if qtd_clientes == 0:
        mais_alto = altura
        codigo_mais_alto = codigo
        mais_baixo = altura
        codigo_mais_baixo = codigo
        mais_gordo = peso
        codigo_mais_gordo = codigo
        mais_magro = peso
        codigo_mais_magro = codigo
    else:
        if altura > mais_alto:
            mais_alto = altura
            codigo_mais_alto = codigo
        if altura < mais_baixo:
            mais_baixo = altura
            codigo_mais_baixo = codigo
        if peso > mais_gordo:
            mais_gordo = peso
            codigo_mais_gordo = codigo
        if peso < mais_magro:
            mais_magro = peso
            codigo_mais_magro = codigo

    soma_altura += altura
    soma_peso += peso
    qtd_clientes += 1

if qtd_clientes == 0:
    print("Nenhum cliente foi informado.")
else:
    media_altura = soma_altura / qtd_clientes
    media_peso = soma_peso / qtd_clientes

    print("\nResultado do censo:")
    print(f"Mais alto: código {codigo_mais_alto}, altura {mais_alto:.2f} m")
    print(f"Mais baixo: código {codigo_mais_baixo}, altura {mais_baixo:.2f} m")
    print(f"Mais gordo: código {codigo_mais_gordo}, peso {mais_gordo:.2f} kg")
    print(f"Mais magro: código {codigo_mais_magro}, peso {mais_magro:.2f} kg")
    print(f"Média das alturas: {media_altura:.2f} m")
    print(f"Média dos pesos: {media_peso:.2f} kg")
