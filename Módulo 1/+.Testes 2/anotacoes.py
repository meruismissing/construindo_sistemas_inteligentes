preco = float(input("Preço do produto: ")) # Para converter para float em só um comando, de str > float
quantidade = int(input("Quantidade: ")) # Para fazer a conversão de str para int no mesmo comando.
total = preco * quantidade
estoque = 13
if quantidade <= 13:
    print("Você pode comprar este item!")
    print("O total fica em:", total)
else:
    print("Este item não está em estoque.")


 # .lower deixa tudo minusculo
 # .upper deixa tudo maiusculo
 # .capitalize deixa tudo com letra maiuscula no começo.
 # .swapcase para inverter o estilo da fonte, como: oLAAAA = Olaaaa

# exemplos:
teste = "Meru"
print(teste)
print()
print(teste.lower())
print()
print(teste.upper())
print()
print(teste.capitalize())
print()
print(teste.swapcase())

teste = "olá pessoal. ".capitalize() + "tudo bem?".capitalize()
print(teste)

teste2 = ["Maçã", "Banana", "Laranja"]
print(teste2)