def contar_linhas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            return len(linhas)
    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
        return 0

nome = "dados.txt"
total = contar_linhas(nome)
print(f"O arquivo '{nome}' tem {total} linhas.")