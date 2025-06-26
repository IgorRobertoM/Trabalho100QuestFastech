def combinar_listas(*listas):
    resultado = []
    for lista in listas:
        for elemento in lista:
            resultado.append(elemento)
    return resultado

lista1 = [1, 2, 3]
lista2 = ['a', 'b']
lista3 = [True, False]

lista_combinada = combinar_listas(lista1, lista2, lista3)
print(lista_combinada)