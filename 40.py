maior_indice = -1
menor_indice = 999999

cidade_maior = 0
cidade_menor = 0

soma_veiculos = 0
soma_acidentes_cidades_pequenas = 0
quant_cidades_pequenas = 0

for i in range(5):
    print("\nCidade", i+1)

    codigo = int(input("Digite o código da cidade: "))
    veiculos = int(input("Digite o número de veículos de passeio: "))
    acidentes = int(input("Digite o número de acidentes com vítimas: "))

    if acidentes > maior_indice:
        maior_indice = acidentes
        cidade_maior = codigo

    if acidentes < menor_indice:
        menor_indice = acidentes
        cidade_menor = codigo

    soma_veiculos += veiculos

    if veiculos < 2000:
        soma_acidentes_cidades_pequenas += acidentes
        quant_cidades_pequenas += 1

media_veiculos = soma_veiculos / 5

if quant_cidades_pequenas > 0:
    media_acidentes_pequenas = soma_acidentes_cidades_pequenas / quant_cidades_pequenas
else:
    media_acidentes_pequenas = 0

print("\n=== Resultados ===")
print("Maior índice de acidentes:", maior_indice, "- Cidade:", cidade_maior)
print("Menor índice de acidentes:", menor_indice, "- Cidade:", cidade_menor)
print("Média de veículos nas 5 cidades:", media_veiculos)
print("Média de acidentes nas cidades com menos de 2000 veículos:", media_acidentes_pequenas)
