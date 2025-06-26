linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = i * j  
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz gerada:")
for linha in matriz:
    print(linha)