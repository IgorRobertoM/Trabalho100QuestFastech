def somar_numeros_arquivo(nome_arquivo):
    try:
        total = 0
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                try:
                    numero = int(linha)
                    total += numero
                except ValueError:
                    pass
        return total
    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
        return 0

nome = "numeros.txt"
resultado = somar_numeros_arquivo(nome)
print(f"A soma dos números do arquivo é: {resultado}")