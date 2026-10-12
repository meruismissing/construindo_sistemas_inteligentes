preco_pizza = 48.00
preco_refri = 12.00
quantidade_amigos = 4
total_conta = preco_pizza + preco_refri
total = total_conta / quantidade_amigos
print(f"Como o preço da pizza está 48.00 e o do refri está 12.00, cada um dos 4 amigos pagará 15 reais, pois no total, dá 60 reais a pizza e o refri juntos. 60 reais dividido por 4 dá R$15.00. A classe da variável final (total) é equivalente a:", type(total))
# É um float, apesar de não conter centavos, pois float são os pontos flutuantes que colocamos para dar ênfase no preço total, seja ele .00 ou, .50, por exemplo.
