n = int(input("Digite o tamanho da matriz (ex: 3 para 3x3): "))

matriz = []

print("Digite os elementos da matriz linha por linha:")
for i in range(n):
    linha = []  
    for j in range(n):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

soma_principal = 0
soma_secundaria = 0

for i in range(n):
    soma_principal += matriz[i][i]                 
    soma_secundaria += matriz[i][n - 1 - i]        

print("\nSoma da diagonal principal:", soma_principal)
print("Soma da diagonal secundária:", soma_secundaria)