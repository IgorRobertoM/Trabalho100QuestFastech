intervalo1 = 0 
intervalo2 = 0 
intervalo3 = 0 
intervalo4 = 0 

while True:
    numero = int(input("Digite um número positivo (ou um número negativo para sair): "))
    
    if numero < 0:
        break

    if 0 <= numero <= 25:
        intervalo1 += 1
    elif 26 <= numero <= 50:
        intervalo2 += 1
    elif 51 <= numero <= 75:
        intervalo3 += 1
    elif 76 <= numero <= 100:
        intervalo4 += 1

print("\nQuantidade de números em cada intervalo:")
print("[  0 -  25]:", intervalo1)
print("[ 26 -  50]:", intervalo2)
print("[ 51 -  75]:", intervalo3)
print("[ 76 - 100]:", intervalo4)
