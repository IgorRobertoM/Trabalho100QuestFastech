while True:
    nome = input("Nome do atleta (pressione Enter para sair): ")

    if nome == "":
        break

    saltos = []

    for i in range(1, 6):
        salto = float(input(f"Digite a distância do {i}º salto (em metros): "))
        saltos.append(salto)

    print(f"\nAtleta: {nome}")
    print(f"Primeiro Salto: {saltos[0]} m")
    print(f"Segundo Salto: {saltos[1]} m")
    print(f"Terceiro Salto: {saltos[2]} m")
    print(f"Quarto Salto: {saltos[3]} m")
    print(f"Quinto Salto: {saltos[4]} m")

    melhor = max(saltos)
    pior = min(saltos)

    saltos.remove(melhor)
    saltos.remove(pior)
    media = sum(saltos) / len(saltos)

    print(f"\nMelhor salto: {melhor} m")
    print(f"Pior salto: {pior} m")
    print(f"Média dos demais saltos: {media:.1f} m")

    print("\nResultado final:")
    print(f"{nome}: {media:.1f} m\n")
