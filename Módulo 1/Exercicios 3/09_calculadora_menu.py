numero1 = int(input("Qual é o primeiro número? "))
numero2 = int(input("Qual é o segundo número? "))
if numero1 <= 0 or numero2 <= 0:
    print("Você não pode dividir por zero!")
    exit()
print("Menu: 1: somar, 2: subtrair, 3: multiplicar, 4: dividir.")
escolha = input("Qual opção você escolhe? ")
somar = numero1 + numero2
subtrair = numero1 - numero2
multiplicar = numero1 * numero2
dividir = numero1 / numero2
if escolha == "1":
    print("Resultado:", numero1 + numero2)
elif escolha == "2":
    print("Resultado:", numero1 - numero2)
elif escolha == "3":
    print("Resultado:", numero1 * numero2)
elif escolha == "4":
    print("Resultado:", numero1 / numero2)


if escolha >= "5":
    print("Opção inválida.")
