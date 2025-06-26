linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matriz = []

print("Digite os elementos da matriz:")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

maior = matriz[0][0]
menor = matriz[0][0]

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        if matriz[i][j] < menor:
            menor = matriz[i][j]

print("\nMaior elemento da matriz:", maior)
print("Menor elemento da matriz:", menor)