# Leia quatro nomes e armazene-os em uma lista inicialmente vazia. Depois, mostre cada nome em uma linha, na ordem de cadastro. Nomes repetidos são permitidos.
alunos = []
a_um = input("Aluno um: ")
a_dois = input("Aluno dois: ")
a_tres = input("Aluno três: ")
a_quatro = input("Aluno quatro: ")

alunos.append(a_um)
alunos.append(a_dois)
alunos.append(a_tres)
alunos.append(a_quatro)

for aluno in alunos:
    print(" Aluno:", aluno, end="")
 