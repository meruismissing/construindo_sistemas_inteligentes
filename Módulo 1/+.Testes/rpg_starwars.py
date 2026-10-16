nome = "Anakin"
vida = 172
forca = 86
raca = "Humano"

print(f"Ficha inicial: {nome}")
print(f"| Vida: {vida}        |")
print(f"| Força: {forca}        |")
print(f"| Raça: {raca}    |")

print("Anakin Skywalker, desde criança, sempre quis ser um grande contribuidor para as tecnologias do universo, com 9 anos inventou seu primeiro droide, C-3PO, e no mesmo ano, aconteceu algo que mudou sua vida. Imagine se você fosse ele?")
participar = input("Gostaria de imaginar? (sim/nao) ")

if participar == "nao": 
    print("Comando cancelado")
    print("Você é bem vindo à tentar de novo a qualquer momento.")
    print()
    exit()
print("﹒┈ ﹒┈ ﹒☆ ﹒┈ ﹒┈ ﹒")
print("Você acorda em Mustafar... De frente para Padmé Amidala, sua esposa, que está segurando seu próprio pescoço em defesa do seu ataque, você estava quase enforcando ela. Então aparece Obi Wan Kenobi, seu tão querido companheiro, sai da nave de Padmé. Automaticamente, seu cérebro se contorce e você começa a ficar paranóico, pensando: 'O que ele está fazendo na nave de Padmé?', mas é um caminho sem volta.")


acao = input("Você tem 3 ações em relação a Padmé. Lutar, poupar ou escapar. Escolha uma.")

if acao == "matar":
    print("Você entra em uma luta com Padmé Amidala, sua esposa. Em seguida, Obi Wan parte para cima e corta seu braço fora. Fim de jogo.")

elif acao == "escapar":
    print("Você fugiu para sua nave, conseguindo escapar de tudo aquilo que sempre teve medo de fazer, mas fez, você traiu todos e é um caminho sem volta, você está sendo procurado na galáxia inteira. Fim de jogo.")

elif acao == "poupar":
    print("Você poupou Padmé")

else:
    print("Opção inválida, jovem Anakin.")
    
