id_mensagem = input("Identifique a mensagem. ")
tempo_disp = float(input("Quanto tempo há disponível, em minutos? "))
tempo_nece = float(input("Quanto tempo é necessário, em minutos? "))
if tempo_disp <= 0 or tempo_nece <= 0:
    print("Tempo inválido!")
    exit()
risco = input("A mensagem indica risco imediato? (sim/nao) ")
if risco != "nao" and risco != "sim":
    print("Resposta inválida")
    exit()
pista = input("A mensagem contém uma pista recorrente? (sim/nao) ")
if pista != "nao" and pista != "sim":
    print("Resposta inválida")
    exit()
elif tempo_nece > tempo_disp:
    print("Solicitar apoio: tempo insuficiente.")
elif tempo_nece <= tempo_disp and risco == "sim":
    print("Prioridade máxima.")
