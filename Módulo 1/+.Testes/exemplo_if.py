idade = int(input("Qual é a sua idade? "))

if idade >= 18:
    print("Você é maior de idade, seu acesso foi autorizado.")
else: 
    print("Seu acesso foi negado. Razão: Menor de idade")

media = float(input("Digite a média de 0 a 10: "))

if media >= 7:
    print(f"Média: {media:.2f}, Aprovado")
elif media >= 5:
    print(f"Média: {media:.2f}, Em recuperação.")
else: 
    print(f"Média: {media:.2f}, Reprovado.")
