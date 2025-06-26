def copiar_arquivo(origem, destino):
    try:
        with open(origem, 'r') as arquivo_origem:
            conteudo = arquivo_origem.read()

        with open(destino, 'w') as arquivo_destino:
            arquivo_destino.write(conteudo)

        print(f"Arquivo copiado de '{origem}' para '{destino}' com sucesso.")
    except FileNotFoundError:
        print(f"Erro: o arquivo de origem '{origem}' não foi encontrado.")

copiar_arquivo("dados.txt", "copia_dados.txt")