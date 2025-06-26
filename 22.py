num = int(input("Digite um número inteiro: "))

if num <= 1:
    print(f"{num} não é um número primo.")
else:
    divisores = []
    for i in range(2, num):
        if num % i == 0:
            divisores.append(i)

    if len(divisores) == 0:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é primo. É divisível por:", end=" ")
        print(", ".join(str(d) for d in divisores))