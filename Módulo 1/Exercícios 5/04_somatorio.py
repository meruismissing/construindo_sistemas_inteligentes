um = int(input("Primeiro número: "))
dois = int(input("Segundo número: "))
tres = int(input("Terceiro número: "))
quarto = int(input("Quarto número: "))
quinto = int(input("Quinto número: "))
contador = 1
acumulador = (um + dois + tres + quarto + quinto)

while contador != 0 and acumulador != contador:
    contador = acumulador
    print("Soma total:", acumulador)

print("Fim!")