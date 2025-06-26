print("===== Cadastro do Gabarito da Prova =====")
gabarito = []
for i in range(1, 11):
    resposta = input(f"Digite a resposta correta da questão {i} (A/B/C/D/E): ").upper()
    gabarito.append(resposta)

maior_acerto = 0
menor_acerto = 10
soma_notas = 0
total_alunos = 0

while True:
    print("\n===== Respostas do Aluno =====")
    respostas_aluno = []
    for i in range(1, 11):
        resposta = input(f"Resposta da questão {i}: ").upper()
        respostas_aluno.append(resposta)

    acertos = 0
    for i in range(10):
        if respostas_aluno[i] == gabarito[i]:
            acertos += 1

    print(f"Você acertou {acertos} questões.")
    total_alunos += 1
    soma_notas += acertos

    if acertos > maior_acerto:
        maior_acerto = acertos
    if acertos < menor_acerto:
        menor_acerto = acertos

    continuar = input("Outro aluno vai utilizar o sistema? (S/N): ").upper()
    if continuar != 'S':
        break

if total_alunos > 0:
    media = soma_notas / total_alunos
else:
    media = 0

print("\n===== Resultado Final =====")
print(f"Total de alunos: {total_alunos}")
print(f"Maior nota: {maior_acerto}")
print(f"Menor nota: {menor_acerto}")
print(f"Média da turma: {media:.2f}")