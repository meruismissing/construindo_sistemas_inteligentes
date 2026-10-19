

nome = input("Qual o seu nome, aventureiro? ")
ouro = int(input("Quantos ouros você possui? "))
if ouro < 0:
    print("Quantidade de ouro inválida!")
    exit()
print("=== MENU ===")
print("| 1: Poção de vida (25 moedas)")
print("| 2: Escudo (60 moedas)")
print("| 3: Espada (100 moedas)")
menu = input("Escolha qual será sua compra. ")
if menu == "1":
    if ouro < 25:
        falta = 25 - ouro
        print("Você não consegue comprar isso ainda! Falta:", falta, "ouros")
    if ouro >= 25:
       print("Item adquirido: Poção de vida")
       ouro -= 25
       print("Ouro atual:", ouro)
    
elif menu == "2":
    if ouro < 60:
        falta = 60 - ouro
        print("Você não consegue comprar isso ainda! Falta:", falta, "ouros")
    if ouro >= 60:
       print("Item adquirido: Escudo")
       ouro -= 60
       print("Ouro atual:", ouro)


elif menu == "3":
    if ouro < 100:
        falta = 100 - ouro
        print("Você não consegue comprar isso ainda! Falta:", falta, "ouros")
    if ouro >= 100:
       print("Item adquirido: Espada")
       ouro -= 100
       print("Ouro atual:", ouro)
else:
    print("Item inexistente.")
