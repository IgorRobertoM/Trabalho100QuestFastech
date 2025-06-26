num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 < num2:
    inicio = num1 + 1
    fim = num2
else:
    inicio = num2 + 1
    fim = num1

soma = 0

print("Números no intervalo:")
for i in range(inicio, fim):
    print(i)
    soma = soma + i

print("Soma dos números no intervalo:", soma)