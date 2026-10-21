print("=== NÍVEIS E CLASSIFICAÇÃO ===")
print("| 1 a 5   | Aprendiz |")
print("| 6 a 15  | Guerreiro|")
print("| 16 a 30 | Veterano |")
print("| 31 ou mais|Lendário|")
nome = input("Qual é o seu nome, aventureiro? ")
nivel = int(input("Qual é o seu nível? "))

if nivel <= 0:
    print("Número inválido.")
elif 1 >= nivel <= 5:
    nivel_aventureiro = "Aprendiz"
    print("Sua classe é:", nivel_aventureiro)
elif 6 >= nivel <= 15:
    nivel_aventureiro = "Guerreiro"
    print("Sua classe é:", nivel_aventureiro)
elif 16 >= nivel <= 30:
    nivel_aventureiro = "Veterano"
    print("Sua classe é:", nivel_aventureiro)
else:
    nivel_aventureiro = "Lendário"
    print("Sua classe é:", nivel_aventureiro)
