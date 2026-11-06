notas = []

for numero in range(1, 5):
    nota = float(input("Digite uma nota de 0 a 10: "))
    notas.append(nota)

total = 0
aprovados = 0

for nota in notas:
    total += nota
    while nota < 0 or nota > 10:
        nota = float(input("Nota anterior inválida. Digite uma nota de 0 a 10: "))
    while nota >= 7:
        aprovados += 1
        break

media = total / len(notas)

print(f"Notas registradas: {notas}")
print(f"Média da turma: {media}")
print("Quantos alunos foram aprovados:", aprovados)

