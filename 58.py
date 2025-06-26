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

print("\nMatriz original:")
for linha in matriz:
    print(linha)

matriz_invertida = []

for i in range(linhas - 1, -1, -1): 
    matriz_invertida.append(matriz[i])

print("\nMatriz com linhas invertidas:")
for linha in matriz_invertida:
    print(linha)