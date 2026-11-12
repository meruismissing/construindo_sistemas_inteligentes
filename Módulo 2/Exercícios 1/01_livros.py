class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def resumo(self):
            print(f"Título: {self.titulo}")
            print(f"Autor: {self.autor}")
            print(f"Páginas: {self.paginas} páginas")

livro1 = Livro("Como Eu Era Antes de Você", "Jojo Moyes", 320)
livro2 = Livro("Harry Potter e a Câmara Secreta", "JK Rowling", 288)

livro1.resumo()
print()
livro2.resumo()

# Classe: Livro
# Instâncias: livro1 e livro2
# atributos: titulo, autor e paginas
# a alteração só afeta um, pois muda só de um.
