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
elif tempo_nece <= tempo_disp and risco == "nao" and pista == "sim":
    print("Prioridade alta.")
elif tempo_nece <= tempo_disp and risco == "nao" and pista == "nao":
    print("Prioridade normal.")

minutos_restantes = tempo_disp - tempo_nece
if minutos_restantes >= 1:
    print("Minutos que restarão após a análise:", minutos_restantes)

# Se há risco imediato mas falta tempo, aparece que é necessário solicitar apoio porque eu coloquei em uma ordem em que se o tempo necessário é maior que o disponível, mostra essa resposta antes de qualquer outra. 
