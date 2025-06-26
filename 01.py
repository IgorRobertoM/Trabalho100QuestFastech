while True:
    nota = float(input("Escreva uma nota entre 0 a 10: "))
    if 0 <= nota <= 10:
        print("Nota valida:", nota)
    else:
        print("Nota incorreta!")