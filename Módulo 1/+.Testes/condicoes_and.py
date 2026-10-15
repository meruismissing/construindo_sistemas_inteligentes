idade = int(input("Idade: "))
vagas = int(input("Vagas disponíveis: "))

if idade >= 14 and vagas > 0:
    print("Inscrição permitida.")
else:
    print("Inscrição não permitida.")

categoria = input("Categoria (estudahte, professor ou visitante): ")
if categoria == "estudante" or categoria == "professor":
    print("Desconto disponível.")
else:
    print("Sem desconto.")
idade = 16
categoria = "estudante"

if idade >= 14 and (categoria == "estudante" or categoria == "professor"):
    print("Pode participar da atividade.")

resposta = input("O robô está em manutenção? (sim/nao): ")
em_manutencao = resposta == "sim"

if not em_manutencao:
    print("Robô disponível para uma missão.")
else: 
    print("Aguarde o fim da manutenção.")

quantidade = int(input("Quantidade desejada: "))
estoque = 10

if quantidade > 0:
    if quantidade <= estoque:
        estoque = estoque - quantidade
        print("Pedido confirmado.")
        print("Estoque restante:", estoque)
    else:
        print("Estoque insuficiente.")
else:
    print("A quantidade deve ser maior que zero.")

    