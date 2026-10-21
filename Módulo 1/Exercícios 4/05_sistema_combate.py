nome = input("Diga seu nome. ")
vida_atual = int(input("Qual sua vida atual? "))
if vida_atual <= 0:
    print("Sua vida não pode ser menor ou igual a 0.")
    exit()
love = int(input("Quantos pontos de ataque você tem? ")) # (LOVE é Level Of ViolEnce, quase a mesma coisa que pontos de ataque, por isso o nome da variavel)
if love <= 0:
    print("Seu ataque não pode ser menor ou igual a 0. Caso contrário, seu ataque não causará dano.")
    exit()
vida_inimigo = int(input("Quanto de vida o inimigo tem? "))
if love >= vida_inimigo:
    print("O inimigo será derrotado em um tapinha, pois seu dano é maior ou equivalente à vida dele.")
    exit()

defesa_inimigo = int(input("Quanto de defesa o inimigo tem? "))
if defesa_inimigo >= love:
    print("O dano não pode ser negativo!")
    exit()
print()
print("=== XINELÃO ===")
print(f"| Vida: {vida_inimigo}")
print(f"| Defesa: {defesa_inimigo}")
print("Você começa a partir para cima do Xinelão, e ele começa a jogar verdades na sua cara. Você pega sua espada e vai para cima, gritando. 'HYAAAA'.")
print()

dano = love - defesa_inimigo
print(f"Você dá uma espadada no inimigo, causando {dano} de dano!")
vida_inimigo -= dano
print(f"Agora a vida do inimigo é: {vida_inimigo} pontos de vida!")
print("Talvez você ainda não esteja à altura.")