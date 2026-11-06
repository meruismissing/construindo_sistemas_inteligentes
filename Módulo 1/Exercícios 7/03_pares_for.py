numero = int(input("Até que número você deseja ver os pares? "))
numero_real = numero
if numero == 1:
    print("Número sem pares no intervalo!")
elif numero <= 0:
    print("Número inválido.")
for numero in range(2, numero_real + 1, 2):
    print(numero, end=" ")

print("Fim!")
