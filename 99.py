digitos_para_valor = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13,
    'E': 14, 'F': 15
}

valor_para_digitos = {v: k for k, v in digitos_para_valor.items()}

def para_decimal(numero_str, base_origem):
    numero_str = numero_str.upper()
    decimal = 0
    potencia = 0

    for digito in reversed(numero_str):
        if digito not in digitos_para_valor or digitos_para_valor[digito] >= base_origem:
            raise ValueError(f"'{digito}' inválido para base {base_origem}")
        valor = digitos_para_valor[digito]
        decimal += valor * (base_origem ** potencia)
        potencia += 1

    return decimal

def de_decimal(numero, base_destino):
    if numero == 0:
        return '0'

    resultado = []
    while numero > 0:
        resto = numero % base_destino
        resultado.append(valor_para_digitos[resto])
        numero = numero // base_destino

    resultado.reverse()
    return ''.join(resultado)

def realizar_operacao_base(num1_str, num2_str, base_origem, operacao, base_destino):
    try:
        n1 = para_decimal(num1_str, base_origem)
        n2 = para_decimal(num2_str, base_origem)
    except ValueError as erro:
        return f"Erro na conversão: {erro}"

    if operacao == '+':
        resultado = n1 + n2
    elif operacao == '-':
        resultado = n1 - n2
    elif operacao == '*':
        resultado = n1 * n2
    elif operacao == '/':
        if n2 == 0:
            return "Erro: divisão por zero"
        resultado = round(n1 / n2)  
    else:
        return "Erro: operação inválida"

    return de_decimal(abs(resultado), base_destino)

print("Exemplo 1:", realizar_operacao_base("A", "5", 16, '+', 2)) 

print("Exemplo 2:", realizar_operacao_base("101", "10", 2, '*', 10)) 

print("Exemplo 3:", realizar_operacao_base("15", "0", 10, '/', 10)) 

print("Exemplo 4:", realizar_operacao_base("7", "3", 10, '%', 10)) 