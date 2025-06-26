def filtrar_linhas(nome_arquivo_origem, nome_arquivo_destino, palavra_chave):
    try:
        with open(nome_arquivo_origem, 'r') as arquivo_origem:
            linhas = arquivo_origem.readlines()

        with open(nome_arquivo_destino, 'w') as arquivo_destino:
            for linha in linhas:

                if palavra_chave.lower() in linha.lower():
                    arquivo_destino.write(linha)

        print(f"Linhas contendo '{palavra_chave}' foram salvas em '{nome_arquivo_destino}'.")
    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo_origem}' não foi encontrado.")

filtrar_linhas("dados.txt", "linhas_filtradas.txt", "python")