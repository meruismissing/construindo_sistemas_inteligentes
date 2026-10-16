nome = "Anakin"
vida = 172
forca = 86
raca = "Humano"

print(f"Ficha inicial: {nome}")
print(f"| Vida: {vida}        |")
print(f"| Força: {forca}        |")
print(f"| Raça: {raca}    |")

print("Anakin Skywalker, desde criança, sempre quis ser um grande contribuidor para as tecnologias do universo, com 9 anos inventou seu primeiro droide, C-3PO, e no mesmo ano, aconteceu algo que mudou sua vida. Imagine se você fosse ele?")
<<<<<<< HEAD
participar = input("Gostaria de imaginar? (sim/nao) ")
=======
participar = input("Gostaria de imaginar? (sim/nao) ").lower()
>>>>>>> 3c045a6c4a37c8f01810705d37d2603d79a4702b

if participar == "nao": 
    print("Comando cancelado")
    print("Você é bem vindo à tentar de novo a qualquer momento.")
    print()
    exit()
<<<<<<< HEAD
print("﹒┈ ﹒┈ ﹒☆ ﹒┈ ﹒┈ ﹒")
print("Você acorda em Tatooine... mergulhado na areia escaldante após uma tempestade. Você percebe que foi transformado em, ninguém mais, ninguém menos que: Anakin Skywalker. Você se levanta e procura pela sua mãe, mas olha seus trajes e percebe em que momento da sua vida você está. Sua mãe morrerá em breve. Nos seus braços.")
=======

elif participar == "sim":
 print("﹒┈ ﹒┈ ﹒☆ ﹒┈ ﹒┈ ﹒")
 print("Você acorda em Mustafar... De frente para Padmé Amidala, sua esposa, que está segurando seu próprio pescoço em defesa do seu ataque, você estava quase enforcando ela. Então aparece Obi Wan Kenobi, seu tão querido companheiro, sai da nave de Padmé. Automaticamente, seu cérebro se contorce e você começa a ficar paranóico, pensando: 'O que ele está fazendo na nave de Padmé?', mas é um caminho sem volta.")
 print()
else:
  exit()

acao = input("Você tem 3 ações em relação a Padmé. Lutar, poupar ou escapar. Escolha uma. ").lower()
print()

if acao == "matar":
    print("Você entra em uma luta com Padmé Amidala, sua esposa. Em seguida, Obi Wan parte para cima e corta seu braço fora. Fim de jogo.")

elif acao == "escapar":
    print("Você fugiu para sua nave, conseguindo escapar de tudo aquilo que sempre teve medo de fazer, mas fez, você traiu todos e é um caminho sem volta, você está sendo procurado na galáxia inteira. Fim de jogo.")

elif acao == "poupar":
    print("Você poupou Padmé, uma escolha sábia a se fazer, afinal, você pode até ser covarde, mas nem tanto. Você vai em direção de Obi Wan e começa a discutir. Obi wan começa: 'Você permitiu que esse lorde sombrio desvirtuasse sua mente, e agora você se tornou justamente o que jurava destruir', Anakin se defende: 'Eu dispenso o sermão, Obi Wan, eu descobri as mentiras dos Jedi, eu não temo o lado sombrio como você, e eu trouxe a paz, liberdade, justiça e a segurança para meu novo império.'. Obi Wan debocha: 'Seu novo império?', Anakin responde com raiva: 'Não me obrigue a matar você.' Obi Wan rebate:'Anakin, meu compromisso é com a República, com a democracia!', Anakin conclui: 'Se você não é meu aliado, então é meu inimigo.' Obi Wan, por vez, lança fatos. 'Só um Sith pensa de uma forma tão amoral. Farei o que for necessário.'. Anakin ameaça. 'Você vai tentar.' Ambos puxam o sabre de luz.") 

else:
  exit()

continuar = input("Você tem certeza que vai continuar? Você pode se render. Continuar? (sim/nao) ").lower()
print()
if continuar == "sim":
  print("Vocês dois começam uma intensa luta de sabres, enquanto caminham até perto do líquido que está em calor intenso. Um tentando jogar o outro. Até entrarem em uma sala, e Anakin começar a enforcar Obi Wan, Obi Wan consegue se defender e chuta Anakin para o chão e então tenta cortá-lo, mas falha, então ambos se levantam e tentam lutar usando a força, acabam estragando um painel que começa a fazer transbordar lava. Eles vão para fora novamente e Obi Wan se equilibra entre canos, Anakin tenta o acertar mas não consegue, então Obi Wan volta para o chão, e ambos continuam sem cessar por nenhum momento. Nem ao menos hesitar. A lava transborda e começa a derreter todo o local em volta deles, obrigando eles a tentar procurar um local seguro. Eles caem num destroço e usam como se fosse um barco, Anakin quase cai, mas eles continuam. Eles se balançam e tentam se acertar, enquanto Obi Wan cai em uma plataforma minúscula, Anakin sobe em um droide voador e vai até Obi Wan, e tenta com tudo que pode, matar ele. Obi Wan desabafa: 'Eu falhei contigo, Anakin, eu falhei contigo', Anakin ignora. Anakin: 'Eu devia saber que os Jedi estavam tentando tomar o poder', Obi Wan, com raiva, começa a brigar incessantemente. 'Anakin, Chanceler Palpatine é maligno', Anakin rebate: 'Do meu ponto de vista, maligno são os Jedi!' Obi Wan, entretanto, se decepciona amargamente. Obi Wan: 'Você já não tem solução!'. Eles continuam, se olhando, e Anakin termina seu discurso com: 'É o seu fim, mestre.'. Obi Wan, continua tentando atacar Anakin, e continua falhando, até Obi Wan dar um salto para trás e ficar em terreno firme. 'Acabou, Anakin! Eu estou em terreno firme!', Anakin olha com muita raiva para Obi Wan e diz: 'Você subestima meu poder.' Obi Wan pede: 'Não faça isso'.")
  print()
  pular = input("Você ainda tem uma última chance! Se render ou pular em direção de Obi Wan? É sua decisão final, isso mudará tudo. (render/pular) ").lower()
  print()
  if pular == "pular":
    print("Você pula em direção de Obi-wan, e ele corta suas pernas com o sabre, você grita em agonia e cai muito perto da lava, que está subindo lentamente. 'Você era o escolhido! Foi dito que você iria destruir os Sith, não se juntar a eles! Trazer o equilíbrio para a força, não jogá-la nas trevas!', Anakin grita: 'EU TE ODEIO!', seus olhos fervendo por conta da lava, Obi Wan começa um discurso triste: 'Você era meu irmão, Anakin. Eu amava você.' Anakin começa a queimar por conta da lava, e queima por inteiro. Mas permanece vivo. Você quem escolheu isso. Padmé se encontra numa maca, no meio de seu parto, perguntando: 'O Anakin está bem?' e Obi Wan apenas acaricia o rosto dela, quieto. Padmé adormece e eles vão de volta para Coruscant.")

elif pular == "render":
  print("Anakin: 'Você não pode me deter, mas eu sei que meu caminho não tem outra escolha a não ser permanecer ao lado dos Jedi. Essa não vai ser minha morte. Não tenho porquê morrer dessa forma, nesse lugar e justamente morrer para você. Eu não teria nenhum orgulho.', Obi Wan dá uma escolha final:'Anakin, se você não fosse tão amoral e insolente, talvez teria uma vida melhor, com Padmé e seus filhos. Te dou esta última chance, para não se tornar um Sith e não morrer nas minhas mãos, não sabe como é uma pessoa tão querida morrer nas suas mãos, ou não se lembra de sua mãe?', Anakin: 'Você não sabe de nada sobre minha mãe, não venha falar dela!' Obi Wan percebe que, nem mesmo se ele quisesse se render, não teria volta. Ele já se tornou um Sith há muito tempo. Você não tem nenhuma escolha se não: Fim de jogo.")

else:
    print("Opção inválida, jovem Anakin!")
    exit()
>>>>>>> 3c045a6c4a37c8f01810705d37d2603d79a4702b
