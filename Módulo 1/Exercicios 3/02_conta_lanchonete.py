lanche = float(input("Qual o preço do lanche? "))
quantidade = int(input("Qual a quantidade que você deseja? "))
total = lanche * quantidade
desconto = total * 0.10
print("O preço fica: R$:", {total:.2f})

if total >= 50.00:
    total = total - desconto
    print(f"O valor do desconto fica: {desconto:.2f}")
print(f"Fica, no total, R$:{total:.2f}")
