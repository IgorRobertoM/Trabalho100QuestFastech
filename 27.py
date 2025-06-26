qtd_turmas = int(input("Digite a quantidade de turmas: "))

if qtd_turmas <= 0:
    print("Número inválido. Digite um valor maior que zero.")
else:
    soma_alunos = 0

    for i in range(qtd_turmas):
        while True:
            alunos = int(input(f"Digite a quantidade de alunos da turma {i+1} (máximo 40): "))
            if 0 < alunos <= 40:
                break
            else:
                print("Quantidade inválida! A turma deve ter entre 1 e 40 alunos.")
        
        soma_alunos += alunos

    media = soma_alunos / qtd_turmas
    print(f"O número médio de alunos por turma é: {media}")
