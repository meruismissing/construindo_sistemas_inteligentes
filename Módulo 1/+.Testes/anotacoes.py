preco = float(input("Preço do produto: ")) # Para converter para float em só um comando, de str > float
quantidade = int(input("Quantidade: ")) # Para fazer a conversão de str para int no mesmo comando.
total = preco * quantidade
estoque = 13
if quantidade <= 13:
    print("Você pode comprar este item!")
    print("O total fica em:", total)
else:
    print("Este item não está em estoque.")
    print("Produto fora de estoque!")
 