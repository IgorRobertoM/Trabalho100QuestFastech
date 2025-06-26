num = int(input("Fatorial de: "))

if num < 0:
    print("Não existe fatorial de número negativo.")
else:
    fatorial = 1
    print(f"{num}! = ", end="")
    for i in range(num, 0, -1):
        fatorial *= i
        if i != 1:
            print(f"{i} . ", end="")
        else:
            print(f"{i} = {fatorial}")