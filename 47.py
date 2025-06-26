while True:
    nome = input("Digite o nome do ginasta (pressione Enter para sair): ")

    if nome == "":
        break

    notas = []

    for i in range(1, 8):
        nota = float(input(f"Nota do jurado {i}: "))
        notas.append(nota)

    print(f"\nAtleta: {nome}")
    for nota in notas:
        print(f"Nota: {nota}")

    melhor = max(notas)
    pior = min(notas)

    notas.remove(melhor)
    notas.remove(pior)
    media = sum(notas) / len(notas)

    print("\nResultado final:")
    print(f"Atleta: {nome}")
    print(f"Melhor nota: {melhor}")
    print(f"Pior nota: {pior}")
    print(f"Média: {media:.2f}\n")