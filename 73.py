def filtrar_numeros(lista, tipo):
    resultado = []

    if tipo == 'pares':
        for numero in lista:
            if numero % 2 == 0:
                resultado.append(numero)

    elif tipo == 'impares':
        for numero in lista:
            if numero % 2 != 0:
                resultado.append(numero)

    elif tipo == 'positivos':
        for numero in lista:
            if numero > 0:
                resultado.append(numero)

    elif tipo == 'negativos':
        for numero in lista:
            if numero < 0:
                resultado.append(numero)

    else:
        return []

    return resultado

numeros = [1, -2, 3, 4, -5, 0, -1, 8]

print(filtrar_numeros(numeros, 'pares'))      
print(filtrar_numeros(numeros, 'impares'))    
print(filtrar_numeros(numeros, 'positivos'))  
print(filtrar_numeros(numeros, 'negativos'))  
print(filtrar_numeros(numeros, 'primos'))     