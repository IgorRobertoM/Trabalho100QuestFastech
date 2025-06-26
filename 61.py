texto_com_espacos = input("Digite um texto com espaços extras: ")

texto_sem_espacos_fim = texto_com_espacos.strip()

palavras = texto_sem_espacos_fim.split()

texto_limpo = " ".join(palavras)

print("Texto sem espaços extras:")
print(texto_limpo)