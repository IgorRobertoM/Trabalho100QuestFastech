texto = input("Digite uma palavra ou frase: ")

texto = texto.lower()

texto_sem_espacos = texto.replace(" ", "")

texto_invertido = texto_sem_espacos[::-1]

if texto_sem_espacos == texto_invertido:
    print(True)
else:
    print(False)