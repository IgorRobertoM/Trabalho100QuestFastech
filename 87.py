def adicionar_numero_linha(nome_arquivo_origem, nome_arquivo_destino):
    try:
        with open(nome_arquivo_origem, 'r') as arquivo_origem:
            linhas = arquivo_origem.readlines()

        with open(nome_arquivo_destino, 'w') as arquivo_destino:
            for i, linha in enumerate(linhas, start=1):
                linha_numerada = f"{i} {linha}"
                arquivo_destino.write(linha_numerada)

        print(f"Arquivo '{nome_arquivo_destino}' criado com linhas numeradas.")
    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo_origem}' não foi encontrado.")

adicionar_numero_linha("dados.txt", "dados_numerados.txt")