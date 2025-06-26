def desenhar_triangulo(altura, tipo):
    if tipo == 'esquerda':
        for i in range(1, altura + 1):
            print("*" * i)

    elif tipo == 'direita':
        for i in range(1, altura + 1):
            espacos = " " * (altura - i)
            estrelas = "*" * i
            print(espacos + estrelas)

    elif tipo == 'centralizado':
        for i in range(1, altura + 1):
            espacos = " " * (altura - i)
            estrelas = "*" * (2 * i - 1)
            print(espacos + estrelas)
    else:
        print("Tipo inválido. Use: 'esquerda', 'direita' ou 'centralizado'.")

print("Triângulo à esquerda:")
desenhar_triangulo(5, 'esquerda')

print("\nTriângulo à direita:")
desenhar_triangulo(5, 'direita')

print("\nTriângulo centralizado:")
desenhar_triangulo(5, 'centralizado')