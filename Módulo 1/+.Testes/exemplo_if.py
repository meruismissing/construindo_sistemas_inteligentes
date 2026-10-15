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

temperatura = float(input("Temperatura: "))

if temperatura >= 30:
    print("Dia quente.")
if temperatura >= 35: # com elif não mostra ambos as impressões. mostra apenas o if e não o elif. Se inverter o valor do if e o elif, funciona. ex: elif temperatura >= 30: "dia quente" e if temperatura >= 35: calor intenso
    print("Calor intenso.")

