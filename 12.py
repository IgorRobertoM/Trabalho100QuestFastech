num = int(input("Digite um número inteiro entre 1 e 10 para ver a tabuada: "))

if num < 1 or num > 10:
    print("Número inválido. Digite um número entre 1 e 10.")
else:
    print("Tabuada de", num, ":")
    for i in range(1, 11):
        resultado = num * i
        print(num, "X", i, "=", resultado)