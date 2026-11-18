class Turma:
    def __init__(self, nome, alunos=None):
        self.nome = nome
        self.alunos = alunos if alunos is not None else []
    
    def matricular(self, nome_aluno):
        self.alunos.append(nome_aluno)
        print(f"Aluno(a) '{nome_aluno}' matriculado(a) com sucesso na turma {self.nome}!")
    def __str__(self):
        # Define como o objeto será exibido ao usar print()
        lista_formatada = ", ".join(self.alunos) if self.alunos else "Nenhum aluno matriculado"
        return f"Turma: {self.nome} | Alunos: [{lista_formatada}]"
turma1 = Turma("Programadores do futuro")
print("=== Sistema de matrículas ===")
print("Digite 'sair' quando terminar, para sair do sistema.")
while True:
    nome_aluno = input("Insira o nome do aluno: ").strip
    if nome_aluno == "sair":
        print("\nEncerrando o cadastro de matrículas...")
        break
    if nome_aluno == "":
        print("Aviso: O nome não pode ficar em branco. Tente novamente.")
        continue

turma1.matricular(nome_aluno)