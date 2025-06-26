def ler_csv_simples(nome_arquivo):
    dados = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

        if len(linhas) > 1:
            for linha in linhas[1:]:
                linha = linha.strip() 
                valores = linha.split(",") 
                dados.append(valores)
        else:
            for linha in linhas:
                linha = linha.strip()
                valores = linha.split(",")
                dados.append(valores)

        return dados

    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
        return []

resultado = ler_csv_simples("exemplo.csv")
print(resultado)