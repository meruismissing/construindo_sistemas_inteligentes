exemplares = 8
quantidade = int(input("Qual o investimento para tal capricho? (Quantos exemplares vossa senhoria deseja?) "))
if quantidade > 8:
    print("Não temos exemplares suficientes.")
elif quantidade <= 0:
    print("Pedido inválido!")
else:
    print("Pedido confirmado!")
    total = exemplares - quantidade
    print("Agora nosso estoque é:", total, "exemplar(es)")
