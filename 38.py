ano_contratacao = 1995

salario = float(input("Digite o salário inicial do funcionário: "))

aumento = 1.5 / 100
salario += salario * aumento

for ano in range(1997, 2025):  # até 2024
    aumento *= 2
    salario += salario * aumento

print("Salário atual em 2024: R$", round(salario, 2))