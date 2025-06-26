def substituir_em_arquivo(nome_arquivo, texto_antigo, texto_novo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()

        conteudo_modificado = conteudo.replace(texto_antigo, texto_novo)

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(conteudo_modificado)

        print(f"Substituições feitas com sucesso no arquivo '{nome_arquivo}'.")
    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")

substituir_em_arquivo("dados.txt", "Olá", "Oi")