idade = int(input("Idade: ")) # Não tinha int, ia contar como string e não daria certo no if
autorizacao = input("Possui autorização? (sim/nao): ") 

if idade >= 16 and autorizacao == "sim": # Faltou um = porque quando é para comparar uma palavra com outra, é usado ==.
    print("Participação permitida.") # Tava sem identação correta.
else:
    print("Participação não permitida.")

# Mesmo com a idade necessária, ainda não é permitido se não possuir autorização. Mesmo com autorização, precisa da idade. 