N = int(input("Digite a quantidade de notas: "))

if N <= 0:
    print("Quantidade inválida. Digite um número maior que zero.")
else:
    soma = 0
    for i in range(N):
        nota = float(input(f"Digite a nota {i+1}: "))
        soma += nota
    media = soma / N
    print(f"A média aritmética das notas é: {media}")