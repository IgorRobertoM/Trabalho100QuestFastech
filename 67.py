texto = "Desenvolvimento Web"

padrao_prefixo = "Desen"
padrao_sufixo = "Web"
padrao_nao_existe = "mobile"

print(padrao_prefixo, "é prefixo de texto?", texto.startswith(padrao_prefixo))

print(padrao_prefixo, "é sufixo de texto?", texto.endswith(padrao_prefixo))

print(padrao_sufixo, "é prefixo de texto?", texto.startswith(padrao_sufixo))

print(padrao_sufixo, "é sufixo de texto?", texto.endswith(padrao_sufixo))

print(padrao_nao_existe, "é prefixo de texto?", texto.startswith(padrao_nao_existe))

print(padrao_nao_existe, "é sufixo de texto?", texto.endswith(padrao_nao_existe))