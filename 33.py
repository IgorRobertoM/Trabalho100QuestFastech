soma = 0
quantidade = 0
menor = None
maior = None

while True:
    temp = input("Digite uma temperatura (ou 'fim' para encerrar): ")
    
    if temp.lower() == 'fim':
        break
    
    temp = float(temp)
    soma += temp
    quantidade += 1
    
    if menor is None or temp < menor:
        menor = temp
    if maior is None or temp > maior:
        maior = temp

if quantidade == 0:
    print("Nenhuma temperatura informada.")
else:
    media = soma / quantidade
    print(f"Menor temperatura: {menor}")
    print(f"Maior temperatura: {maior}")
    print(f"Média das temperaturas: {media:.2f}")