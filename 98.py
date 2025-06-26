valor_para_digitos = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D',
    14: 'E', 15: 'F'
}

def de_decimal(numero, base):
    if numero == 0:
        return "0"

    resultado = []
    while numero > 0:
        resto = numero % base
        resultado.append(valor_para_digitos[resto])
        numero = numero // base

    resultado.reverse()
    return ''.join(resultado)

def encontrar_palindromos_base(lista_numeros_decimais, base):
    lista_palindromos = []

    for numero in lista_numeros_decimais:
        convertido = de_decimal(numero, base)
        if convertido == convertido[::-1]:
            lista_palindromos.append(numero)

    return lista_palindromos