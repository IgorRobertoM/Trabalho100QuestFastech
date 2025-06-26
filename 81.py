def anexar_conteudo(nome_arquivo, conteudo_extra):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(conteudo_extra)
    print(f"Conteúdo anexado no arquivo '{nome_arquivo}' com sucesso.")

texto_extra = "\nEsta linha será adicionada ao final do arquivo."
anexar_conteudo("arquivo_teste.txt", texto_extra)