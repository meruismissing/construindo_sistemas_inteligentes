nome = input("Digite o seu nome completo: ")
print(f"Olá, {nome}! Seja bem-vindo(a)!")

idade = input("(︶⑅︶)っ Qual sua idade? ")
idade = int(idade)

print(idade)
print(type(idade))

if idade <= 18:
 print("Pelo visto você é menor de idade, recomendo que prossiga com seu responsável legal.")