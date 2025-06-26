num = int(input("Digite um número inteiro: "))

if num <= 1:
    print(f"{num} não é primo.")
else:
    eh_primo = True
    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(f"{num} é primo.")
    else:
        print(f"{num} não é primo.")