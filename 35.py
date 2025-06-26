limite = int(input("Digite um número inteiro: "))

if limite < 2:
    print("Não existem números primos nesse intervalo.")
else:
    print(f"Números primos entre 1 e {limite}:")
    for num in range(2, limite + 1):
        eh_primo = True
        for i in range(2, num):
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            print(num)
