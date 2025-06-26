numero = input("Digite um número inteiro positivo: ")

if numero.isdigit():
    numero_invertido = numero[::-1]
    print("Número invertido:", numero_invertido)
else:
    print("Você não digitou um número inteiro positivo.")