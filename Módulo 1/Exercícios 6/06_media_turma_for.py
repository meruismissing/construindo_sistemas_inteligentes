qtd_alunos = int(input("Quantos alunos tem na turma? "))
if qtd_alunos <= 0:
    print("Esse número é inválido.")
else:
  soma = 0
  for i in range(0, qtd_alunos):
   nota = float(input(f"Qual a nota do aluno? "))
   soma += nota
   while nota < 0 or nota > 10:
    print("Nota inválida, selecione uma de 0 a 10.")
    nota = float(input(f"Qual a nota do aluno? "))

soma = soma + nota
if nota >= 7:
    print("A nota está acima da média.")


media = soma / qtd_alunos
if media > 10 or media < 0:
    print("Essa média é inválida.")

print(f"Média da turma: {media:.2f}")