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

elemento = int(input("\nDigite o número que deseja contar na matriz: "))

contador = 0
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] == elemento:
            contador += 1

print(f"\nO número {elemento} aparece {contador} vez(es) na matriz.")