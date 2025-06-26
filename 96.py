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
        if digito not in digitos_para_valor or digitos_para_valor[digito] >= base_origem:
            raise ValueError(f"Dígito inválido '{digito}' para a base {base_origem}")
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

def somar_em_bases(lista_numeros, base_origem, base_destino):
    soma_decimal = 0

    for num_str in lista_numeros:
        try:
            valor = para_decimal(num_str, base_origem)
            soma_decimal += valor
        except ValueError as erro:
            print(f"Erro ao converter '{num_str}': {erro}")

    return de_decimal(soma_decimal, base_destino)

numeros = ["A", "F", "1G", "3"] 
resultado = somar_em_bases(numeros, base_origem=16, base_destino=2)
print("Resultado final na base 2:", resultado)
