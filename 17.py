num = int(input("Digite um número inteiro não negativo para calcular o fatorial: "))

if num < 0:
    print("Número inválido! Digite um número inteiro não negativo.")
elif num == 0 or num == 1:
    print(f"{num}! = 1")
else:
    fatorial = 1
    expressao = ""
    for i in range(num, 0, -1):
        fatorial *= i
        expressao += str(i)
        if i != 1:
            expressao += "."
    print(f"{num}! = {expressao} = {fatorial}")