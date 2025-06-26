while True:
    while True:
        pop_a = int(input("Digite a população do país A (maior que 0): "))
        pop_b = int(input("Digite a população do país B (maior que 0): "))
        if pop_a > 0 and pop_b > 0:
            break
        else:
            print("As populações devem ser maiores que 0. Tente novamente.")

    while True:
        taxa_a = float(input("Digite a taxa de crescimento de A (em % positivo): "))
        taxa_b = float(input("Digite a taxa de crescimento de B (em % positivo): "))
        if taxa_a > 0 and taxa_b > 0:
            break
        else:
            print("As taxas devem ser maiores que 0. Tente novamente.")

    taxa_a = taxa_a / 100
    taxa_b = taxa_b / 100

    anos = 0

    while pop_a < pop_b:
        pop_a = pop_a + (pop_a * taxa_a)
        pop_b = pop_b + (pop_b * taxa_b)
        anos = anos + 1

    print("\nResultados:")
    print("Número de anos para a população de A ultrapassar ou igualar a de B:", anos)
    print("População final de A:", int(pop_a))
    print("População final de B:", int(pop_b))

    repetir = input("\nDeseja realizar outra simulação? (s/n): ")
    if repetir.lower() != 's':
        break