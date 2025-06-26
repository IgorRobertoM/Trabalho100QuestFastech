def validar_numeros_base(lista_de_strings, base):
    digitos_validos = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    numeros_validos = []

    for numero_str in lista_de_strings:
        numero_str = numero_str.upper()

        if numero_str == "":
            continue

        valido = True

        for caractere in numero_str:
            if caractere not in digitos_validos:
                valido = False
                break
            if digitos_validos[caractere] >= base:
                valido = False
                break

        if valido:
            numeros_validos.append(numero_str)

    return numeros_validos