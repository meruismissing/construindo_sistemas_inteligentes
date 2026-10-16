nota = float(input("Nota: "))

if nota >= 5:
    print("Primeira condição atendida.")

elif nota >= 7: 
    print("Segunda condição atendida.")
else:
    print("Segunda condição não atendida.")

print("Fim.") # Antes de executar, serão mostradas as mensagens: Primeira condição atendida e segunda condição atendida.
# Com elif, será mostrado apenas uma das respostas, pois se colocar mais de um if, mostra todas as respostas que se encaixem, não apenas a que se encaixou por último. Vai retornar apenas o primeiro porque o elif significa "senão se", ou seja, se não é um, é outro, mas se enquadra no primeiro também, e pelo primeiro vir antes do segundo, ele vem primeiro nisso também.
