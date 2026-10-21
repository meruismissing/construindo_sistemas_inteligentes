salario = float(input("Qual a estimativa do seu salário mensal? "))
if salario >= 2000.0:
    print(f"Seu salário é {salario}.")
    print("Seu salário é válido.")
elif salario < 2000.0:
    print("Salário inválido.")
    motivo = "Salário inválido."
    print("Empréstimo recusado. Motivo:", motivo)
    exit()
valor_solicitado = float(input("Qual o valor solicitado para empréstimo? "))
if valor_solicitado >= salario * 10:
    print("Você não pode solicitar um empréstimo que ultrapasse seu salário em 10 vezes ou mais!")
    motivo = "Empréstimo excede o salário."
    print("Empréstimo recusado. Motivo:", motivo)
    exit()
parcelas_quantidade = int(input("Em quantas parcelas você irá pagar? "))
if 0 <= parcelas_quantidade > 48:
    print("Quantidade de parcelas têm que estar entre 1 e 48.")
    motivo = "Quantidade de parcelas excede 48 ou é menor que 1."
    print("Empréstimo recusado. Motivo:", motivo)
    exit()
elif parcelas_quantidade >= salario % 30:
    print("Quantidade de parcelas não pode ultrapassar 30% do salário.")
    motivo = "Quantidade de parcelas excede 30% do salário."
    print("Empréstimo recusado. Motivo:", motivo)
    exit()
elif 1 >= parcelas_quantidade <= 48:
    print("A quantidade de parcelas está correta.")
