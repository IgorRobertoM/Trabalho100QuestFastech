def escrever_novo_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
    print(f"Conteúdo escrito no arquivo '{nome_arquivo}' com sucesso.")

texto = "Esta é uma nova linha de texto.\nAqui tem outra linha."
escrever_novo_arquivo("arquivo_teste.txt", texto)