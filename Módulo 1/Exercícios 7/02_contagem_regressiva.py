numero = int(input("Quanto tempo até o lançamento? "))
if numero <= 0:
    print("Valor inválido.")
    exit()
num_real = numero
for numero in range(num_real, 0, -1):
    print(numero, end=" ")

print("Lançamento realizado.")