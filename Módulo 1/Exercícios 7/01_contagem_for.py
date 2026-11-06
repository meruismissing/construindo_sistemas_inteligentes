numero = int(input("Até que número você deseja contar? "))
if numero <= 0:
    print("Valor inválido.")
    exit()

for numero in range(1, numero + 1):
    print(numero, end=" ")