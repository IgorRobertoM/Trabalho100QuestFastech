def converter_temperatura(valor, unidade_origem, unidade_destino):
    unidade_origem = unidade_origem.upper()
    unidade_destino = unidade_destino.upper()

    unidades_validas = ['C', 'F', 'K']
    if unidade_origem not in unidades_validas or unidade_destino not in unidades_validas:
        return "Erro: unidade inválida. Use 'C', 'F' ou 'K'."

    if unidade_origem == unidade_destino:
        return valor

    if unidade_origem == 'F':
        celsius = (valor - 32) / 1.8
    elif unidade_origem == 'K':
        celsius = valor - 273.15
    else:
        celsius = valor

    if unidade_destino == 'F':
        return celsius * 1.8 + 32
    elif unidade_destino == 'K':
        return celsius + 273.15
    else:
        return celsius

print(converter_temperatura(0, 'C', 'F'))     # 32.0
print(converter_temperatura(100, 'C', 'K'))   # 373.15
print(converter_temperatura(32, 'F', 'C'))    # 0.0
print(converter_temperatura(300, 'K', 'F'))   # 80.33
print(converter_temperatura(25, 'C', 'C'))    # 25
print(converter_temperatura(25, 'X', 'C'))    # Erro