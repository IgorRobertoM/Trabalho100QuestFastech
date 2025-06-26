N = int(input("Quantos números você deseja informar? "))

if N <= 0:
    print("Número inválido. Informe um valor maior que zero.")
else:
    menor = None
    maior = None
    soma = 0

    for i in range(N):
        while True:
            num = float(input(f"Digite o {i+1}º número (entre 0 e 1000): "))
            if 0 <= num <= 1000:
                break
            else:
                print("Número inválido! Digite um número entre 0 e 1000.")

        soma += num
        if menor is None or num < menor:
            menor = num
        if maior is None or num > maior:
            maior = num

    print(f"Menor valor: {menor}")
    print(f"Maior valor: {maior}")
    print(f"Soma dos valores: {soma}")