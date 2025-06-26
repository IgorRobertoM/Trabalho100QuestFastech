n = int(input("Digite o número de termos da série H: "))

h = 0

for i in range(1, n + 1):
    h += 1 / i  

print("O valor de H é:", h)