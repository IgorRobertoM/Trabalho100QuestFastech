n = int(input("Digite o número de pessoas: "))

if n <= 0:
    print("Número inválido. Digite um valor maior que zero.")
else:
    soma_idades = 0
    for i in range(n):
        idade = int(input(f"Digite a idade da pessoa {i+1}: "))
        soma_idades += idade

    media = soma_idades / n
    print(f"Média de idade: {media}")

    if 0 <= media <= 25:
        print("A turma é jovem.")
    elif 26 <= media <= 60:
        print("A turma é adulta.")
    elif media > 60:
        print("A turma é idosa.")
    else:
        print("Média inválida.")