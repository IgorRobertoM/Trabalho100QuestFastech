class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")

    def __str__(self):
        return f"Livro: {self.titulo} por {self.autor}"

livro1 = Livro("Python para Iniciantes", "Maria Silva", 250)
print(livro1) 