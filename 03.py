while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("Erro: o nome deve ter mais de 3 caracteres.")
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 150:
            break
        else:
            print("Erro: a idade deve estar entre 0 e 150.")
    except ValueError:
        print("Erro: digite um número inteiro para a idade.")
while True:
    try:
        salario = float(input("Digite seu salário: "))
        if salario > 0:
            break
        else:
            print("Erro: o salário deve ser maior que zero.")
    except ValueError:
        print("Erro: digite um número válido para o salário.")
while True:
    sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ").lower()
    if sexo in ['f', 'm']:
        break
    else:
        print("Erro: sexo deve ser 'f' ou 'm'.")
while True:
    estado_civil = input("Digite seu estado civil ('s' - solteiro, 'c' - casado, 'v' - viúvo, 'd' - divorciado): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Erro: estado civil deve ser 's', 'c', 'v' ou 'd'.")
print("\nInformações validadas com sucesso:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
estado_dict = {'s': 'Solteiro(a)', 'c': 'Casado(a)', 'v': 'Viúvo(a)', 'd': 'Divorciado(a)'}
print(f"Estado Civil: {estado_dict[estado_civil]}")