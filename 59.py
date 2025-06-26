texto = input("Digite uma frase ou palavra: ")

texto = texto.lower()

vogais = "aeiou"

contador_vogais = 0
contador_consoantes = 0

for letra in texto:
    if letra.isalpha():
        if letra in vogais:
            contador_vogais += 1
        else:
            contador_consoantes += 1

print("Número de vogais:", contador_vogais)
print("Número de consoantes:", contador_consoantes)