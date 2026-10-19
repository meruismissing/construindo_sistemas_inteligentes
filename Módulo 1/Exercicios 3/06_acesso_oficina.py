inscricao = input("Você possui inscrição? (sim/nao) ")

if inscricao == "sim":
  print("Pode prosseguir com seu acesso.")
elif inscricao == "nao":
  print("Você não possui inscrição, logo, seu acesso é inválido.")
  exit()

idade = int(input("Qual sua idade? "))

if idade <= 0:
  print("Idade inválida!")
if idade >= 14:
  print("Você tem idade necessária para prosseguir.")

if idade >= 14 and inscricao == "sim":
  print("Está tudo certinho, você pode acessar nossa oficina.")
