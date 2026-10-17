print("Olá! Bem-vindo(a) a previsão do tempo.")
sensacao = int(input("Qual a sensação térmica de hoje? "))

if sensacao < 18:
    print("O ambiente atual está frio.")
elif sensacao >= 18 and sensacao < 26:
    print("O ambiente atual está agradável.")
elif sensacao >= 26:
    print("O ambiente atual está quente!")
    
