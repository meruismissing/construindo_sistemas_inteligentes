horas = int(input("Quantas horas seu veículo permaneceu estacionado? Escreva numericamente, não por extenso. "))
print()
dindin_cliente = float(input("Quantos dindins você tem? "))
if horas <= 0:
    print("Horas inválidas.")
elif 1 >= horas <= 2:
    print("O valor total que deve ser pago é: R$10,00.")
    valor = 10.00
    dindin_cliente -= 10.00
    print("Agora você tem:", dindin_cliente, "dinheiros")
elif 2 < horas <= 5:
    print("O valor total que deve ser pago é: R$20,00.")
    valor = 20.00
    dindin_cliente -= 20.00
    print("Agora você tem:", dindin_cliente, "dinheiros")
elif horas > 5:
    print("O valor total que deve ser pago é: R$30,00.")
    valor = 30.00
    dindin_cliente -= 30.00
    print("Agora você tem:", dindin_cliente, "dinheiros")