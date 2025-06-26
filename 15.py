n = int(input("Digite quantos termos da série de Fibonacci deseja gerar: "))

a, b = 1, 1

if n <= 0:
    print("Digite um número maior que zero.")
else:
    print("Série de Fibonacci:")
    for i in range(n):
        print(a)
        a, b = b, a + b