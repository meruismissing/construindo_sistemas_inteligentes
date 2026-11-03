numero = int(input("Digite um número inteiro: "))
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
print(f"O resultado ficou {resultado}")