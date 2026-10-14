preco = float(input("Preço do produto: ")) # Para converter para float em só um comando, de str > float
quantidade = int(input("Quantidade: ")) # Para fazer a conversão de str para int no mesmo comando.

estoque = 13
if quantidade <= 13:
    print("Você pode comprar este item!")
else:
    print("Este item não está em estoque.")

total = preco * quantidade 

print("Total da compra:", total)