base = int(input("Digite a base (número inteiro): "))
expoente = int(input("Digite o expoente (número inteiro não negativo): "))

if expoente < 0:
    print("Expoente deve ser um número inteiro não negativo.")
else:
    resultado = 1
    for _ in range(expoente):
        resultado = resultado * base
    
    print(f"{base} elevado a {expoente} é {resultado}")