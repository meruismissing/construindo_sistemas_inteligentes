class Livro:
    def __init__(self, titulo, emprestado):
        self.titulo = titulo
        self.emprestado = emprestado
        self.emprestado = False
    def emprestar(self, emprestado):
        if emprestado == True:
            return False, f"Esse livro já foi emprestado."
        self.emprestado = True
        return True, f"Esse livro está disponível e foi emprestado agora."
    def devolver(self, emprestado):
        if emprestado == False:
            return False, f"A sua devolução não foi completa pois não há nada a ser devolvido."
        self.emprestado = False
        return True, f"Esse livro foi devolvido."

livro1 = Livro("Batman: Ano Um", False)
print(f"Título do livro: {livro1.titulo}, Emprestado: {livro1.emprestado}")
print()
sucesso, mensagem = livro1.emprestar(emprestado=False)
print(f"Você tentou emprestar o livro. {sucesso} | {mensagem}")
print(f"Título do livro: {livro1.titulo}, Emprestado: {livro1.emprestado}")
print()
sucesso, mensagem = livro1.emprestar(emprestado=True)
print(f"Você tentou emprestar o livro. {sucesso} | {mensagem}")
print(f"Título do livro: {livro1.titulo}, Emprestado: {livro1.emprestado}")
print()
sucesso, mensagem = livro1.devolver(emprestado=True)
print(f"Você tentou devolver o livro. {sucesso} | {mensagem}")
print(f"Título do livro: {livro1.titulo}, Emprestado: {livro1.emprestado}")
print()
sucesso, mensagem = livro1.devolver(emprestado=False)
print(f"Você tentou devolver o livro. {sucesso} | {mensagem}")
print(f"Título do livro: {livro1.titulo}, Emprestado: {livro1.emprestado}")