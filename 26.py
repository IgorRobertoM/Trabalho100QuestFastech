total_eleitores = int(input("Digite o número total de eleitores: "))

if total_eleitores <= 0:
    print("Número inválido. Digite um valor maior que zero.")
else:
    votos1 = 0
    votos2 = 0
    votos3 = 0

    for i in range(total_eleitores):
        print("\nCandidatos: 1, 2 ou 3")
        voto = int(input(f"Eleitor {i+1}, digite o número do seu candidato: "))
        
        if voto == 1:
            votos1 += 1
        elif voto == 2:
            votos2 += 1
        elif voto == 3:
            votos3 += 1
        else:
            print("Voto inválido!")

    print("\nResultado da eleição:")
    print(f"Candidato 1: {votos1} voto(s)")
    print(f"Candidato 2: {votos2} voto(s)")
    print(f"Candidato 3: {votos3} voto(s)")