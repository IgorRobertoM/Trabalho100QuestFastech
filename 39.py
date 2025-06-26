
maior_altura = 0
menor_altura = 999  

aluno_mais_alto = 0
aluno_mais_baixo = 0


for i in range(10):
    numero = int(input("Digite o número do aluno: "))
    altura = float(input("Digite a altura do aluno (em cm): "))

    
    if altura > maior_altura:
        maior_altura = altura
        aluno_mais_alto = numero

    
    if altura < menor_altura:
        menor_altura = altura
        aluno_mais_baixo = numero

print("\nResultado:")
print("Aluno mais alto: número", aluno_mais_alto, "com", maior_altura, "cm")
print("Aluno mais baixo: número", aluno_mais_baixo, "com", menor_altura, "cm")
