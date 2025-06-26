linhas = int(input("Digite o número de linhas da matriz: "))

matriz = []

print("Digite os elementos da matriz, linha por linha:")

for i in range(linhas):
    linha = input(f"Digite os elementos da linha {i} separados por espaço: ").split()
    matriz.append(linha)

colunas_esperadas = len(matriz[0])
todas_linhas_mesmo_tamanho = True

for linha in matriz:
    if len(linha) != colunas_esperadas:
        todas_linhas_mesmo_tamanho = False
        break

e_quadrada = (linhas == colunas_esperadas)

resultado = e_quadrada and todas_linhas_mesmo_tamanho
print(resultado)