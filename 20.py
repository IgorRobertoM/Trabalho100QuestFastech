while True:
    num = int(input("Digite um número inteiro positivo menor que 16 para calcular o fatorial: "))

    if num < 0 or num >= 16:
        print("Número inválido! Digite um número inteiro positivo menor que 16.")
        continue

    fatorial = 1
    expressao = ""
    for i in range(num, 0, -1):
        fatorial *= i
        expressao += str(i)
        if i != 1:
            expressao += "."

    print(f"{num}! = {expressao} = {fatorial}")

    repetir = input("Deseja calcular outro fatorial? (s/n): ").lower()
    if repetir != 's':
        break