def sao_anagramas(palavra1, palavra2):
    palavra1 = palavra1.lower().replace(" ", "")
    palavra2 = palavra2.lower().replace(" ", "")

    if sorted(palavra1) == sorted(palavra2):
        return True
    else:
        return False

print(sao_anagramas("amor", "Roma"))         
print(sao_anagramas("listen", "silent"))     
print(sao_anagramas("python", "typhon"))     
print(sao_anagramas("banana", "abacate"))    