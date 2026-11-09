produto_preco = 12.00
produto_quantidade = 5
produto_preco2 = 13.00
produto_quantidade2 = 6
produto_preco3 = 14.00
produto_quantidade3 = 7
produto_preco4 = 15.00
produto_quantidade4 = 8

print(f"Valor total do produto 1: {produto_preco * produto_quantidade}")
print(f"Valor total do produto 2: {produto_preco2 * produto_quantidade2}")
print(f"Valor total do produto 3: {produto_preco3 * produto_quantidade3}")
print(f"Valor total do produto 4: {produto_preco4 * produto_quantidade4}")

def total_venda(valor, quantidade):
    return valor * quantidade

print(total_venda(10.50, 33.7))

