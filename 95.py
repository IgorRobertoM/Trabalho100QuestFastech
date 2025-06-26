digitos_para_valor = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

valor_para_digitos = {v: k for k, v in digitos_para_valor.items()}


def para_decimal(numero_str, base_origem):
    numero_str = numero_str.upper()
    decimal = 0
    potencia = 0

    for digito in reversed(numero_str):
        valor = digitos_para_valor[digito]
        decimal += valor * (base_origem ** potencia)
        potencia += 1

    return decimal


def de_decimal(decimal, base_destino):
    if decimal == 0:
        return "0"

    restos = []
    while decimal > 0:
        resto = decimal % base_destino
        restos.append(valor_para_digitos[resto])
        decimal //= base_destino

    restos.reverse()
    return ''.join(restos)


def converter_base(numero_str, base_origem, base_destino):
    decimal = para_decimal(numero_str, base_origem)
    convertido = de_decimal(decimal, base_destino)
    return convertido

print(converter_base("1A", 16, 10)) 
print(converter_base("1010", 2, 16))
print(converter_base("255", 10, 2)) 