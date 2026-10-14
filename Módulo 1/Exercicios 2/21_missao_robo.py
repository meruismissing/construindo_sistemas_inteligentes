nome = "Atlas"
energia = 100 
distancia_metros = 0
amostras = 0
missao_andamento = True 

print("Nome:", nome)
print("Energia:", energia)
print("Distância percorrida, em metros:", distancia_metros)
print("Amostras coletadas:", amostras)
print("Missão em andamento:", missao_andamento)

distancia_metros += 120
energia -= 20
print("O robô percorre 120 metros e consome 20 pontos de energia.")
amostras += 3 
energia -= 15
print("Ele coleta 3 amostras e consome 15 pontos de energia.")
energia += 10
print("Recarrega 10 pontos de energia.")
distancia_metros += 80
energia -= 25
print("Ele percorre mais 80 metros e consome 25 pontos de energia.")
amostras += 2
energia -= 10
print("Coleta mais 2 amostras e consome 10 pontos de energia.")
missao_andamento = False 
print("Missão encerrada com sucesso.")
print("Ficha atualizada:")
print("Nome:", nome)
print("Energia:", energia)
print("Distância percorrida, em metros:", distancia_metros)
print("Amostras coletadas:", amostras)
print("Missão em andamento:", missao_andamento)
metros_minuto = distancia_metros / 4
print("Metros percorridos p/ minuto:", metros_minuto)
