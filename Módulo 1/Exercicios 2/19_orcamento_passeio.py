alunos = 25
onibus = 600.00
ingresso = 15.00
lanche = 10.00
ingresso = ingresso * alunos
lanche = lanche * alunos
total = ingresso + lanche + onibus
alunos = total / alunos
print("O custo total dos ingressos serão de R$", ingresso)
print("O custo total dos lanches serão de R$", lanche)
print("O custo total do passeio será de R$", total)
print("Cada aluno deverá pagar sua parte, e sua parte será R$", alunos)
# A quantidade de alunos aumentou, então se tornou pessoas à mais para pagar pelo passeio, fazendo o custo por pessoa diminuir.
