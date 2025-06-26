def contar_palavras(lista_de_frases):
    import string

    contagem = {}

    for frase in lista_de_frases:
        frase = frase.lower()

        for pontuacao in string.punctuation:
            frase = frase.replace(pontuacao, "")

        palavras = frase.split()

        for palavra in palavras:
            if palavra in contagem:
                contagem[palavra] += 1
            else:
                contagem[palavra] = 1

    return contagem

frases = [
    "Olá mundo!",
    "Python é incrível, olá novamente.",
    "Mundo Python é maravilhoso."
]

resultado = contar_palavras(frases)
print(resultado)