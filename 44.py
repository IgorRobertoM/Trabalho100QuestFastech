print("==== Candidatos ====")
print("1 - José")
print("2 - João")
print("3 - Maria")
print("4 - Ana")
print("5 - Voto Nulo")
print("6 - Voto em Branco")
print("0 - Encerrar votação\n")

votos_1 = 0
votos_2 = 0
votos_3 = 0
votos_4 = 0
votos_nulo = 0
votos_branco = 0
total_votos = 0

while True:
    voto = int(input("Digite o código do voto (0 para encerrar): "))
    
    if voto == 0:
        break

    if voto == 1:
        votos_1 += 1
    elif voto == 2:
        votos_2 += 1
    elif voto == 3:
        votos_3 += 1
    elif voto == 4:
        votos_4 += 1
    elif voto == 5:
        votos_nulo += 1
    elif voto == 6:
        votos_branco += 1
    else:
        print("Código inválido. Tente novamente.")
        continue

    total_votos += 1

if total_votos > 0:
    perc_nulo = (votos_nulo / total_votos) * 100
    perc_branco = (votos_branco / total_votos) * 100
else:
    perc_nulo = 0
    perc_branco = 0

print("\n===== Resultado da Votação =====")
print(f"José (1): {votos_1} votos")
print(f"João (2): {votos_2} votos")
print(f"Maria (3): {votos_3} votos")
print(f"Ana (4): {votos_4} votos")
print(f"Votos nulos: {votos_nulo}")
print(f"Votos em branco: {votos_branco}")
print(f"Percentual de votos nulos: {perc_nulo:.2f}%")
print(f"Percentual de votos em branco: {perc_branco:.2f}%")