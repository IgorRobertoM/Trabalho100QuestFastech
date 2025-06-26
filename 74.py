def calcular_fatorial_iterativo(numero):
    if numero < 0:
        return "Erro: fatorial não existe para números negativos."
    
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado

print(calcular_fatorial_iterativo(5))  
print(calcular_fatorial_iterativo(0))  
print(calcular_fatorial_iterativo(-2)) 