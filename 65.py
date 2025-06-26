def extrair_substring(texto, inicio, fim):
    if inicio < 0:
        inicio = 0
    if fim > len(texto):
        fim = len(texto)
    return texto[inicio:fim]

texto_completo = "Programação em Python"
indice_inicio = 4
indice_fim = 12
resultado1 = extrair_substring(texto_completo, indice_inicio, indice_fim)
print(resultado1)
texto_completo_2 = "ABCDE"
indice_inicio_2 = 1
indice_fim_2 = 10
resultado2 = extrair_substring(texto_completo_2, indice_inicio_2, indice_fim_2)
print(resultado2)