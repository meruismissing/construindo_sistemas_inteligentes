alunos = int(input("Quantos alunos têm na turma? "))
while alunos <= 0:
    print("Esse número é inválido!")
    alunos = int(input("Quantos alunos têm na turma? "))

print("Prosseguindo...")
total_alunos = alunos
soma = 0

contador = 0
while contador < total_alunos:
    contador += 1
    nota = float(input(f"Qual a nota do aluno {contador}? "))
    soma += nota

media = (soma / total_alunos)

print("a média final é:", media)
