N = int(input("Digite um número inteiro maior que 1: "))

if N <= 1:
    print("Número inválido. Digite um número maior que 1.")
else:
    total_divisoes = 0
    print(f"Números primos entre 1 e {N}:")

    for num in range(2, N + 1):
        primo = True
        for i in range(2, num):
            total_divisoes += 1
            if num % i == 0:
                primo = False
                break
        if primo:
            print(num)

    print(f"Número total de divisões executadas: {total_divisoes}")