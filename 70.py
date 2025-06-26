import random
import string

def gerar_senha(comprimento, incluir_numeros=True, incluir_simbolos=False):
    caracteres = string.ascii_letters  

    if incluir_numeros:
        caracteres += string.digits  

    if incluir_simbolos:
        caracteres += "!@#$%^&*"

    if len(caracteres) == 0:
        return "Erro: Nenhum tipo de caractere selecionado."

    senha = ""
    for i in range(comprimento):
        senha += random.choice(caracteres)

    return senha

print(gerar_senha(10))                  
print(gerar_senha(12, True, True))         
print(gerar_senha(8, incluir_numeros=False))  