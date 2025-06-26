n = int(input("Digite quantos termos da série você quer mostrar: "))

soma = 0  
numerador = 1  
denominador = 1  

for i in range(n):
    termo = numerador / denominador
    print(f"{numerador}/{denominador}", end="")

    soma += termo

    numerador += 1
    denominador += 2

    if i < n - 1:
        print(" + ", end="")
    else:
        print()

print("Soma da série:", soma)