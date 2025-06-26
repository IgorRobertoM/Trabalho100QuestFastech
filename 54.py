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

transposta = []

for j in range(colunas):
    nova_linha = []
    for i in range(linhas):
        nova_linha.append(matriz[i][j])  
    transposta.append(nova_linha)

print("\nMatriz transposta:")
for linha in transposta:
    print(linha)