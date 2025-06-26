class Livro:
    total_livros = 0 

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        Livro.total_livros += 1  

    def detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")

    @classmethod
    def mostrar_total_livros(cls):
        print(f"Total de livros criados: {cls.total_livros}")

livro1 = Livro("Python para Iniciantes", "Maria Silva", 250)
livro2 = Livro("Aprendendo Programação", "João Souza", 300)

livro1.detalhes()
livro2.detalhes()

Livro.mostrar_total_livros() 